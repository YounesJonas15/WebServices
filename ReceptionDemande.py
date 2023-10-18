import logging
import os
import json
logging.basicConfig(level=logging.DEBUG)
import sys
from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.util.wsgi_wrapper import run_twisted

class DemandeService(ServiceBase):
    @rpc(Unicode, Unicode, Unicode, _returns=Unicode)
    def recevoir_demande(
        ctx, nom_client, adresse, email
    ):
        demande_data = {
            "Nom du Client": nom_client,
            "Adresse": adresse,
            "Email": email,
        }

        json_file = "demandes.json"
        if os.path.isfile(json_file):
            with open(json_file, "r") as f:
                data = json.load(f)
        else:
            data = []

        data.append(demande_data)

        with open(json_file, "w") as f:
            json.dump(data, f, indent=4)

        return "Demande reçue et enregistrée avec succès."

application = Application([DemandeService],
                          tns='spyne.examples.hello',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11()
                          )
if __name__ == '__main__':
    wsgi_app = WsgiApplication(application)
    twisted_apps = [
        (wsgi_app, b'ReceptionDemandeService'),
    ]
    
    sys.exit(run_twisted(twisted_apps, 8000))