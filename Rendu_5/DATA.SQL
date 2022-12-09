--Zone(#nom: varchar, prix: integer)


INSERT INTO Zone VALUES ('Centre-ville','5.5');
INSERT INTO Zone VALUES ('ZAC','2');  --ZAC= ZONE D ACTIVITE COMMERCIALLES
INSERT INTO Zone VALUES ('Zone_industrielle','1.5');
INSERT INTO Zone VALUES ('Hors_centre','4');


-- Parking(#idParking: integer,nb_places: integer, nb_personnes: integer, zone => Zone)


INSERT INTO Parking VALUES ('1','2','0','Centre-ville');
INSERT INTO Parking VALUES ('2','1','1','Centre-ville');
INSERT INTO Parking VALUES ('3','1','1','Zone_industrielle');
INSERT INTO Parking VALUES ('4','2','0','ZAC');
INSERT INTO Parking VALUES ('5','1','0','Zone_industrielle');
INSERT INTO Parking VALUES ('6','2','2','ZAC');
INSERT INTO Parking VALUES ('7','1','1','Hors_centre');



--Ticket


INSERT INTO Ticket VALUES ('1','2021-08-31 09:53:58','2021-09-01 08:00:15','2_roues','1');
INSERT INTO Ticket VALUES ('2','2021-08-31 17:40:01','2021-08-31 23:58:36','camion','2');
INSERT INTO Ticket VALUES ('3','2021-09-01 12:45:36','2021-09-01 18:36:00','2_roues','6');
INSERT INTO Ticket VALUES ('4','2021-09-01 07:15:00','2021-09-01 18:37:00','vehicule_simple','6');
INSERT INTO Ticket VALUES ('5','2021-09-01 07:15:00',NULL,'vehicule_simple','1');
--Compte(e-mail,mot-de-passe,point fidelité,immatriculation)

INSERT INTO Compte VALUES (
'1',
'y.ouraq@etu.utc.fr',
'youraq',
'36',
'33 SQl 78',
'
{
	"nom" : "OURAQ",
	"prenom" : "yassine",
	"type_utilisateur" : "abonne",
	"abonnement" :
		[
			{
				"nom" : "vehicule_simple", 
				"prix" : 39.99,
				"type_vehicule" : "vehicule_simple",
				"date_debut" : "2021-08-07"
			}			
		]
}
'
);
INSERT INTO Compte VALUES (
'2',
'n.yi@etu.utc.fr',
'nyi',
'3',
'38 EST DF',
'
{
	"nom" : "YI",
	"prenom" : "nicolas",
	"type_utilisateur" : "abonne",
	"abonnement" :
		[
			{
				"nom" : "2_roues", 
				"prix" : 19.99,
				"type_vehicule" : "2_roues",
				"date_debut" : "2021-08-01"
			}		
		]
}
'
);

INSERT INTO Compte VALUES (
'3',
'a.saoud@etu.utc.fr',
'asaoud',
'0',
'10 TRO 36',
'
{
	"nom" : "SAOUD",
	"prenom" : "adel",
	"type_utilisateur" : "abonne",
	"abonnement" :
		[
			{
				"nom" : "2_roues", 
				"prix" : 19.99,
				"type_vehicule" : "2_roues",
				"date_debut" : "2021-08-03"
			},
			{
				"nom" : "Camion", 
				"prix" : 79.99,
				"type_vehicule" : "Camion",
				"date_debut" : "2021-08-01"
			}	
		]
}
'
);

INSERT INTO Compte VALUES ('4',
'm.solan@etu.utc.fr',
'msolan',
'0','
34 NUL AF',
'{
	"nom" : "SOLAN",
	"prenom" : "matthieu",
	"type_utilisateur" : "occas"
}'
);

--Transaction(ticket INTEGER PRIMARY KEY REFERENCES Ticket(idTicket), compte INTEGER REFERENCES Compte, moyen_paiement moyen_paiement_t NOT NULL, montant FLOAT)


INSERT INTO Transaction VALUES ('1', '2' ,'carte','7.50','guichet');
INSERT INTO Transaction VALUES ('2', '3','especes','4.25','automate');
INSERT INTO Transaction VALUES ('3', '3','carte','2.39','automate');
INSERT INTO Transaction VALUES ('4', '4','carte','5.00','automate');
INSERT INTO Transaction VALUES ('5', NULL,'carte','5.00','automate');
--Le prix a été ici mis arbitraiment il sera calculé en fonction du prix de la zone et de la durée du ticket

--Place(#num: integer, #parking => idParking, type_place: enumerate{camion, 2_roues, vehicule_simple},type_place)

INSERT INTO Place VALUES ('3','1','2_roues','couverte');
INSERT INTO Place VALUES ('3','3','vehicule_simple','couverte');
INSERT INTO Place VALUES ('3','5','vehicule_simple','couverte');
INSERT INTO Place VALUES ('3','2','camion','plein_air');
INSERT INTO Place VALUES ('26','1','camion','plein_air');
INSERT INTO Place VALUES ('36','4','camion','plein_air');
INSERT INTO Place VALUES ('149','6','2_roues','couverte');
INSERT INTO Place VALUES ('50','7','2_roues','couverte');
INSERT INTO Place VALUES ('250','6','vehicule_simple','couverte');

--Reservation(idRes ,compte associe a la reservation, numPlace , parking , horaire TIMESTAMP , FOREIGN KEY(numPlace, parking) REFERENCES Place(num, parking));


INSERT INTO Reservation VALUES('1','1','26','1','2021-09-03 07:15:00');
INSERT INTO Reservation VALUES('2','2','36','4','2021-09-03 07:00:00');
INSERT INTO Reservation VALUES('3','3','50','7','2021-09-04 10:00:00');



