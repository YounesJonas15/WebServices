import os
import time

def listener(path):
    dirs = os.listdir(path)
    before = dict([(f, None) for f in dirs])  # Contenu du dossier au démarrage
    while True:
        time.sleep(10) 

        after = dict([(f, None) for f in os.listdir(path)]) 

        added = [f for f in after if not f in before]  # Liste des fichiers ajoutés depuis le dernier check

        if added:  # Si des fichiers ont été ajoutés
            print(f"Les fichiers suivants ont été ajoutés : {', '.join(added)}")

        before = after  # Mettre à jour le contenu précédent pour le prochain check
