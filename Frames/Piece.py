from classes import *
from modeles import *
import sqlite3 as sql
import tkinter as tk

class piece(tk.Frame):
    def __init__(self, fenetre, MgrPieces):
        super().__init__(fenetre)
        self.MgrPieces=MgrPieces
        self.nom_piece = tk.StringVar()
        self.couleur = tk.StringVar()
        self.intitule_piece = tk.StringVar()

    def Renseigner_Piece(self):

        def CreerPiece():
            self.MgrPieces.create(self.nom_piece.get(), self.couleur.get())
            self.destroy()

        txt1 = tk.Label(self, text='Nom de la pièce :')
        entree1 = tk.Entry(self, textvariable=self.nom_piece, width=50)
        txt2 = tk.Label(self, text='Couleur :')
        entree2 = tk.Entry(self, textvariable=self.couleur, width=50)
        bouton1 = tk.Button(self, text="Valider", command=CreerPiece)
        txt1.grid()
        entree1.grid()
        txt2.grid()
        entree2.grid()
        bouton1.grid()

    def Del_Piece(self):
        def Valider():
            self.MgrPieces.delete(self.nom_piece)
            self.destroy()

        for i in self.MgrPieces.read():
            texte = str(i.nom)
            tk.Radiobutton(self, text=texte, variable=self.nom_piece, value=i.nom).pack()
        tk.Button(self, text="Valider", command=Valider).pack()

    def Modifier_Piece(self):
        def Update():
            # Mise à jour des variables
            self.MgrPieces.read(int(self.nom_piece.get())).nom = self.intitule_piece.get()
            self.MgrPieces.read(int(self.nom_piece.get())).couleur = self.couleur.get()
            self.MgrPieces.update(self.MgrPieces.read(int(self.nom_piece.get())))
            self.destroy()

        def Valider():
            tk.Label(self, text='Nom de la pièce :').grid()
            tk.Entry(self, textvariable=self.intitule_piece, width=50).gid()
            tk.Label(self, text='Couleur :').grid()
            tk.Entry(self, textvariable=self.couleur, width=50).grid()
            tk.Button(self, text="Valider", command=Update).grid()

        tk.Label(self, text="Identifiant de la pièce à modifier: ").grid()
        for i in self.MgrPieces.read():
            texte = str(i.nom)
            tk.Radiobutton(self, text=texte, variable=self.nom_piece, value=i.id_piece).pack()
        tk.Button(self, text="Valider", command=Valider).pack()