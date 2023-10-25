from suds.client import Client
import tkinter as tk


# Saisie des informations du client
nom = input("Nom : ")
prenom = input("prénom: ")
ville = input("Ville: ")
email = input("Email: ")
type = input("appartement ou maison: ")
nombre_piece= input("nombre de piece: ")
montant = input("Montant: ")
revenu = input("Revenu: ")
depenses = input("Dépenses: ")


recevoirDemandeService_client = Client('http://localhost:8000/ReceptionDemandeService?wsdl')

result = recevoirDemandeService_client.service.recevoir_demande(
    nom, prenom, ville, email,type, montant,nombre_piece, revenu, depenses
)


