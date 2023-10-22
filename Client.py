from suds.client import Client

# Saisie des informations du client
nom = input("Nom : ")
prenom = input("prénom: ")
adresse = input("Adresse: ")
email = input("Email: ")
montant = input("Montant: ")
nombre_piece= input("nombre de piece: ")
superfecie = input("superficie : ")
revenu = input("Revenu: ")
depenses = input("Dépenses: ")


recevoirDemandeService_client = Client('http://localhost:8000/ReceptionDemandeService?wsdl')


result = recevoirDemandeService_client.service.recevoir_demande(
    nom, prenom, adresse, email, montant,nombre_piece, superfecie, revenu, depenses
)


print(result)
