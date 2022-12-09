#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  3 10:31:54 2022

@author: nf18p046
"""

import user_reservation, user_subscription

def check_account_exist(login, cur):
    cur.execute("SELECT * FROM Compte WHERE (email = '%s')"%(login))
    return (cur.fetchone() is None)

def generate_id(idName ,tablename, cur):
    cur.execute("SELECT MAX(%s) FROM %s"%(idName, tablename))
    result = cur.fetchone()
    if( result is None):
        return 1
    else:
        return (int(result[0]) + 1)


def connect_user(choix, cur):
    if(choix == "1"):
        print("----Connection----")
        login = input("Entrez votre adresse mail : ")        
        if(check_account_exist(login, cur)):
            print("Ce compte n'existe pas !")
            return
        else:
            password = input("Entrez votre mot de passe : ")
            cur.execute("SELECT * FROM Compte WHERE (mot_de_passe = '%s' AND email = '%s')"\
                        %(password, login))
            result = cur.fetchone() 
            if(result is None):
                print("Le mot de passe est incorrect !")
                return
            else:
                userId = result[0]
                display_user_space(cur, userId, login)
            
    if(choix == "2"):
        print("-----Création d'un compte-----")
        login = input("Entrez une adresse mail : ")
        if(check_account_exist(login, cur)):
            password = input("Entrez un mot de passe : ")
            immat = input("Entrez l'immatriculation de votre véhicule principal : ")
            if(len(immat) != 9):
                print("L'immatriculation saisie est invalide !")
                return
            else:
                 userId = generate_id('idCompte', 'Compte', cur)
                 cur.execute("INSERT INTO Compte VALUES('%s', '%s', '%s', '0', '%s')"\
                        %(userId, login, password, immat))
                 cur.execute("INSERT INTO Occasionnel VALUES('%s')"\
                        %(userId))
                 display_user_space(cur, userId, login)

        else:
            print("Ce compte existe deja !")
            return
                
def display_user_space(cur, userId, login):
    print("------- Espace Utilisateur de "+ login + " -------")
    usr_input = -1
    while(usr_input != "0"):
        print("1 : Gérer mes réservations")
        print("2 : Gérer mes abonnements")
        print("3 : Modifier mon compte")
        print("4 : Afficher mes transactions")
        print("5 : Afficher mes informations")
        print("0 : Quitter mon espace utilisateur")
        usr_input = input("Votre choix : ")
        
        if(usr_input == "1"):
            user_reservation.manage_reservations(cur, userId)
            
        elif(usr_input == "2"):
            user_subscription.manage_subscriptions(cur, userId)  
            
        elif(usr_input == "3"):
            update_account(cur, userId, login)  
            
        elif(usr_input == "4"):
            display_transactions(cur, userId)  
        elif(usr_input == "5"):
            display_information(cur, userId)
            
            
            
def manage_reservations(cur, userId):
    print("gestion des reservations")

    
def manage_subscriptions(cur, userId):
    print("gestion des abonnements")

    
def update_account(cur, userId,email):
    print("------Espace Modification de "+ email +" ------")
    usr_input=-1
    while(usr_input!="0"):
        print("1: Modifier mon email")
        print("2: Modifier mon mot de passe")
        print("3: Changer mon immatriculation")
        print("0: Quitter l'Espace Modification")
        usr_input=input("Votre choix:")

        if (usr_input=='1'):
            n=input('Entrez un nouvel email:')
            if (check_account_exist(n, cur) == False):
                print('le compte existe déjà')
                return
            else:
                sql=("UPDATE Compte SET email='%s' WHERE idCompte='%s'"%(n,userId))
                cur.execute(sql)
                print('ID du compte est:' + str(userId) + 'le nouvel email est:' + n)
                email = n

        elif (usr_input=='2'):
            n=input("entrez un nouveau mdp:")
            sql=("UPDATE Compte SET mot_de_passe='%s' WHERE idCompte='%s'"%(n,userId))
            cur.execute(sql)
            print('ID du compte est:' + str(userId)  + ' le nouveau mot de passe  est:' + n)

        elif (usr_input=='3'):
            n=input('La nouvelle immatriculation est : ')
            if(len(n) != 9):
                print("Immatriculation incorrecte !")
                return
            sql=("UPDATE Compte SET immat='%s'WHERE idCompte='%s'"%(n,userId))
            cur.execute(sql)
            print('ID du compte est: ' + str(userId) + ' la nouvelle immatriculation est: ' + n)

        elif (usr_input == '0'):
            display_transactions(cur,userId)
    




    
def display_transactions(cur, userId):
    sql=("SELECT * FROM Transaction WHERE compte='%s'"%(userId) )
    cur.execute(sql)
    ligne= cur.fetchone()
    if(ligne is None):
        print('Pas de transactions à afficher !')
        return
    while ligne:
        print('Identifiant du ticket: '+ str(ligne[0]) +' payé par: '+ligne[2]+' le prix étant de : '+ str(ligne[3])+ ' sur: '+ligne[4] )
        ligne=cur.fetchone()

def display_information(cur, userId):
    print("------Mes Informations-------")
    cur.execute("SELECT nom, prenom FROM Abonne WHERE(compte = '%d');"%(userId))
    identite = cur.fetchone()
    cur.execute("SELECT * FROM Compte WHERE(idCompte = '%d')"%(userId))
    compte = cur.fetchone()
    print("Vos informations :")
    if(identite is not None):
        print("Nom : %s, Prenom : %s"%(identite[0], identite[1]))
    print("Email : %s, Immatriculation : %s, Points : %d"%(compte[1] ,compte[4], compte[3]))
    
    
