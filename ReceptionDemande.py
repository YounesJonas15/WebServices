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
    @rpc(Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, Unicode,Unicode, Unicode, _returns=Unicode)
    def recevoir_demande(
        ctx, nom, prenom, adresse, email, montant, nombre_piece, superficie, revenu, depenses
    ):
        demande_data = {
            "Nom du Client": nom,
            "Prenom du Client": prenom,
            "Adresse": adresse,
            "Email": email,
            "Montant": montant,
            "Nombre de pieces": nombre_piece,
            "Superficie": superficie,
            "Revenu" : revenu,
            "Depenses" : depenses
        }
        all_demandes = []
        try:
            with open("demandes.json", "r") as f:
                all_demandes = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            pass
        
        all_demandes.append(demande_data)
        

        with open("demandes.json", "w") as f:
            json.dump(all_demandes, f, indent=4)

        #Appel service orchestre
        orchestre_Reception = Client('http://localhost:8001/ServiceOrchestration?wsdl')
        result = orchestre_Reception.service.Orchestration()
        return result
    
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