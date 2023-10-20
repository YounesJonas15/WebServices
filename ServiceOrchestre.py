import json
import sys
from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.util.wsgi_wrapper import run_twisted

class ServiceOrchestration(ServiceBase):
    @rpc(_returns=str)
    def Extraction_nom_client(ctx):
        try:
            # Lire les données depuis le fichier JSON
            with open("demandes.json", "r") as f:
                data = json.load(f)

            # Vérifier s'il y a des demandes dans le fichier
            if data:
                # Récupérer la dernière demande
                last_demande = data[-1] 
                print(last_demande) 
                return "Dernière demande lue avec succès depuis le fichier JSON."
            else:
                return "Aucune demande trouvée dans le fichier JSON."

        except (json.JSONDecodeError, FileNotFoundError) as e:
            return f"Erreur lors de la lecture du fichier : {str(e)}"
        
        
    
application = Application([ServiceOrchestration],
                          tns='spyne.examples.orchestration',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11()
                          )

if __name__ == '__main__':
    wsgi_app = WsgiApplication(application)
    twisted_apps = [
        (wsgi_app, b'ServiceOrchestration'),
    ]
    sys.exit(run_twisted(twisted_apps, 8001))
