#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  3 10:31:54 2022

@author: nf18p046
"""
import time

            
def place_reservee(cur, num, idParking, date):
    cur.execute("SELECT * FROM ComptePlace WHERE (num = '%s' AND parking = '%s'\
                                                  AND (horaire < '%s' AND (horaire + INTERVAL '1 HOUR' > '%s')) )"\
                                                    %(num, idParking, date, date))
    res = cur.fetchone()
    cur.fetchall()
    return (res is not None)

def prix_place(cur, idParking):
    cur.execute("SELECT Zone.prix FROM Parking, Zone WHERE (Zone.nom = Parking.zone AND Parking.idParking = '%s')"%(idParking))
    return str(cur.fetchone()[0])

"""def res_place(cur, num, idParking):
    cur.execute("SELECT Zone.prix FROM Parking, Zone WHERE (Zone.nom = Parking.zone AND Parking.idParking = '%s')"%(idParking))
    return cur.fetchall()
"""

def manage_reservations(cur, userId):
    usr_input = -1
    while int(usr_input):
        print("-----Espace de réservation-----")
        print("1 : Réserver une place")
        print("2 : Gérer mes réservations")
        print("3 : Afficher mes réservations")
        print("0 : Retourner mon espace utilisateur")
        usr_input = input("Votre choix : ")
        if(usr_input == "1"):
            reserver_place(cur, userId)
        elif(usr_input == "2"):
            gerer_reservation(cur, userId)
        elif(usr_input == "3"):
            afficher_reservation(cur, userId)


def reserver_place(cur,userId):
    print("Choisissez un parking:")
    cur.execute("SELECT idparking, nb_places, nb_personnes FROM parking")
    res = cur.fetchone()
    print("fetched!")
    while res:
        if res[2]==res[1]:
            res = cur.fetchone()
            continue
        if(res[1] - res[2] > 0):
            print("numero de parking: ", res[0],"    place disponible: ", res[1]- res[2])
        res = cur.fetchone()
    choix_parking = input("Votre choix de parking: ")
    cur.execute("SELECT num, type_vehicule, type_place FROM PLACE WHERE parking={}".format(choix_parking));
    res = cur.fetchone()
    if(res is None):
        print("Pas de place disponible !")
    while (res is not None):
        print("numero de place: ", res[0],"    type_vehicule: ", res[1], " type_place: ", res[2], \
              " prix : ", str(prix_place(cur, choix_parking)))
        res = cur.fetchone()
    choix_place = int(input("Votre choix de place: "))
    choix_horaire = input("Quand entrez-vous: au format YYYY-MM-DD HH:MM:SS : ")
    time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
    if(choix_horaire < time_now):
        print("Erreur choix horaire")
        return
    if(place_reservee(cur, choix_place, choix_parking, choix_horaire) == True):
        print("La place est déjà réservée à cet horraire !")
        return

    cur.execute("SELECT count(*) FROM RESERVATION")
    idreservation = cur.fetchone()[0] + 1
    sql_insert = "INSERT INTO RESERVATION VALUES({},{},{},{},'{}')".format(idreservation, userId, choix_place, choix_parking, choix_horaire)
    cur.execute(sql_insert)

def gerer_reservation(cur,userId):
    time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
    sql_trouve_reservation = "SELECT * FROM reservation WHERE compte={} AND horaire > '{}'".format(userId,time_now)
    cur.execute(sql_trouve_reservation)
    res = cur.fetchone()
    if (res is None):
        print("pas de reservation valide")
        return
    list_idres = []
    while (res is not None):
        print("idreservation: ",res[0],"    numero place: ",res[2],"    parking: ",res[3],"horaire: ",res[4])
        list_idres.append(res[0])
        res = cur.fetchone()
    usr_input = -1
    while(usr_input != "0" and len(list_idres)!=0):
        print("-----Modification Réservation----")
        print("1 : supprimer une reservation")
        print("2 : modifier une data")
        print("0 : retourner page précédente")
        usr_input = input("Votre choix: ")
        if usr_input == "1":
            idsup = int(input("Quelle reservation voulez-vous supprimer: "))
            if idsup not in list_idres:
                print("Invalide reservation!")
                continue
            sqlsup = "DELETE FROM RESERVATION WHERE idres='{}'".format(idsup)
            cur.execute(sqlsup)
            list_idres.remove(idsup)
        if usr_input == "2":
            afficher_reservation(cur, userId)
            idmod = int(input("Quelle reservation voulez-vous modifier: "))
            if idmod not in list_idres:
                print("Invalide reservation!")
                continue
            datemod = input("Entrez-vous la date nouvelle de cette reservation: (YYYY-MM-DD HH:MM:SS) ")
            time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
            if(datemod < time_now):
                print("Erreur choix horaire")
                return
            sqlmod = "UPDATE RESERVATION SET horaire='{}' WHERE idres={};".format(datemod, idmod)
            cur.execute(sqlmod)
    
def afficher_reservation(cur, userId):
    cur.execute("SELECT * FROM Reservation WHERE (Reservation.compte = '%d')"%(userId))
    res = cur.fetchall()
    if(res is None):
        print("Pas de réservations à afficher !")     
    else:
        for row in res:
            print("numero réservation : ", row[0], "numero place: ",row[2],"    parking: ",row[3],"horaire: ",row[4])

