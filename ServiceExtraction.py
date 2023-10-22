import json
import sys
from spyne import Application, rpc, ServiceBase, Unicode, Array, Float
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.util.wsgi_wrapper import run_twisted
from suds.client import Client

class ServiceExtraction(ServiceBase):
    @rpc(_returns=Array(Float))
    def Extraction_donne_client(ctx):
        try:
            # Lire les données depuis le fichier JSON
            with open("demandes.json", "r") as f:
                data = json.load(f)

            # Vérifier s'il y a des demandes dans le fichier
            if data:
                # Récupérer la dernière demande
                last_demande = data[-1] 
                print(last_demande) 
                solvabilite_calcul = Client('http://localhost:8003/ServiceSolvabilite?wsdl')
                solvabilite_score = solvabilite_calcul.service.solvabiliteClient(last_demande['Nom du Client'],last_demande['Prenom du Client'], last_demande['Email'] )
                print(solvabilite_score)
                propriete_calcul = Client('http://localhost:8004/ServicePropriete?wsdl')
                propriete_score = propriete_calcul.service.proprieteClient()
                print(propriete_score)
                score = []
                score.append(solvabilite_score)
                score.append(propriete_score)
                return score
            else:
                return "Aucune demande trouvée dans le fichier JSON."
        except (json.JSONDecodeError, FileNotFoundError) as e:
            return f"Erreur lors de la lecture du fichier : {str(e)}"
        
         

application = Application([ServiceExtraction],
                          tns='spyne.examples.extraction',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11()
                          )


if __name__ == '__main__':
    wsgi_app = WsgiApplication(application)
    twisted_apps = [
        (wsgi_app, b'ServiceExtractionClient'),
    ]
    sys.exit(run_twisted(twisted_apps, 8002))

















# Ouvrir le fichier JSON
#with open('demande.json', 'r') as json_file:
 #   data = json.load(json_file)
    
#print(data)
