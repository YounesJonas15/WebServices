import json
import sys
from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.util.wsgi_wrapper import run_twisted
from suds.client import Client

class ServiceOrchestration(ServiceBase):
    @rpc(_returns=str)
    def Orchestration(ctx):
        extractionDonneClientService_client = Client('http://localhost:8002/ServiceExtractionClient?wsdl')
        temp = extractionDonneClientService_client.service.Extraction_donne_client()
        result = temp[0]
        decisionService = Client('http://localhost:8005/ServiceDecision?wsdl')
        finalDecision = decisionService.service.decisionClient(result[0], result[1])
        if (finalDecision):
            return ("Vous avez eu le pret")
        else:
            return ("Vous n'avez pas eu le pret")

        
        
    
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
