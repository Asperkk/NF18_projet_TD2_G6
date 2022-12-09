--nbre de personnes actuellement sur le parking 1 :
SELECT COUNT(idTicket) FROM Parking, Ticket WHERE ((Ticket.parking = Parking.idParking AND parking = 1 )AND Ticket.horaire_sortie IS NULL);

--nbre de reservations du parking 4 :
SELECT COUNT(idRes) FROM Reservation, Place WHERE (Reservation.numPlace = Place.num AND Place.parking = Reservation.parking AND Place.parking = 4);

--liste des abonnés :
SELECT * FROM Abonne;

--liste des abonnements de SAOUD adel :
SELECT Abonnement.nom FROM Souscription, Abonnement, Abonne WHERE(Souscription.abonnement = Abonnement.nom AND Souscription.abonne = Abonne.compte AND Abonne.nom = 'SAOUD' AND Abonne.prenom = 'adel');

--liste des réservations de OURAQ yassine

SELECT Reservation.horaire, Reservation.numPlace, Reservation.parking FROM Reservation, Abonne WHERE(Reservation.compte = Abonne.compte AND Abonne.nom = 'SAOUD' AND Abonne.prenom = 'adel');


--Prix des parkings du centre-ville :
SELECT Parking.idParking, Zone.prix FROM Parking, Zone WHERE (Parking.zone = Zone.nom AND Zone.nom = 'Centre-ville');

--Liste des places couvertes dans la ZAC :
SELECT Place.num, Place.parking FROM Zone, Parking, Place WHERE (Place.parking = Parking.idParking AND Zone.nom = Parking.zone AND Place.parking = Parking.idParking AND Zone.nom = 'ZAC' AND Place.type_place = 'couverte');

DROP VIEW IF EXISTS AbonnementAbonne, ComptePlace;
--Vue Abonnements :
CREATE VIEW AbonnementAbonne AS (SELECT Abonnement.nom, Abonne.compte FROM Abonnement, Souscription, Abonne WHERE (Abonne.compte = Souscription.abonne AND Abonnement.nom = Souscription.abonnement));
--Vue réservation :
CREATE VIEW ComptePlace AS (SELECT Place.num, Place.type_place, Compte.idCompte, Compte.email, Reservation.horaire FROM Compte, Place, Reservation WHERE (Place.num = Reservation.numPlace AND Reservation.compte = Compte.idCompte));



