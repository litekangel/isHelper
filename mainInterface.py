import tkinter as tk
from tkinter import filedialog

from Frames.Besoin import besoin
from Frames.Exigence import exigence
from Frames.Piece import piece
from Modules.lectureBesoin import read_besoin
from Modules.lectureExigence import read_exigence
from Modules.lectureNomenclature import read_nomenclature
from Modules.saveProject import save_project
from modeles import *

db = 'bdd.sql'
MgrExigences = ExigencesMgr(db)
MgrBesoins = BesoinsMgr(db)
MgrPieces = PieceMgr(db)
# MgrNomenclature = NomenclatureMgr(db)

fenetre = tk.Tk()

fenetre.tk_setPalette(background='#2c3e50', troughColor="#c1392b")

# définition des différentes frame
frame_besoin = besoin(fenetre, MgrBesoins)
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
    global frame_besoin
    frame_besoin.destroy()
    frame_besoin = besoin(fenetre, MgrBesoins)
    frame_besoin.grid()
    # x est une variable locale qui permet de gérer l'action à réaliser
    if x == 1:
        frame_besoin.Renseigner_Besoin()
        Update_menu()
    elif x == 2:
        frame_besoin.Del_Besoin()
    elif x == 3:
        frame_besoin.Modifier_Besoin()


def Manage_exigence(x):
    global frame_exigence
    frame_exigence.destroy()
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
    global frame_piece
    frame_piece.destroy()
    frame_piece = piece(fenetre, MgrPieces)
    frame_piece.grid()
    # x est une variable locale qui permet de gérer l'action à réaliser
    if x == 1:
        frame_piece.Renseigner_Piece()
    elif x == 2:
        frame_piece.Del_Piece()
    elif x == 3:
        frame_piece.Modifier_Piece()


def Import_besoin():
    fenetre.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                  filetypes=[("csv files", "*.csv")])
    read_besoin(fenetre.filename, MgrBesoins)


def Import_exigence():
    fenetre.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                  filetypes=[("csv files", "*.csv")])
    read_exigence(fenetre.filename, MgrExigences)


# def Import_piece():
#    fenetre.filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=[("csv files", "*.csv")])
#    read_piece(fenetre.filename, MgrPieces)

def Import_nomenclature():
    fenetre.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                  filetypes=[("csv files", "*.csv")])
    read_nomenclature(fenetre.filename, MgrNomenclature)


def Export_project():
    fenetre.filename = filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                                    filetypes=[("csv files", "*.csv")])
    save_project(fenetre.filename, MgrBesoins, MgrExigences)


# Définition du fond d'écran de l'application

fenetre.title("IsHelper")
logo = tk.PhotoImage(file="ish.gif")
pic = tk.Label(fenetre, image=logo, bg='#2c3e50')
pic.grid()
# message d'accueil
hometxt = "La solution d'aide à l'ingénierie système"
text = tk.Label(fenetre, text=hometxt, bg='#2c3e50', fg='#ecf0f1', font=('Helvetica', 18))
text.grid()

menubar = tk.Menu(fenetre)
menubar.configure(background='#ecf0f1', foreground="#2c3e50")

menu1 = tk.Menu(menubar, tearoff=0)
menu1.configure(background='#ecf0f1', foreground="#2c3e50")
# utilisation des fonctions lambda pour pouvoir passer des paramètres dans la fct
menu1.add_command(label="Renseigner Besoin", command=lambda x=1: Manage_besoin(1))
menu1.add_command(label="Renseigner Exigence", state='disabled', command=lambda x=1: Manage_exigence(1))
menu1.add_command(label="Renseigner Pièce", command=lambda x=1: Manage_piece(1))
menu1.add_command(label='Supprimer un Besoin', command=lambda x=2: Manage_besoin(2))
menu1.add_command(label='Supprimer une Exigence', state='disabled', command=lambda x=2: Manage_exigence(2))
menu1.add_command(label='Supprimer une Pièce', command=lambda x=2: Manage_piece(2))
menu1.add_command(label='Modifier un Besoin', command=lambda x=3: Manage_besoin(3))
menu1.add_command(label='Modifier une Exigence', state='disabled', command=lambda x=3: Manage_exigence(3))
menu1.add_command(label='Modifier une Pièce', command=lambda x=3: Manage_piece(3))
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.destroy)
menubar.add_cascade(label="Gérer", menu=menu1)

menu2 = tk.Menu(menubar, tearoff=0)
menu2.configure(background='#ecf0f1', foreground="#2c3e50")
menu2.add_command(label='Importer besoins', command=Import_besoin)
menu2.add_command(label='Importer exigences', command=Import_exigence)
menu2.add_command(label='Importer nomenclature', command=Import_nomenclature)
# menu2.add_command(label='Importer pièces', command=Import_piece())
menu2.add_command(label='Exporter projet', command=Export_project)
menubar.add_cascade(label="Données", menu=menu2)

# Intérêt mdrrrrrrrrrrr
menu3 = tk.Menu(menubar, tearoff=0)
menu3.add_command(label="Couper")
menu3.add_command(label="Copier")
menu3.add_command(label="Coller")
menubar.add_cascade(label="Editer", menu=menu3)
menu3.configure(background='#ecf0f1', foreground="#2c3e50")
fenetre.config(menu=menubar)

# test si la bdd ouverte permet l'ajout d'exigences

fenetre.mainloop()
