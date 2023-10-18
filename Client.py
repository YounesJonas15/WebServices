from suds.client import Client

# Saisie des informations du client
nom_client = input("Nom du Client: ")
adresse = input("Adresse: ")
email = input("Email: ")
# Créez un client Suds pour le service web
recevoirDemandeService_client = Client('http://localhost:8000/ReceptionDemandeService?wsdl')


# Appelez l'opération recevoir_demande avec les données du client
result = recevoirDemandeService_client.service.recevoir_demande(
    nom_client, adresse, email
)

# Affichez la réponse du service
print(result)
