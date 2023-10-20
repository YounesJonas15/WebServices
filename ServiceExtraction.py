import json

# Ouvrir le fichier JSON
with open('demande.json', 'r') as json_file:
    data = json.load(json_file)
    
print(data)
