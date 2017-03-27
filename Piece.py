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