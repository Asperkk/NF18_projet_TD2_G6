#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  3 10:30:50 2022

@author: nf18p046
"""
import user, admin_place, admin_subscriptionZone
       
def display_admin_space(cur):
    
    print("------- Espace Administrateur -------")
    usr_input = -1
    while(usr_input != "0"):
        print("1 : Gérer les Parkings") #Gestion Parkings, modifs parkings, création parking et places
        #Si pas assez de places dans le parking : on oblige l'admin à les créer
        print("2 : Gérer les places") # Modifier places, supprimer des places (Penser à changer place_disponible)
        print("3 : Gérer les Zones") #Modifs Zones, création zones
        print("4 : Gérer les abonnements")# Créer et modifier les abonnements
        print("5 : Afficher les transactions") # Stats, commandes avec group by, nombre de tickets par
        #utilisateur, view avec Transactions pour l'affichage
        print("0 : Quitter l'espace administrateur")
        usr_input = input("Votre choix : ")
        
        if(usr_input == "1"):
            manage_parkings(cur)  
            
        elif(usr_input == "2"):
            admin_place.manage_place(cur)  
            
        elif(usr_input == "3"):
            admin_subscriptionZone.manage_zones(cur)  
            
        elif(usr_input == "4"):
            admin_subscriptionZone.manage_subscriptions(cur)
            
        elif(usr_input == "5"):
            display_transaction(cur)
            
            
def manage_parkings(cur):
   print("------- Espace Parkings -------\n")
   usr_input = -1
   while(usr_input != "0"):
       print("1 : Afficher tous les parkings")
       print("2 : Créer un parking") 
       print("3 : Supprimer un parking")
       print("4 : Modifier un parking")
       print("0 : Quitter l'espace parkings")
       usr_input = input("Votre choix : ")   
       if(usr_input == "1"):
         display_parkings(cur)  
            
       elif(usr_input == "2"):
         create_parking(cur)  
            
       elif(usr_input == "3"):
         delete_parking(cur)
            
       elif(usr_input == "4"):
         update_parking(cur)
         
         
def display_parkings(cur):
    cur.execute("SELECT idParking, nom, prix, nb_places, nb_personnes FROM Parking, Zone WHERE (Zone.nom = Parking.zone)")
    for row in cur.fetchall():
        print("numParking : %d, zone : %s, prix : %d, nb_places disponibles : %d, nb_personnes : %d \n"%(row[0], row[1], row[2], row[3], row[4]))
        
def create_parking(cur):
    print("\n Zones disponibles pour créer un parking : \n")
    display_zones(cur)
    zone = input("Entrez un nom de zone : ")
    if(check_zone_exist(zone, cur) == False):
        print("La Zone entrée n'existe pas !\n")
        return
    nb_places = int(input("Entrez le nombre de places : "))
    new_id = user.generate_id("idParking", "Parking", cur)
    cur.execute("INSERT INTO Parking VALUES('%d', '%d', '0', '%s')"%(new_id, nb_places, zone))
    for i in range(nb_places):
        print("\n-------")
        admin_place.add_place_db(new_id, cur)
    print("Le parking a été créé !")
    
def delete_parking(cur):
    print("Parkings à supprimer : \n")
    display_parkings(cur)
    idPark = int(input("Id du parking à supprimer : "))
    if(check_id_exist('idParking', idPark, 'Parking', cur) == False):
        print("Le parking saisi n'existe pas !")
        return
    print('\033[93m' + "Etes vous sur de vouloir supprimer le parking : '%d' ? Sa suppression détruira toutes les données liées à ce parking !")
    choix = input("Etes vous sur ? (Y/N) \n")
    if(choix == "Y"):
        delete_parking_from_db(idPark, cur)

def update_parking(cur):
    print("Quels Parkings voulez vous modifier ? : \n")
    display_parkings(cur)
    parking = int(input("Entrez un numéro de parking : "))
    usr_input = -1
    while(usr_input != "0"):
        print("-----Modification Parking----")
        print("1 : Modifier le nombre de places")
        print("2 : Modifier zone")
        print("0 : retourner page précédente")
        
        usr_input = input("Votre choix: ")
        cur.execute("SELECT idParking, nb_places, zone FROM Parking WHERE (idParking = '%d')"%(parking))
        info_parking = cur.fetchone()
        if usr_input == "1":
            nb_places = int(input("Entrez le nouveau nombre de places : "))
            if(nb_places < info_parking[1]):
                for i in range(info_parking[1] - nb_places):
                    print("\nVeuillez choisir une place à supprimer : ")
                    admin_place.delete_place_db(parking, cur)
            elif(nb_places > info_parking[1]):  
                print("\n Création de nouvelles places : ")
                for i in range(nb_places - info_parking[1]):
                    admin_place.add_place_db(parking, cur)
            cur.execute("UPDATE Parking SET nb_places = '%d' WHERE (idParking = '%d')"%(nb_places, parking))
        elif usr_input == "2":
            zone = input("Entrez un nom de zone : ")
            if(check_zone_exist(zone, cur) == False):
                print("La Zone entrée n'existe pas !\n")
                return   
            cur.execute("UPDATE Parking SET zone = '%s' WHERE (idParking = '%d')"%(zone, parking))
         
def display_transaction(cur):
    print("------Espace Transaction------")
    usr_input=-1
    while(usr_input!="0"):
        print("1: Nombre de tickets achetés par client")
        print("2: Somme totale depense par client")
        print("3: benefice fait par type de vehicule ")
        print("4: benefice fait par parking")
        print("5: liste des transactions entre 2 dates")
        print("0: Quitter l'Espace Transaction")
        usr_input=input("Votre choix:")
        if usr_input=='1':
            sql=("SELECT email, COUNT(ticket) FROM TransactionCompte GROUP BY email ORDER BY COUNT(ticket) DESC")
            cur.execute(sql)
            ligne= cur.fetchone()
            while ligne:
                print("Ont été achetés " + str(ligne[1]) + " tickets sous l'email suivant " + str(ligne[0]))
                ligne=cur.fetchone()
        elif usr_input=='2':
            sql=("SELECT email, sum(montant) FROM TransactionCompte GROUP BY email ORDER BY sum(montant) DESC")
            cur.execute(sql)
            ligne= cur.fetchone()
            while ligne:
                print("Un montant total de  " + str(ligne[1]) + " euros a été dépensé sous l'email suivant " + str(ligne[0]))
                ligne=cur.fetchone()
        elif usr_input=='3':
            sql=("SELECT type_vehicule, sum(montant) FROM TransactionDate GROUP BY type_vehicule ORDER BY sum(montant) DESC")
            cur.execute(sql)
            ligne= cur.fetchone()
            while ligne:
                print("Vous avez reçu " +str(ligne[1]) + " euros pour le type de véhicule suivant:  " + str(ligne[0]))
                ligne=cur.fetchone()
        elif usr_input=='4':
            sql=("SELECT parking, sum(montant) FROM TransactionDate GROUP BY parking ORDER BY sum(montant) DESC")
            cur.execute(sql)
            ligne= cur.fetchone()
            while ligne:
                print("Vous avez reçu " +str(ligne[1]) + " euros pour parking suivant:  " + str(ligne[0]))
                ligne=cur.fetchone()
        elif usr_input=='5':
            de=input("Veuillez saisir la date de début sous la forme suivante: yyyy-mm-dd hh:mm:ss ")
            a=input("Veuillez saisir la date de fin finie  sous l'une des forme suivante 'yyyy-mm-dd hh:mm:ss' ")
            sql=("SELECT ticket,email,montant FROM TransactionDate WHERE horaire_entree BETWEEN '%s' AND '%s' " %(de,a) )
            cur.execute(sql)
            ligne=cur.fetchone()
            while ligne:
                print("Le compte " +str(ligne[1])+" a acheté le ticket numero " +str(ligne[0])+ "  pour un montant de " + str(ligne[2])+ " sur la période désignée")
                ligne = cur.fetchone()
                
def display_zones(cur):
    sql = "SELECT * FROM zone"
    cur.execute(sql)
    donnee = cur.fetchall()
    for ligne in donnee:
        print("Zone : %-20s\tPrix : %.2f \n"%(ligne[0],ligne[1]))
            
def check_zone_exist(nom, cur):
    cur.execute("SELECT * FROM Zone WHERE(nom = '%s')"%(nom))
    return (cur.fetchone() is not None)

    

def check_id_exist(idName, idValue, table, cur):
    cur.execute("SELECT * FROM %s WHERE(%s = '%d')"%(table, idName, idValue))
    return (cur.fetchone() is not None)
    

def delete_parking_from_db(idParking, cur):
    cur.execute("SELECT idTicket FROM Ticket WHERE(parking = '%d')"%(idParking))
    for row in cur.fetchall():
        cur.execute("DELETE FROM Transaction WHERE(ticket = '%d')"%(row[0]))
    cur.execute("DELETE FROM Ticket WHERE(parking = '%d')"%(idParking))
    cur.execute("DELETE FROM Reservation WHERE(parking = '%d')"%(idParking))
    cur.execute("DELETE FROM Place WHERE(parking = '%d')"%(idParking))
    cur.execute("DELETE FROM Parking WHERE(idParking = '%d')"%(idParking))
