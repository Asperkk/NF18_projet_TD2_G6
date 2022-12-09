#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  3 10:25:28 2022

@author: nf18p046
"""


import psycopg2
import admin, user

def connect_db():
    conn = psycopg2.connect(
            host="tuxa.sme.utc",
            database="*******",
            user="*******",
            password="******")
    return conn
conn = connect_db()
cur = conn.cursor()


usr_input = -1
print("**************PARKING DATABASE**************")
while(usr_input != "0"):
    print("0 : quitter le programme")
    print("1 : Mode administrateur")
    print("2 : Mode utilisateur")
    print("3 : Sauvegarder les changements")
    usr_input = input("Votre choix : ")
    if(usr_input == "3"):
        conn.commit()
        print("Changements enregistrés !\n")
    elif(usr_input != "0"):
        if(usr_input == "1"):
            mdp = input("Entrez le mot de passe administrateur :")
            if(mdp == "admin"):
                admin.display_admin_space(cur)
        else:
            print("------Mode Utilisateur-------")
            print("1 : se connecter")
            print("2 : créer un compte")
            print("entrez n'importe quelle autre touche pour quitter")
            usr_input = input("Votre choix : ")
            user.connect_user(usr_input, cur)
            
     
conn.commit()
conn.close()
