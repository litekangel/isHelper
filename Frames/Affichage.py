import tkinter as tk
from tkinter.ttk import *

class affichage(tk.Frame):
    def __init__(self, fenetre, MgrBesoins, MgrExigences, MgrPieces):
        super().__init__(fenetre)
        self.MgrBesoins = MgrBesoins
        self.MgrExigences = MgrExigences
        self.MgrPieces=MgrPieces

    def affichage_besoins(self):
        tk.Label(self, text="Liste des besoins").grid()
        Stock = list()
        for i in self.MgrBesoins.read():
            Stock.append(str(i.id_besoin) + '. ' + i.intitule)
        ListeElt = Combobox(self, values=Stock, state='readonly')
        ListeElt.grid()

    def affichage_exigences(self):
        tk.Label(self, text="Liste des besoins").grid()
        Stock = list()
        for i in self.MgrExigences.read():
            Stock.append(str(i.idex) + '. ' + i.intitule)
        ListeElt = Combobox(self, values=Stock, state='readonly')
        ListeElt.grid()

    def affichage_pieces(self):
        tk.Label(self, text="Liste des besoins").grid()
        Stock = list()
        for i in self.MgrPieces.read():
            Stock.append(str(i.id_piece) + '. ' + i.nom)
        ListeElt = Combobox(self, values=Stock, state='readonly')
        ListeElt.grid()
