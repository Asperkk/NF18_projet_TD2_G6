

def has_subscription(cur, userId):
    cur.execute("SELECT compte FROM AbonnementAbonne WHERE (compte = '%d')"%(userId));
    res = cur.fetchone()
    cur.fetchall()
    return(res is not None)


def manage_subscriptions(cur, userId):
    print("----Gestion des abonnements----")
    usr_input = -1
    while(usr_input != "0"):
        print("1 : Afficher tous mes abonnements")
        print("2 : Ajouter un nouvel abonnement")
        print("3 : Résilier un abonnement")
        print("0 : Quitter mon espace utilisateur")
        usr_input = input("Votre choix : ")

        if(usr_input == "1"):
            sql = "SELECT * FROM souscription where abonne=%d"%(userId)
            cur.execute(sql)
            donnee = cur.fetchall()
            for ligne in donnee:
                print("\tAbonnnement : %s, Date de début : %s"%(ligne[0],ligne[2]))
        if(usr_input == "2"):
            sql = "SELECT a.nom FROM abonnement a LEFT JOIN (SELECT * FROM souscription where abonne=%d) s ON a.nom=s.abonnement where abonnement IS NULL"%(userId)
            cur.execute(sql)
            donnee = cur.fetchall()
            if donnee:
                indice = 0
                for ligne in donnee:
                    indice = indice+1
                    print("\t%d Abonnnements disponibles: %s"%(indice, ligne[0]))
                choix = int(input("veuillez saisir l'indice de l'abonnement que vous voulez\n"))

                while (1>choix or choix>indice):
                     choix = int(input("veuillez resaisir l'indice de l'abonnement que vous voulez\n"))
                     print(choix)
                if(has_subscription(cur, userId) == False):
                    nom = input("Entrez votre nom : ")
                    prenom = input("Entrez votre prénom : ")
                    cur.execute("INSERT INTO Abonne VALUES ('%d', '%s', '%s')"%(userId, nom, prenom))
                    cur.execute("DELETE FROM Occasionnel WHERE (compte = '%d')"%(userId))
                sql = "INSERT INTO Souscription VALUES('%s','%d','2022-05-03')"%(donnee[indice-1][0],userId)
                cur.execute(sql)
            else:
                print("Aucun abonnement disponible\n")
        if(usr_input == "3"):
            sql = "SELECT * FROM souscription where abonne=%d"%(userId)
            cur.execute(sql)
            donnee = cur.fetchall()
            indice = 0
            for ligne in donnee:
                indice = indice+1
                print("\t%d Votre abonnement: %s"%(indice, ligne[0]))

            choix = int(input("Veuillez saisir l'indice de l'abonnement que vous voulez résilier\n"))
            while (1>choix or choix>indice):
                 choix = int(input("Veuillez resaisir l'indice de l'abonnement que vous voulez résilier\n"))
                 print(choix)
            confirm = input("L'abonnnement choisi: %s, êtes vous êtes sûr de vouloir le résiler? Si oui taper y, sinon n\n"%(donnee[indice-1][0]))
            if confirm=='y':
                sql = "DELETE FROM souscription WHERE abonnement='%s' AND abonne=%d"%(donnee[indice-1][0],userId)
                cur.execute(sql)
                print("Succès !")
            if(has_subscription(cur, userId) == False):
                    cur.execute("INSERT INTO Occasionnel VALUES ('%d')"%(userId))
                    cur.execute("DELETE FROM Abonne WHERE (compte = '%d')"%(userId))
              

