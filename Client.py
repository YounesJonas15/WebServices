from suds.client import Client
import tkinter as tk

# Fonction pour soumettre les informations
def soumettre_informations():
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    ville = entry_ville.get()
    email = entry_email.get()
    type_immobilier = entry_type.get()
    nombre_piece = entry_piece.get()
    montant = entry_montant.get()
    revenu = entry_revenu.get()
    depenses = entry_depenses.get()

    recevoirDemandeService_client = Client('http://localhost:8000/ReceptionDemandeService?wsdl')

    result = recevoirDemandeService_client.service.recevoir_demande(
        nom, prenom, ville, email, type_immobilier, montant, nombre_piece, revenu, depenses
    )

# Création de l'interface utilisateur
root = tk.Tk()
root.title("Formulaire de demande de prêt")

# Création des champs de saisie
label_nom = tk.Label(root, text="Nom : ")
label_nom.grid(row=0, column=0)
entry_nom = tk.Entry(root)
entry_nom.grid(row=0, column=1)

label_prenom = tk.Label(root, text="Prénom : ")
label_prenom.grid(row=1, column=0)
entry_prenom = tk.Entry(root)
entry_prenom.grid(row=1, column=1)

label_ville = tk.Label(root, text="Ville : ")
label_ville.grid(row=2, column=0)
entry_ville = tk.Entry(root)
entry_ville.grid(row=2, column=1)

label_email = tk.Label(root, text="Email : ")
label_email.grid(row=3, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=3, column=1)

label_type = tk.Label(root, text="Type d'immobilier : ")
label_type.grid(row=4, column=0)
entry_type = tk.Entry(root)
entry_type.grid(row=4, column=1)

label_piece = tk.Label(root, text="Nombre de pièces : ")
label_piece.grid(row=5, column=0)
entry_piece = tk.Entry(root)
entry_piece.grid(row=5, column=1)

label_montant = tk.Label(root, text="Montant : ")
label_montant.grid(row=6, column=0)
entry_montant = tk.Entry(root)
entry_montant.grid(row=6, column=1)

label_revenu = tk.Label(root, text="Revenu : ")
label_revenu.grid(row=7, column=0)
entry_revenu = tk.Entry(root)
entry_revenu.grid(row=7, column=1)

label_depenses = tk.Label(root, text="Dépenses : ")
label_depenses.grid(row=8, column=0)
entry_depenses = tk.Entry(root)
entry_depenses.grid(row=8, column=1)

# Bouton de soumission
submit_button = tk.Button(root, text="Soumettre", command=soumettre_informations)
submit_button.grid(row=9, column=1)

root.mainloop()
