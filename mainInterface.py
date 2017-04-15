import tkinter as tk
from Besoin import *
from Exigence import *
from Piece import *
import sqlite3 as sql
import tkinter as tk
from classes import *
from modeles import *

db = sql.connect('bdd.sql')
MgrExigences = ExigencesMgr(db)
MgrBesoins = BesoinsMgr(db)
MgrPieces = PieceMgr(db)

fenetre = tk.Tk()

#définition des différents frame
frame_besoin=besoin(fenetre, MgrBesoins)
frame_exigence = exigence(fenetre, MgrBesoins, MgrExigences)
frame_piece = piece(fenetre, MgrPieces)

def Update_menu():
    menubar.delete(0, 1)
    menu1 = tk.Menu(menubar, tearoff=0)
    menu1.add_command(label="Renseigner Besoin", command=lambda x=1: Manage_besoin(1))
    menu1.add_command(label="Renseigner Exigence", command=lambda x=1: Manage_exigence(1))
    menu1.add_command(label="Renseigner Pièce", command=lambda x=1: Manage_piece(1))
    menu1.add_command(label='Supprimer un Besoin', command=lambda x=2: Manage_besoin(2))
    menu1.add_command(label='Supprimer une Exigence', command=lambda x=2: Manage_exigence(2))
    menu1.add_command(label='Supprimer une Pièce', command=lambda x=2: Manage_piece(2))
    menu1.add_command(label='Modifier un Besoin', command=lambda x=3: Manage_besoin(3))
    menu1.add_command(label='Modifier une Exigence', command=lambda x=3: Manage_exigence(3))
    menu1.add_command(label='Modifier une Pièce', command=lambda x=3: Manage_piece(3))
    menu1.add_separator()
    menu1.add_command(label="Quitter", command=fenetre.destroy)
    menubar.insert_cascade(0, label='Gérer', menu=menu1)

def Manage_besoin(x):
    frame_besoin.destroy()
    global frame_besoin
    frame_besoin = besoin(fenetre, MgrBesoins)
    frame_besoin.grid()
    #x est une variable locale qui permet de gérer l'action à réaliser
    if x == 1:
        frame_besoin.Renseigner_Besoin()
        Update_menu()
    elif x == 2:
        frame_besoin.Del_Besoin()
    elif x == 3:
        frame_besoin.Modifier_Besoin()

def Manage_exigence(x):
    frame_exigence.destroy()
    global frame_exigence
    frame_exigence = exigence(fenetre, MgrBesoins, MgrExigences)
    frame_exigence.grid()
    # x est une variable locale qui permet de gérer l'action à réaliser
    if x == 1:
        frame_exigence.Renseigner_Exigence()
    elif x == 2:
        frame_exigence.Del_Exigence()
    elif x == 3:
        frame_exigence.Modifier_Exigence()

def Manage_piece():
    frame_piece.destroy()
    global frame_piece
    frame_piece = piece(fenetre, MgrPieces)
    frame_piece.grid()
    # x est une variable locale qui permet de gérer l'action à réaliser
    if x == 1:
        frame_piece.Renseigner_Piece()
    elif x == 2:
        frame_piece.Del_Piece()
    elif x == 3:
        frame_piece.Modifier_Piece()

# Définition du fond d'écran de l'application
fenetre.configure(background='#2c3e50')
fenetre.title("IsHelper")
logo = tk.PhotoImage(file="ish.gif")
pic = tk.Label(fenetre, image=logo, bg='#2c3e50')
pic.grid()
# message d'accueil
hometxt = "La solution d'aide à l'ingénierie système"
text = tk.Label(fenetre, text=hometxt, bg='#2c3e50', fg='#ecf0f1', font=('Helvetica', 18))
text.grid()

menubar = tk.Menu(fenetre)

# Projet
nom_projet = tk.StringVar()
liste_projet = list()
# Equipe humaine
nom_personne = tk.StringVar()
liste_personne = list()
# Tache
nom_tache = tk.StringVar()
tache = tk.StringVar()
temps = tk.StringVar()
nom = tk.StringVar()
pourcentage = tk.StringVar()
liste_tache = list()
# Affichage (définition des dates)
projet = tk.StringVar()
today = tk.StringVar()
start = tk.StringVar()
end = tk.StringVar()
nom_diagramme = tk.StringVar()


menu1 = tk.Menu(menubar, tearoff=0)
# utilisation des fonctions lambda pour pouvoir passer des paramètres dans la fct
menu1.add_command(label="Renseigner Besoin", command=lambda x=1:Manage_besoin(1))
menu1.add_command(label="Renseigner Exigence", state='disabled', command=lambda x=1:Manage_exigence(1))
menu1.add_command(label="Renseigner Pièce", command=lambda x=1:Manage_piece(1))
menu1.add_command(label='Supprimer un Besoin', command=lambda x=2:Manage_besoin(2))
menu1.add_command(label='Supprimer une Exigence', state='disabled', command=lambda x=2:Manage_exigence(2))
menu1.add_command(label='Supprimer une Pièce', command=lambda x=2:Manage_piece(2))
menu1.add_command(label='Modifier un Besoin', command=lambda x=3:Manage_besoin(3))
menu1.add_command(label='Modifier une Exigence', state='disabled', command=lambda x=3:Manage_exigence(3))
menu1.add_command(label='Modifier une Pièce', command=lambda x=3:Manage_piece(3))
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.destroy)
menubar.add_cascade(label="Gérer", menu=menu1)

menu2 = tk.Menu(menubar, tearoff=0)
menu2.add_command(label="Couper")
menu2.add_command(label="Copier")
menu2.add_command(label="Coller")
menubar.add_cascade(label="Editer", menu=menu2)

fenetre.config(menu=menubar)

#test si la bdd ouverte permet l'ajout d'exigences

fenetre.mainloop()