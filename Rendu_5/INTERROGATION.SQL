DROP VIEW IF EXISTS AbonnementAbonne, ComptePlace, TransactionCompte, TransactionDate, Abonne, Occasionnel;

--Vue Abonnes:
CREATE VIEW Abonne AS (
	SELECT Compte.utilisateur->>'nom' AS nom, Compte.utilisateur->>'prenom' AS prenom, Compte.idCompte
	FROM Compte
	WHERE (utilisateur->>'type_utilisateur' = 'abonne')

);

--Vue Occasionnels:
CREATE VIEW Occasionnel AS (
	SELECT Compte.utilisateur->>'nom' AS nom, Compte.utilisateur->>'prenom' AS prenom
	FROM Compte
	WHERE (utilisateur->>'type_utilisateur' = 'occas')

);


--Vue Abonnements :
CREATE VIEW AbonnementAbonne AS (
	SELECT Compte.utilisateur->>'nom' AS nom,
	Compte.utilisateur->>'prenom' AS prenom,
	Compte.idCompte, 
	a->>'nom' AS abonnement,
	CAST(a->>'prix' AS FLOAT) AS cout,
	a->>'type_vehicule' AS type_vehicule,
	a->>'date_debut' AS date_debut
	FROM Compte, JSON_ARRAY_ELEMENTS(utilisateur->'abonnement') AS a
);


--Vue réservation :
CREATE VIEW ComptePlace AS (SELECT Place.num, Place.parking, Place.type_place, Compte.idCompte, Compte.email, Reservation.horaire FROM Compte, Place, Reservation WHERE (Place.num = Reservation.numPlace AND Reservation.compte = Compte.idCompte AND Place.parking = Reservation.parking) );

--Vues transaction :
CREATE VIEW TransactionCompte AS (SELECT ticket, moyen_paiement, montant, pt_de_vente, email FROM Transaction LEFT JOIN Compte ON Transaction.compte = Compte.idCompte);

CREATE VIEW TransactionDate AS (SELECT * FROM TransactionCompte LEFT JOIN Ticket ON ticket=idticket);


--nbre de personnes actuellement sur le parking 1 :
SELECT COUNT(idTicket) FROM Parking, Ticket WHERE ((Ticket.parking = Parking.idParking AND parking = 1 )AND Ticket.horaire_sortie IS NULL);

--nbre de reservations du parking 4 :
SELECT COUNT(idRes) FROM Reservation, Place WHERE (Reservation.numPlace = Place.num AND Place.parking = Reservation.parking AND Place.parking = 4);

--liste des Comptes :
SELECT * FROM Compte;

--liste des abonnements de SAOUD adel :
SELECT a.nom, a.prenom, a.abonnement FROM AbonnementAbonne AS a WHERE(a.nom = 'SAOUD' AND a.prenom = 'adel');


--liste des réservations de l'abonné SAOUD adel

SELECT nom, prenom, Reservation.horaire, Reservation.numPlace, Reservation.parking FROM Reservation, Compte, Abonne WHERE(Reservation.compte = Compte.idCompte AND Abonne.nom = 'SAOUD' AND Abonne.prenom = 'adel');


--Prix des parkings du centre-ville :
SELECT Parking.idParking, Zone.prix FROM Parking, Zone WHERE (Parking.zone = Zone.nom AND Zone.nom = 'Centre-ville');

--Liste des places couvertes dans la ZAC :
SELECT Place.num, Place.parking FROM Zone, Parking, Place WHERE (Place.parking = Parking.idParking AND Zone.nom = Parking.zone AND Place.parking = Parking.idParking AND Zone.nom = 'ZAC' AND Place.type_place = 'couverte');

SELECT * FROM Abonne;
SELECT * FROM Occasionnel;
SELECT * FROM AbonnementAbonne;

--Cout total des abonnements de SAOUD ADEL
SELECT idCompte, SUM(a.cout) AS cout_total FROM AbonnementAbonne AS a WHERE(a.nom = 'SAOUD' AND a.prenom = 'adel') GROUP BY idCompte;
