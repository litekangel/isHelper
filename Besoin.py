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
        self.nom_besoin = tk.StringVar()

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

    def Del_Besoin(self):
        def Valider():
            self.MgrBesoins.delete(self.nom_besoin)
            self.destroy()

        for i in self.MgrBesoins.read():
            texte = str(i.intitule)
            tk.Radiobutton(self, text=texte, variable=self.nom_besoin, value=i.id_besoin).pack()
        tk.Button(self, text="Valider", command=Valider).pack()

    def Modifier_Besoin(self):
        def Update():
            self.MgrBesoins.read(int(self.nom_besoin.get())).intitule = self.intitule1.get()
            self.MgrBesoins.read(int(self.nom_besoin.get())).primaire = int(self.value.get())
            self.MgrBesoins.update(self.MgrBesoins.read(int(self.nom_besoin.get())))
            self.destroy()

        def Valider():
            # récupération de l'intitulé du besoin
            txt1 = tk.Label(self, text='Intitulé :')
            entree0 = tk.Entry(self, textvariable=self.intitule1, width=100)
            txt1.grid()
            entree0.grid(row= 2+len(self.MgrBesoins.read()), column=1)
            tk.Radiobutton(self, text="Besoin Primaire", variable=self.value, value=1).grid()
            tk.Radiobutton(self, text="Besoin Secondaire", variable=self.value, value=0).grid()
            tk.Button(self, text="Valider", command=Update).grid()

        tk.Label(self, text="Identifiant du besoin à modifier: ").grid()
        for i in self.MgrBesoins.read():
            texte = str(i.intitule)
            tk.Radiobutton(self, text=texte, variable=self.nom_besoin, value=i.id_besoin).grid()
        tk.Button(self, text="Valider", command=Valider).grid()