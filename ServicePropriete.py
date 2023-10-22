import json
import sys
from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.util.wsgi_wrapper import run_twisted
from suds.client import Client


class ServicePropriete(ServiceBase):
    @rpc( Unicode, Unicode,Unicode,float, _returns=bool)
    def proprieteClient(ctx, nb_piece, superficie, adresse,montant):
        try:
            with open("ventes_recentes.json", "r") as f:
                data = json.load(f)
                print(data)
                print(nb_piece,adresse,montant)
            if data:
                for vente in data:
                    if vente["Adresse"] == adresse and vente["nombre_piece"] == int(nb_piece):
                        prix = float(vente.get("prix"))
                        print(prix)
                        if montant <= prix :
                            return True
                        elif montant > prix :
                            return False
                    else :
                        print("aucun match")    

            else:
                return "Aucune ventes recentes à proximité de cette adresse"
            
        except (json.JSONDecodeError, FileNotFoundError) as e:
            return f"Erreur lors de la lecture du fichier : {str(e)}"
    
application = Application([ServicePropriete],
                          tns='spyne.examples.propriete',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11()
                          )
if __name__ == '__main__':
    wsgi_app = WsgiApplication(application)
    twisted_apps = [
        (wsgi_app, b'ServicePropriete'),
    ]
    sys.exit(run_twisted(twisted_apps, 8004))