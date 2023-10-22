import json
import sys
from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.util.wsgi_wrapper import run_twisted
from suds.client import Client


class ServiceSolvabilite(ServiceBase):
    @rpc( Unicode, Unicode, Unicode,Unicode,Unicode,Unicode, _returns=bool)
    def solvabiliteClient(ctx, nom, prénom, email, montant, revenu, depenses):
        all_demandes = []
        result_tuple = {}
        try:
            with open("banque.json", "r") as f:
                all_demandes = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            pass

        
        for demande_data in all_demandes:
            if demande_data["Nom du Client"] == nom:
            # Récupérer le tuple (nom, prenom, email) correspondant
                result_tuple = demande_data
        
        dettes = sum(result_tuple["Dete"]) 
                   
        if (((float(montant) + float(dettes))/((float(revenu) - float(depenses))*365) * 100)/30) < 110:
            return True
        else:
            return False
    
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