import json
import sys
from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.util.wsgi_wrapper import run_twisted
from suds.client import Client


class ServiceSolvabilite(ServiceBase):
    @rpc( Unicode, Unicode, Unicode,Unicode,Unicode,Unicode, _returns=float)
    def solvabiliteClient(ctx, nom, prénom, email, montant, revenu, depenses):
        list_client = []
        result_tuple = {}
        try:
            with open("banque.json", "r") as f:
                list_client = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            pass

        
        dettes = 0  

        for client in list_client:
            if client["Email"] == email:
                # Récupérer le tuple (nom, prénom, email) correspondant
                result_tuple = client
                dettes = sum(result_tuple["Dete"])
                break

        # Si le client n'est pas trouvé, retourner -1, sinon effectuer le calcul et retourner le résultat
        if dettes == 0:
            return -1
        else:
            return (float(montant) + float(dettes)) / ((float(revenu) - float(depenses)) * 365) * 100 / 30



application = Application([ServiceSolvabilite],
                          tns='spyne.examples.solvabilite',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11()
                          )
if __name__ == '__main__':
    wsgi_app = WsgiApplication(application)
    twisted_apps = [
        (wsgi_app, b'ServiceSolvabilite'),
    ]
    sys.exit(run_twisted(twisted_apps, 8003))