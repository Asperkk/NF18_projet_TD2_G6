
import user

def manage_place(cur):
    print("\n---------Gestion des Places--------")
    usr_input = -1
    while(usr_input != "0"):
        print("1 : Ajouter un place")
        print("2 : Supprimer un place")
        print("3 : Afficher les place libres")
        print("0 : Retourner vers la page précédente")

        usr_input = input("Votre choix : ")
        
        if usr_input == "1":
            ajoute_place(cur)

        if usr_input == "2":
            supprime_place(cur)

        if usr_input == "3":
            afficher_libre(cur)



def ajoute_place(cur):
    cur.execute("SELECT idparking FROM parking")
    res = cur.fetchone()
    tabres = []
    while res:
        tabres.append(res[0])
        res = cur.fetchone()
    print("parking: ",tabres)
    parking = input("parking choix: ")
    add_place_db(parking, cur)
    


def supprime_place(cur):
    parking = input("parking choix: ")
    delete_place_db(parking, cur)
def est_libre(cur):
    pass

def afficher_places(parking, cur):
    sqllib = "SELECT * FROM place WHERE (parking = '%d' )"%(parking)
    cur.execute(sqllib)
    res = cur.fetchone()
    while res:
        print("num: ",res[0],"  parking: ",res[1]," type_vehicule: ", res[2],"  type_place: ",res[3])
        res = cur.fetchone()

def afficher_libre(cur):
    horaire_consulter = input("Début de l'horaire a consulter: (format YY-MM-DD hh-mm-ss)")
    duree = input("Durée : ")
    sqlview = """CREATE VIEW res_conflit AS 
    SELECT numplace,parking,horaire 
    FROM reservation WHERE horaire >= timestamp'{}' AND horaire<=timestamp '{}' + interval '{} hours' """.format(horaire_consulter, horaire_consulter, duree)
    cur.execute(sqlview)
    sqlclt = """
    SELECT * FROM res_conflit as r  
    RIGHT JOIN place as p 
    ON r.numplace=p.num AND r.parking=p.parking  
    WHERE r.horaire IS NULL 
    """
    cur.execute(sqlclt)
    print("\nPlaces libres  : \n")
    res = cur.fetchall()
    for index,row in enumerate(res):
        if index == 0:
            print("num place: ",row[3],"    parking: ",row[4])
        if index > 0 and (row[5]!=res[index-1][6] or row[6]!=res[index-1][6]):
            print("num place: ",row[3],"    parking: ",row[4])
    cur.execute("DROP VIEW res_conflit")
    
    
    
def add_place_db(idParking, cur):
    num = user.generate_id('num', 'Place', cur)
    print("\nCréation Place %d : "%(num))
    type_vehicule = input("type_vehicule {vehicule_simple, camion 2_roues} : ")
    type_place = input("type_place {couverte, plein_air }: ")
    sqlajt = "INSERT INTO place VALUES({},{},'{}','{}')".format(num,idParking ,type_vehicule,type_place)
    cur.execute(sqlajt)
    
def delete_place_db(idParking, cur):  
    print("\nListe des places :")
    afficher_places(idParking, cur)
    num = int(input("num choix: "))
    cur.execute("DELETE FROM Reservation WHERE(parking = '%d' AND numPlace = '%d')"%(idParking, num))
    sqlsup = "DELETE FROM place WHERE parking={} AND num={}".format(idParking,num)
    cur.execute(sqlsup)
    
