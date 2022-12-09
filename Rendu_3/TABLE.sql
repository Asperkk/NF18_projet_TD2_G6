DROP TABLE IF EXISTS Transaction, Zone, Parking, Ticket, Compte, Occasionnel, Abonnement, Abonne, Souscription, Place, Reservation;

DROP TYPE IF EXISTS pt_de_vente_t, vehicule_t, moyen_paiement_t, type_place_t;

CREATE TYPE pt_de_vente_t AS ENUM ('automate', 'guichet');
CREATE TYPE vehicule_t AS ENUM ('camion', '2_roues', 'vehicule_simple');
CREATE TYPE moyen_paiement_t AS ENUM ('carte','especes');
CREATE TYPE type_place_t AS ENUM ('couverte','plein_air');

CREATE TABLE Zone(nom VARCHAR PRIMARY KEY, prix FLOAT, CHECK(prix > 0));

CREATE TABLE Parking(idParking INTEGER PRIMARY KEY, nb_places INTEGER, nb_personnes INTEGER, zone VARCHAR REFERENCES Zone(nom) NOT NULL, CHECK((nb_personnes >= 0 AND nb_places > 0) AND nb_personnes <= nb_places));

CREATE TABLE Ticket(idTicket INTEGER PRIMARY KEY, horaire_entree TIMESTAMP NOT NULL, horaire_sortie TIMESTAMP,  type_vehicule vehicule_t NOT NULL, parking INTEGER REFERENCES Parking(idParking) NOT NULL, CHECK((horaire_sortie IS NULL) OR (horaire_sortie > horaire_entree) ));

CREATE TABLE Compte(idCompte INTEGER PRIMARY KEY, email VARCHAR UNIQUE NOT NULL, mot_de_passe VARCHAR NOT NULL, pts_de_fidelite INTEGER, immat VARCHAR NOT NULL,CHECK(pts_de_fidelite >= 0));

CREATE TABLE Transaction(ticket INTEGER PRIMARY KEY REFERENCES Ticket(idTicket), compte INTEGER REFERENCES Compte(idCompte), moyen_paiement moyen_paiement_t NOT NULL, montant FLOAT, CHECK (montant >= 0),  pt_de_vente pt_de_vente_t NOT NULL);

CREATE TABLE Occasionnel(compte INTEGER PRIMARY KEY REFERENCES Compte(idCompte));

CREATE TABLE Abonnement(nom VARCHAR PRIMARY KEY, prix FLOAT, type_vehicule vehicule_t NOT NULL, CHECK(prix > 0));

CREATE TABLE Abonne(compte INTEGER PRIMARY KEY REFERENCES Compte(idCompte), nom VARCHAR NOT NULL, prenom VARCHAR NOT NULL);

CREATE TABLE Souscription(abonnement VARCHAR REFERENCES Abonnement(nom), abonne INTEGER REFERENCES Abonne(compte), date_debut DATE NOT NULL, PRIMARY KEY(abonnement, abonne));

CREATE TABLE Place(num INTEGER, parking INTEGER REFERENCES Parking(idParking), type_vehicule vehicule_t NOT NULL,type_place type_place_t NOT NULL, PRIMARY KEY(num, parking));

CREATE TABLE Reservation(idRes INTEGER PRIMARY KEY, compte INTEGER REFERENCES Compte(idCompte) NOT NULL, numPlace INTEGER NOT NULL, parking INTEGER NOT NULL, horaire TIMESTAMP NOT NULL, FOREIGN KEY(numPlace, parking) REFERENCES Place(num, parking));




