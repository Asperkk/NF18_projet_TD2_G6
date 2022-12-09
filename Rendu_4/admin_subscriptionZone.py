#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: nf18p049
"""

def manage_subscriptions(cur):
    print("----Gestion des abonnements----")
    usr_input = -1
    while(usr_input != "0"):
        print("1 : Afficher les abonnements existants")
        print("2 : Ajouter un nouvel abonnement")
        print("3 : Supprimer un abonnement")
        print("0 : Quitter l'espace abonnement")
        usr_input = input("Votre choix : ")

        if(usr_input == "1"):
            sql = "SELECT * FROM abonnement"
            cur.execute(sql)
            donnee = cur.fetchall()
            for ligne in donnee:
                print("Abonnnement : %-10s\t Prix : %-3.2f\tType_véhicule : %s"%(ligne[0],ligne[1], ligne[2]))
        if(usr_input == "2"):
            sql = "SELECT * FROM abonnement"
            cur.execute(sql)
            donnee = cur.fetchall()
            existants = []
            for ligne in donnee:
                existants.append(ligne[0].lower())
            print(existants)
            Nabonnement = input("Veuillez saisir le nom du nouvel abonnement\n")
            while (Nabonnement.lower() in existants):
                Nabonnement = input("L'abonnement saisi existe déjà! Veuillez resaisir le nom du nouvel abonnement\n")
            Nprix = float(input("Veuillez saisir le prix de l'abonnement\n"))
            print("Indices de type de véhicules, 1 : camion  2 : 2_roues  3 : vehicule_simple\n")
            NtypeIndice = int(input("Veuillez saisir l'indice du type de véhicule de l'abonnement\n"))
            while NtypeIndice not in [1, 2, 3]:
                NtypeIndice = int(input("Erreur! Veuillez resaisir l'indice du type de véhicule de l'abonnement\n"))

            if NtypeIndice==1:
                Ntype = 'camion'
            elif NtypeIndice==2:
                Ntype = '2_roues'
            elif NtypeIndice==3:
                Ntype = 'vehicule_simple'

            sql = "INSERT INTO abonnement VALUES ('%s', '%.2f', '%s')"%(Nabonnement, Nprix, Ntype)
            cur.execute(sql)

        if(usr_input == "3"):
            sql = "SELECT a.nom FROM abonnement a LEFT JOIN (SELECT DISTINCT abonnement FROM souscription) s ON a.nom=s.abonnement WHERE s.abonnement IS NULL"
            cur.execute(sql)
            donnee = cur.fetchall()
            print("***Les abonnements qui ont des abonnés ne sont pas affichés!***\n")
            if donnee:
                print("Abonnements supprimables :\n")
                length = 0
                case = []
                for ligne in donnee:
                    length = length+1
                    case.append(length)
                    print("%-2d Abonnnement : %s"%(length, ligne[0]))
                NabonnementIndice = int(input("Veuillez saisir l'indice de l'abonnement à supprimer\n"))
                while NabonnementIndice not in case:
                    NabonnementIndice = int(input("Erreur! Veuillez resaisir l'indice de l'abonnement à supprimer\n"))
                if (input("Vous allez supprimer "+donnee[NabonnementIndice-1][0]+" , entrez y pour confirmer, autre touche pour annuler\n") == 'y'):
                    sql = "DELETE FROM abonnement WHERE nom='%s'"%(donnee[NabonnementIndice-1][0])
                    cur.execute(sql)
                else:
                    print("Suppression annulée\n")

            else:
                print("Il n'y pas d'abonnement supprimable!\n")

def manage_zones(cur):
    print("----Gestion des Zones----")
    usr_input = -1
    while(usr_input != "0"):
        print("1 : Afficher les zones existantes")
        print("2 : Ajouter une nouvelle zone")
        print("3 : Supprimer une zone")
        print("4 : Modifier le prix d'une zone")
        print("0 : Quitter l'espace zone")
        usr_input = input("Votre choix : ")

        if(usr_input == "1"):
            sql = "SELECT * FROM zone"
            cur.execute(sql)
            donnee = cur.fetchall()
            for ligne in donnee:
                print("Zone : %-20s\tPrix : %.2f"%(ligne[0],ligne[1]))

        if(usr_input == "2"):
            sql = "SELECT * FROM abonnement"
            cur.execute(sql)
            donnee = cur.fetchall()
            existants = []
            for ligne in donnee:
                existants.append(ligne[0].lower())
            Nzone = input("Veuillez saisir le nom de la nouvelle zone\n")
            while (Nzone.lower() in existants):
                Nzone = input("La zone saisie existe déjà! Veuillez resaisir le nom de la nouvelle zone\n")
            Nprix = float(input("Veuillez saisir le prix de l'abonnement\n"))
            sql = "INSERT INTO zone VALUES ('%s', '%.2f')"%(Nzone, Nprix)
            cur.execute(sql)

        if(usr_input == "3"):
            sql = "SELECT z.nom FROM zone z LEFT JOIN (SELECT DISTINCT zone FROM parking) p ON z.nom=p.zone WHERE p.zone IS NULL"
            cur.execute(sql)
            donnee = cur.fetchall()
            print("***Les zones qui sont associées des parkings ne sont pas affichées!***\n")
            if donnee:
                print("Zones supprimables :\n")
                length = 0
                case = []
                for ligne in donnee:
                    length = length+1
                    case.append(length)
                    print("%-2d Zone : %s"%(length, ligne[0]))
                NzoneIndice = int(input("Veuillez saisir l'indice de la zone à supprimer\n"))
                while NzoneIndice not in case:
                    NzoneIndice = int(input("Erreur! Veuillez resaisir l'indice de la zone à supprimer\n"))
                if (input("Vous allez supprimer "+donnee[NzoneIndice-1][0]+" , entrez y pour confirmer, autre touche pour annuler\n") == 'y'):
                    sql = "DELETE FROM zone WHERE nom='%s'"%(donnee[NzoneIndice-1][0])
                    cur.execute(sql)
                else:
                    print("Suppression annulée\n")

            else:
                print("Il n'y pas de zone supprimable!\n")

        if(usr_input == "4"):
            sql = "SELECT * FROM zone"
            cur.execute(sql)
            donnee = cur.fetchall()
            if donnee:
                print("Zones supprimables :\n")
                length = 0
                case = []
                for ligne in donnee:
                    length = length+1
                    case.append(length)
                    print("%-2d Zone : %-20s Prix : %.2f"%(length, ligne[0],ligne[1]))
                NzoneIndice = int(input("Veuillez saisir l'indice de la zone\n"))
                while NzoneIndice not in case:
                    NzoneIndice = int(input("Erreur! Veuillez resaisir l'indice de la zone %s\n"))%(donnee[NzoneIndice-1][0])

                Nprix = -1
                while Nprix<0:
                    Nprix = float(input("Veuillez saisir le nouveau prix de la zone\n"))
                if input("Zone : "+donnee[NzoneIndice-1][0]+", Ancien prix : "+str(donnee[NzoneIndice-1][1])+", nouveau prix : "+str(Nprix)+", entrez y pour confirmer, autre touche pour annuler\n"):
                    sql = "UPDATE zone SET prix='%.2f' WHERE nom='%s'"%(Nprix, donnee[NzoneIndice-1][0])
                    cur.execute(sql)
                else:
                    print("Modification annulée\n")

            else:
                print("Il n'y pas de zone existante!\n")



