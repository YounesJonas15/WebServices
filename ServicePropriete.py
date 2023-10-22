import json
import sys
from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.util.wsgi_wrapper import run_twisted
from suds.client import Client


class ServicePropriete(ServiceBase):
    @rpc( Unicode, Unicode, _returns=float)
    def proprieteClient(ctx, nb_piece, superficie):
        return 50
    
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