import json
import sys
from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.util.wsgi_wrapper import run_twisted
from suds.client import Client

class ServiceOrchestration(ServiceBase):
    @rpc(Unicode,_returns=str)
    def Orchestration(ctx,file_name):
        print("jai recu", {file_name})
        #Extraction des information
        extractionDonneClientService_client = Client('http://localhost:8002/ServiceExtractionClient?wsdl')
        nom, prenom, adresse, email, montant, nombre_piece, superfecie, revenu, depenses = extractionDonneClientService_client.service.Extraction_donne_client(file_name)
        print(nom[1])
        print(prenom[1])
        # Service de solvabilite
        solvabilite_calcul = Client('http://localhost:8003/ServiceSolvabilite?wsdl')
        solvabilite_score = solvabilite_calcul.service.solvabiliteClient(nom[1], prenom[1], email[1], montant[1], revenu[1], depenses[1])
        print(solvabilite_score)

        # Service de propriete
        propriete_calcul = Client('http://localhost:8004/ServicePropriete?wsdl')
        propriete_score = propriete_calcul.service.proprieteClient(nombre_piece[1], superfecie[1],adresse[1],montant[1])
        print(propriete_score)
        decisionService = Client('http://localhost:8005/ServiceDecision?wsdl')
        finalDecision = decisionService.service.decisionClient(solvabilite_score, propriete_score)
        if (finalDecision):
            print("vous avez le pret")
            return ("Vous avez eu le pret")
        else:
            print("vous n'avez pas ")
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
