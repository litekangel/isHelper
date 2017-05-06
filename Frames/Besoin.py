from classes import *
from modeles import *
import sqlite3 as sql
import tkinter as tk
from tkinter.ttk import *

class besoin(tk.Frame):
    def __init__(self, fenetre, MgrBesoins):
        super().__init__(fenetre)
        self.intitule1 = tk.StringVar()
        self.value = tk.StringVar()
        self.MgrBesoins=MgrBesoins
        self.nom_besoin = tk.StringVar()
        self.origine = tk.StringVar()
        self.modele = tk.StringVar()

    def Renseigner_Besoin(self):
        import tkinter as tk

        def CreerBesoin():
            var=Select.get()+self.intitule1.get()
            self.MgrBesoins.create(var, primaire=int(self.value.get()), origine=self.origine.get(), nature=self.modele.get())
            self.destroy()

        def Valider():
            # nettoyage de la zone d'affichage
            for elt in self.winfo_children():
                elt.destroy()
            # récupération de l'intitulé du besoin
            txt1 = tk.Label(self, text='Intitulé :')
            #on force l'écriture partielle du besoin en fct du type de besoin demandé
            #liste des possibilités
            liste_entree = [["Pouvoir"],["Doit être", "Doit avoir"],["Interréagir", "Communiquer", "Permettre"],
                            ["Assurer"],["Utiliser", "Respecter","Imposer"],["S'adapter"]]
            pos=Stock.index(self.modele.get())
            #Mise à jour zone écriture en fct
            global Select
            Select = tk.StringVar()
            Stock2 = liste_entree[pos]
            ListeElt = Combobox(self, textvariable=Select, values=Stock2, state='readonly')
            ListeElt.grid(row=5, column=1)
            entree0 = tk.Entry(self, textvariable=self.intitule1, width=100)
            # Bouton de sortie
            bouton4 = tk.Button(self, text="Valider", command=CreerBesoin)
            txt1.grid(row=5)
            entree0.grid(row=5, column=2)
            tk.Label(self, text='Origine du besoin :').grid(row=6)
            tk.Entry(self, textvariable=self.origine, width=100).grid(row=6, column=1 and 2)
            bouton4.grid(row=7, column=0)

        bouton1 = tk.Radiobutton(self, text="Besoin Primaire", variable=self.value, value=1)
        bouton2 = tk.Radiobutton(self, text="Besoin Secondaire", variable=self.value, value=0)
        bouton3 = tk.Button(self, text="Valider", command=Valider)
        bouton1.grid()
        bouton2.grid()
        tk.Label(self, text='Type de besoin').grid()
        Stock = ['Besoin de service', "Beosin d'efficacité", "Besoin d'intéraction", "Besoin de sécurité",
                 "Besoin de contrainte", "Besoin d'environnement"]
        ListeElt = Combobox(self, textvariable=self.modele, values=Stock, state='readonly')
        ListeElt.grid(row=2, column=1)
        bouton3.grid()

    def Del_Besoin(self):
        def Valider():
            self.MgrBesoins.delete(int(Select.get()[:Select.get().index('.')]))
            self.destroy()
        Select = tk.StringVar()
        Stock = list()
        for i in self.MgrBesoins.read():
            Stock.append(str(i.id_besoin) + '. ' + i.intitule)
        ListeElt = Combobox(self, textvariable=Select, values=Stock, state='readonly')
        ListeElt.grid()
        tk.Button(self, text="Valider", command=Valider).grid()

    def Modifier_Besoin(self):
        def Update():
            bes=self.MgrBesoins.read(int(Select.get()[:Select.get().index('.')]))
            bes.intitule = self.intitule1.get()
            bes.primaire = int(self.value.get())
            bes.origine = self.origine.get()
            self.MgrBesoins.update(bes)
            self.destroy()

        def Valider():
            # nettoyage de la zone d'affichage
            for elt in self.winfo_children():
                elt.destroy()
            # récupération de l'intitulé du besoin
            txt1 = tk.Label(self, text='Intitulé :')
            entree0 = tk.Entry(self, textvariable=self.intitule1, width=100)
            txt1.grid()
            entree0.grid(row= 0, column=1)
            tk.Label(self, text='Origine du besoin :').grid()
            tk.Entry(self, textvariable=self.origine, width=100).grid(row=1, column=1)
            tk.Radiobutton(self, text="Besoin Primaire", variable=self.value, value=1).grid(row=2, column= 0)
            tk.Radiobutton(self, text="Besoin Secondaire", variable=self.value, value=0).grid(row=2, column= 1)
            tk.Button(self, text="Valider", command=Update).grid(column=1)

        tk.Label(self, text="Identifiant du besoin à modifier: ").grid()
        Select = tk.StringVar()
        Stock = list()
        for i in self.MgrBesoins.read():
            Stock.append(str(i.id_besoin) + '. ' + i.intitule)
        ListeElt = Combobox(self, textvariable=Select, values=Stock, state='readonly')
        ListeElt.grid()
        tk.Button(self, text="Valider", command=Valider).grid()