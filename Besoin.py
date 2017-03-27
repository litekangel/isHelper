from classes import *
from modeles import *
import sqlite3 as sql
import tkinter as tk

class besoin(tk.Frame):
    def __init__(self, fenetre, MgrBesoins):
        super().__init__(fenetre)
        self.intitule1 = tk.StringVar()
        self.value = tk.StringVar()
        self.MgrBesoins=MgrBesoins

    def Renseigner_Besoin(self):
        import tkinter as tk

        def CreerBesoin():
            self.MgrBesoins.create(self.intitule1.get(), int(self.value.get()))
            self.destroy()

        def Valider():
            # récupération de l'intitulé du besoin
            txt1 = tk.Label(self, text='Intitulé :')
            entree0 = tk.Entry(self, textvariable=self.intitule1, width=100)
            # Bouton de sortie
            bouton4 = tk.Button(self, text="Valider", command=CreerBesoin)
            txt1.grid(row=4)
            entree0.grid(row=4, column=1)
            bouton4.grid(row=5, column=0)

        bouton1 = tk.Radiobutton(self, text="Besoin Primaire", variable=self.value, value=1)
        bouton2 = tk.Radiobutton(self, text="Besoin Secondaire", variable=self.value, value=0)
        bouton3 = tk.Button(self, text="Valider", command=Valider)
        bouton1.grid()
        bouton2.grid()
        bouton3.grid()
