from classes import *
from modeles import *
import sqlite3 as sql
import tkinter as tk

class exigence(tk.Frame):
    def __init__(self, fenetre, MgrBesoins, MgrExigences):
        super().__init__(fenetre)
        self.value=tk.StringVar()
        self.intitule = tk.StringVar()
        self.critere = tk.StringVar()
        self.niveau = tk.StringVar()
        self.mere = tk.StringVar()
        self.exigence_mere = tk.StringVar()
        self.nom_exigence = tk.StringVar()
        self.besoin_origine = tk.StringVar(None)
        self.MgrBesoins=MgrBesoins
        self.MgrExigences=MgrExigences

    def Renseigner_Exigence(self):
        def CreerExigence():
            self.MgrExigences.create(self.intitule.get(), self.critere.get(), besoin=int(self.besoin_origine.get()),
                                espece=int(self.value.get()), niveau=int(self.niveau.get()),
                                exigence_mere=int(self.exigence_mere.get()))
            self.destroy()

        def DemanderExigenceMere():
            if int(self.mere.get()) == False:
                for i in self.MgrExigences.read():
                    tk.Radiobutton(self, text=str(i.intitule), variable=self.exigence_mere, value=i.idex).grid()
                tk.Button(self, text="Valider", command=CreerExigence).grid()
            else:
                self.MgrExigences.create(self.intitule.get(), self.critere.get(), besoin=int(self.besoin_origine.get()),
                                    espece=int(self.value.get()), niveau=int(self.niveau.get()),
                                    exigence_mere=0)
                self.destroy()

        def Valider():
            # récupération de l'intitulé de l'exigence
            txt1 = tk.Label(self, text='Intitulé :')
            entree0 = tk.Entry(self, textvariable=self.intitule, width=100)
            # récupération de la caractéristique de l'exigence
            txt2 = tk.Label(self, text='Caractéristique :')
            entree1 = tk.Entry(self, textvariable=self.critere, width=30)
            # récupération du niveau du critère
            txt3 = tk.Label(self, text='Niveau du critère :')
            entree2 = tk.Entry(self, textvariable=self.niveau, width=30)
            # récupération de la caratéristique mère
            txt4 = tk.Label(self, text='Exigence mère :')
            bouton4_1 = tk.Radiobutton(self, text="Oui", variable=self.mere, value=1)
            bouton4_2 = tk.Radiobutton(self, text="Non", variable=self.mere, value=0)
            # Récupération beoin lié
            txt5 = tk.Label(self, text='Besoin lié :')

            txt1.grid()
            txt2.grid()
            txt3.grid()
            txt4.grid()
            entree0.grid(row=3, column=1)
            entree1.grid(row=4, column=1)
            entree2.grid(row=5, column=1)
            bouton4_1.grid(row=6, column=1, )
            bouton4_2.grid(row=6, column=2)
            txt5.grid()
            for i in self.MgrBesoins.read():
                tk.Radiobutton(self, text=str(i.intitule), variable=self.besoin_origine, value=i.id_besoin).grid(
                    column=1)
            print(self.besoin_origine.get())
            # Bouton de sortie
            bouton4 = tk.Button(self, text="Valider", command=DemanderExigenceMere)
            bouton4.grid(column=1)

        bouton1 = tk.Radiobutton(self, text="Fonctionnelle", variable=self.value, value=1)
        bouton2 = tk.Radiobutton(self, text="Non Fonctionnelle", variable=self.value, value=0)
        bouton3 = tk.Button(self, text="Valider", command=Valider)
        bouton1.grid()
        bouton2.grid()
        bouton3.grid()

    def Del_Exigence(self):
        def Valider():
            self.MgrExigences.delete(self.nom_exigence)
            self.destroy()

        for i in self.MgrExigences.read():
            texte = str(i.intitule)
            tk.Radiobutton(self, text=texte, variable=self.nom_exigence, value=i.idex).pack()
        tk.Button(self, text="Valider", command=Valider).pack()

    def Modifier_Exigence(self):
        def Update():
            self.MgrExigences.read(int(self.nom_exigence.get())).intitule = self.intitule.get()
            self.MgrExigences.read(int(self.nom_exigence.get())).critere = self.critere.get()
            self.MgrExigences.read(int(self.nom_exigence.get())).besoin = self.besoin_origine.get()
            self.MgrExigences.read(int(self.nom_exigence.get())).espece = self.value.get()
            self.MgrExigences.read(int(self.nom_exigence.get())).niveau = self.niveau.get()
            self.MgrExigences.update(self.MgrExigences.read(int(self.nom_exigence.get())))
            self.destroy()

        def Valider():
            # récupération de l'intitulé de l'exigence
            txt1 = tk.Label(self, text='Intitulé :')
            entree0 = tk.Entry(self, textvariable=self.intitule, width=100)
            # récupération de la caractéristique de l'exigence
            txt2 = tk.Label(self, text='Caractéristique :')
            entree1 = tk.Entry(self, textvariable=self.critere, width=30)
            # récupération du niveau du critère
            txt3 = tk.Label(self, text='Niveau du critère :')
            entree2 = tk.Entry(self, textvariable=self.niveau, width=30)
            # Récupération beoin lié
            txt5 = tk.Label(self, text='Besoin lié :')

            txt1.grid(row=0)
            txt2.grid(row=1)
            txt3.grid(row=2)
            entree0.grid(row=0, column=1)
            entree1.grid(row=1, column=1)
            entree2.grid(row=2, column=1)
            txt5.grid(row=4)
            for i in self.MgrBesoins.read():
                tk.Radiobutton(self, text=str(i.intitule), variable=self.besoin_origine, value=i.id_besoin).grid()
            # Bouton de sortie
            bouton4 = tk.Button(self, text="Valider", command=Update)
            bouton4.grid()

        tk.Label(self, text="Identifiant de l'exigence à modifier: ").grid()
        for i in self.MgrExigences.read():
            texte = str(i.intitule)
            tk.Radiobutton(self, text=texte, variable=self.nom_exigence, value=i.idex).grid()
        tk.Button(self, text="Valider", command=Valider).grid()