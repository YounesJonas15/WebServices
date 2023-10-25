from suds.client import Client
import tkinter as tk

"""
def get_input():
    global nom, prenom, adresse, email, montant, nombre_piece, superficie, revenu, depenses
    nom = entry_nom.get()
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    adresse = entry_adresse.get()
    email = entry_email.get()
    montant = entry_montant.get()
    nombre_piece = entry_nombre_piece.get()
    superficie = entry_superficie.get()
    revenu = entry_revenu.get()
    depenses = entry_depenses.get()

# Interface graphique
root = tk.Tk()
root.title("Formulaire de demmande de pret immobilier")

# Labels
tk.Label(root, text="Nom").grid(row=0)
tk.Label(root, text="Prénom").grid(row=1)
tk.Label(root, text="Adresse").grid(row=2)
tk.Label(root, text="Email").grid(row=3)
tk.Label(root, text="Montant").grid(row=4)
tk.Label(root, text="Nombre de pièce").grid(row=5)
tk.Label(root, text="Superficie").grid(row=6)
tk.Label(root, text="Revenu").grid(row=7)
tk.Label(root, text="Dépenses").grid(row=8)

# Entrées
entry_nom = tk.Entry(root)
entry_prenom = tk.Entry(root)
entry_adresse = tk.Entry(root)
entry_email = tk.Entry(root)
entry_montant = tk.Entry(root)
entry_nombre_piece = tk.Entry(root)
entry_superficie = tk.Entry(root)
entry_revenu = tk.Entry(root)
entry_depenses = tk.Entry(root)

entry_nom.grid(row=0, column=1)
entry_prenom.grid(row=1, column=1)
entry_adresse.grid(row=2, column=1)
entry_email.grid(row=3, column=1)
entry_montant.grid(row=4, column=1)
entry_nombre_piece.grid(row=5, column=1)
entry_superficie.grid(row=6, column=1)
entry_revenu.grid(row=7, column=1)
entry_depenses.grid(row=8, column=1)

# Bouton de soumission
tk.Button(root, text="Soumettre", command=get_input).grid(row=9, column=1, pady=10)



print(result)

root.mainloop()
"""
# Saisie des informations du client
nom = input("Nom : ")
prenom = input("prénom: ")
adresse = input("Adresse: ")
email = input("Email: ")
montant = input("Montant: ")
nombre_piece= input("nombre de piece: ")
superfecie = input("superficie : ")
revenu = input("Revenu: ")
depenses = input("Dépenses: ")


recevoirDemandeService_client = Client('http://localhost:8000/ReceptionDemandeService?wsdl')

result = recevoirDemandeService_client.service.recevoir_demande(
    nom, prenom, adresse, email, montant,nombre_piece, superfecie, revenu, depenses
)


