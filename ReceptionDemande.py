import logging
import os
import json
logging.basicConfig(level=logging.DEBUG)
import sys
from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.util.wsgi_wrapper import run_twisted
from suds.client import Client

class DemandeService(ServiceBase):
    @rpc(Unicode, Unicode, Unicode, Unicode,Unicode ,Unicode, Unicode, Unicode,Unicode, _returns=Unicode)
    def recevoir_demande(
        ctx, nom, prenom, ville, email,type, montant, nombre_piece, revenu, depenses
    ):
        demande_data = {
            "Nom du Client": nom,
            "Prenom du Client": prenom,
            "Ville": ville,
            "Email": email,
            "Type" : type,
            "Montant": montant,
            "Nombre de pieces": nombre_piece,
            "Revenu" : revenu,
            "Depenses" : depenses
        }
        file_name = f"{nom+prenom}.json"  
        file_path = os.path.join("demandes", file_name) 

        with open(file_path, "w") as f:
            json.dump(demande_data, f, indent=4)

application = Application([DemandeService],
                          tns='spyne.examples.Reception',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11()
                          )
if __name__ == '__main__':
    wsgi_app = WsgiApplication(application)
    twisted_apps = [
        (wsgi_app, b'ReceptionDemandeService'),
    ]
    
    sys.exit(run_twisted(twisted_apps, 8000))