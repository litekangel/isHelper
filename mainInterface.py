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

def Manage_besoin():
    frame_besoin = besoin(fenetre, MgrBesoins)
    global frame_besoin
    frame_besoin.grid()
    frame_besoin.Renseigner_Besoin()

def Manage_exigence():
    frame_exigence = exigence(fenetre, MgrBesoins, MgrExigences)
    global frame_exigence
    frame_exigence.grid()
    frame_exigence.Renseigner_Exigence()

def Manage_piece():
    frame_piece = piece(fenetre, MgrPieces)
    global frame_piece
    frame_piece.grid()
    frame_piece.Renseigner_Piece()

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
menu1.add_command(label="Renseigner Besoin", command=Manage_besoin)
menu1.add_command(label="Renseigner Exigence", command=Manage_exigence)
menu1.add_command(label="Renseigner Pièce", command=Manage_piece)
menubar.add_cascade(label="Gérer", menu=menu1)

menu2 = tk.Menu(menubar, tearoff=0)
menu2.add_command(label="Couper")
menu2.add_command(label="Copier")
menu2.add_command(label="Coller")
menubar.add_cascade(label="Editer", menu=menu2)

fenetre.config(menu=menubar)

#test si la bdd ouverte permet l'ajout d'exigences

fenetre.mainloop()