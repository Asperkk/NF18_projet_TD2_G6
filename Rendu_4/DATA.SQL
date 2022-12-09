---Zone(#nom: varchar, prix: integer)


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

INSERT INTO Compte VALUES ('1','y.ouraq@etu.utc.fr','youraq','36','33 SQl 78');
INSERT INTO Compte VALUES ('2','n.yi@etu.utc.fr','nyi','3','38 EST DF');
INSERT INTO Compte VALUES ('3','a.saoud@etu.utc.fr','asaoud','0','10 TRO 36');
INSERT INTO Compte VALUES ('4','m.solan@etu.utc.fr','msolan','0','34 NUL AF');

--Transaction(ticket INTEGER PRIMARY KEY REFERENCES Ticket(idTicket), compte INTEGER REFERENCES Compte, moyen_paiement moyen_paiement_t NOT NULL, montant FLOAT)


INSERT INTO Transaction VALUES ('1', '2' ,'carte','7.50','guichet');
INSERT INTO Transaction VALUES ('2', '3','especes','4.25','automate');
INSERT INTO Transaction VALUES ('3', '3','carte','2.39','automate');
INSERT INTO Transaction VALUES ('4', '4','carte','5.00','automate');
INSERT INTO Transaction VALUES ('5', NULL,'carte','5.00','automate');
--Le prix a été ici mis arbitraiment il sera calculé en fonction du prix de la zone et de la durée du ticket

--CREATE TABLE Occasionnel(compte INTEGER PRIMARY KEY REFERENCES Compte(idCompte));



--Abonnement(#nom: varchar, prix: float, type_vehicule: enumerate{camion, 2_roues, vehicule_simple})
INSERT INTO Abonnement VALUES('Camion','79.99','camion');
INSERT INTO Abonnement VALUES('2_roues','19.99','2_roues');
INSERT INTO Abonnement VALUES('vehicule_simple','39.99','vehicule_simple');





--CREATE TABLE Abonne(compte INTEGER PRIMARY KEY REFERENCES Compte(idCompte), nom VARCHAR NOT NULL, prenom VARCHAR NOT NULL);

INSERT INTO Abonne VALUES('1','OURAQ','yassine');
INSERT INTO Abonne VALUES('2','YI','nicolas');
INSERT INTO Abonne VALUES('3','SAOUD','adel');
INSERT INTO Abonne VALUES('4','SOLAN','matthieu');

--CREATE TABLE Souscription(abonnement REFERENCES Abonnement(nom), abonne  REFERENCES Abonne(compte), date_debut;

INSERT INTO Souscription VALUES('Camion','3','2021-08-03');
INSERT INTO Souscription VALUES('2_roues','2','2021-08-01');
INSERT INTO Souscription VALUES('vehicule_simple','1','2021-08-07');
INSERT INTO Souscription VALUES('2_roues','3','2021-08-03');
INSERT INTO Souscription VALUES('vehicule_simple','4','2021-07-01');  -- cet ancien abonne est devenu un occasionnel sa soucription a expire


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
