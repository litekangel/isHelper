from classes import *
from modeles import *
import sqlite3 as sql
import tkinter as tk
from tkinter.ttk import *
from tkinter import filedialog

class exigence(tk.Frame):
    def __init__(self, fenetre, MgrBesoins, MgrExigences):
        super().__init__(fenetre)
        self.value=tk.StringVar()
        self.intitule = tk.StringVar()
        self.critere = tk.StringVar()
        self.niveau = tk.StringVar()
        self.mere = tk.StringVar(value='None')
        self.nom_exigence = tk.StringVar()
        self.origine = tk.StringVar(value='None')
        self.MgrBesoins=MgrBesoins
        self.MgrExigences=MgrExigences

    def Renseigner_Exigence(self):
        def CreerExigence():
            if self.origine.get() != 'None':
                self.MgrExigences.create(self.intitule.get(), self.critere.get(), besoin=int(self.origine.get()[:self.origine.get().index('.')]),
                                espece=int(self.value.get()), niveau=int(self.niveau.get()), exigence_mere=None)
                self.destroy()
            elif self.mere.get() != 'None':
                self.MgrExigences.create(self.intitule.get(), self.critere.get(), besoin=None,
                                         espece=int(self.value.get()), niveau=int(self.niveau.get()),
                                         exigence_mere=int(self.mere.get()[:self.mere.get().index('.')]))
                self.destroy()
            else:
                self.MgrExigences.create(self.intitule.get(), self.critere.get(),
                                         besoin=None, espece=int(self.value.get()), niveau=int(self.niveau.get()),
                                         exigence_mere=None)
                self.destroy()

        def Valider():
            # nettoyage de la zone d'affichage
            for elt in self.winfo_children():
                elt.destroy()
            def origine_besoin(event):
                # supression de la surcharge affichage
                for elt in liste_bind:
                    elt.destroy()
                liste_bind.clear()
                # création du nouvel affichage
                Stock=list()
                for i in self.MgrBesoins.read():
                    Stock.append(str(i.id_besoin) + '. ' + i.intitule)
                liste_bind.append(Combobox(self, textvariable=self.origine, values=Stock, state='readonly'))
                liste_bind.append(tk.Button(self, text="Valider", command=CreerExigence))
                bouton4.destroy()
                for elt in liste_bind:
                    elt.grid(column=1)
                self.mere = tk.StringVar(value='None')
            def origine_exigence(event):
                # supression de la surcharge affichage
                for elt in liste_bind:
                    elt.destroy()
                liste_bind.clear()
                # création du nouvel affichage
                Stock = list()
                for i in self.MgrExigences.read():
                    Stock.append(str(i.idex) + '. ' + i.intitule)
                liste_bind.append(Combobox(self, textvariable=self.mere, values=Stock, state='readonly'))
                liste_bind.append(tk.Button(self, text="Valider", command=CreerExigence))
                bouton4.destroy()
                for elt in liste_bind:
                    elt.grid(column=1)
                self.origine = tk.StringVar(value='None')
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
            # Récupération beoin lié
            txt1.grid()
            txt2.grid()
            txt3.grid()
            entree0.grid(row=0, column=1)
            entree1.grid(row=1, column=1)
            entree2.grid(row=2, column=1)
            tk.Label(self, text="Raffinement de l'élément :").grid()
            b=tk.Radiobutton(self, text="Besoin")
            b.grid(row=3, column=1)
            e=tk.Radiobutton(self, text="Exigence")
            e.grid(row=3, column=2)
            #création liste contenant les objets (sous forme de radiobutton) liés à l'exigence
            liste_bind=list()
            b.bind('<1>', origine_besoin)
            e.bind('<1>', origine_exigence)
            # Bouton de sortie
            bouton4 = tk.Button(self, text="Valider", command=CreerExigence)
            bouton4.grid(column=1)

        bouton1 = tk.Radiobutton(self, text="Fonctionnelle", variable=self.value, value=1)
        bouton2 = tk.Radiobutton(self, text="Non Fonctionnelle", variable=self.value, value=0)
        bouton3 = tk.Button(self, text="Valider", command=Valider)
        bouton1.grid()
        bouton2.grid()
        bouton3.grid()

    def Del_Exigence(self):
        def Valider():
            self.MgrExigences.delete(int(Select.get()[:Select.get().index('.')]))
            self.destroy()
        Select = tk.StringVar()
        Stock = list()
        for i in self.MgrExigences.read():
            Stock.append(str(i.idex) + '. ' + i.intitule)
        ListeElt = Combobox(self, textvariable=Select, values=Stock, state='readonly')
        ListeElt.grid()
        tk.Button(self, text="Valider", command=Valider).grid()

    def Modifier_Exigence(self):
        def Update():
            if self.origine.get() != 'None':
                exige = self.MgrExigences.read(int(Select.get()[:Select.get().index('.')]))
                exige.intitule = self.intitule.get()
                exige.critere = self.critere.get()
                exige.origine = int(self.origine.get()[:self.origine.get().index('.')])
                exige.espece = self.value.get()
                exige.niveau = self.niveau.get()
                self.exigence = None
                self.MgrExigences.update(exige)
                self.destroy()
            elif self.mere.get() != 'None':
                exige = self.MgrExigences.read(int(Select.get()[:Select.get().index('.')]))
                exige.intitule = self.intitule.get()
                exige.critere = self.critere.get()
                exige.origine = None
                exige.espece = self.value.get()
                exige.niveau = self.niveau.get()
                self.exigence_mere= int(self.mere.get()[:self.mere.get().index('.')])
                self.MgrExigences.update(exige)
                self.destroy()
            else:
                exige = self.MgrExigences.read(int(Select.get()[:Select.get().index('.')]))
                exige.intitule = self.intitule.get()
                exige.critere = self.critere.get()
                exige.origine = None
                exige.espece = self.value.get()
                exige.niveau = self.niveau.get()
                self.exigence_mere = None
                self.MgrExigences.update(exige)
                self.destroy()
        def Valider():
            #nettoyage de la zone d'affichage
            for elt in self.winfo_children():
                elt.destroy()
            def origine_besoin(event):
                # supression de la surcharge affichage
                for elt in liste_bind:
                    elt.destroy()
                liste_bind.clear()
                # création du nouvel affichage
                Stock=list()
                for i in self.MgrBesoins.read():
                    Stock.append(str(i.id_besoin) + '. ' + i.intitule)
                liste_bind.append(Combobox(self, textvariable=self.origine, values=Stock, state='readonly'))
                liste_bind.append(tk.Button(self, text="Valider", command=Update))
                bouton4.destroy()
                for elt in liste_bind:
                    elt.grid(column=1)
                self.mere = tk.StringVar(value='None')
            def origine_exigence(event):
                # supression de la surcharge affichage
                for elt in liste_bind:
                    elt.destroy()
                liste_bind.clear()
                # création du nouvel affichage
                Stock = list()
                for i in self.MgrExigences.read():
                    Stock.append(str(i.idex) + '. ' + i.intitule)
                liste_bind.append(Combobox(self, textvariable=self.mere, values=Stock, state='readonly'))
                liste_bind.append(tk.Button(self, text="Valider", command=Update))
                bouton4.destroy()
                for elt in liste_bind:
                    elt.grid(column=1)
                self.origine = tk.StringVar(value='None')
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

            position=len(self.MgrExigences.read())
            txt1.grid(row=2+position)
            txt2.grid(row=3+position)
            txt3.grid(row=4+position)
            entree0.grid(row=2+position, column=1)
            entree1.grid(row=3+position, column=1)
            entree2.grid(row=4+position, column=1)
            tk.Label(self, text="Raffinement de l'élément :").grid(row=5+position)
            b = tk.Radiobutton(self, text="Besoin")
            b.grid(row=5+position, column=1)
            e = tk.Radiobutton(self, text="Exigence")
            e.grid(row=5+position, column=2)
            # création liste contenant les objets (sous forme de radiobutton) liés à l'exigence
            liste_bind = list()
            b.bind('<1>', origine_besoin)
            e.bind('<1>', origine_exigence)
            # Bouton de sortie
            bouton4 = tk.Button(self, text="Valider", command=Update)
            bouton4.grid()

        tk.Label(self, text="Identifiant de l'exigence à modifier: ").grid()
        t=list()
        Select = tk.StringVar()
        Stock=list()
        for i in self.MgrExigences.read():
            Stock.append(str(i.idex)+'. ' + i.intitule)
        ListeElt = Combobox(self, textvariable=Select, values=Stock, state='readonly')
        ListeElt.grid()
        tk.Button(self, text="Valider", command=Valider).grid()

    def update_origin(self, exigence_idex):
        def Update():
            if self.origine.get() != 'None':
                exige = self.MgrExigences.read(exigence_idex)
                exige.origine = int(self.origine.get()[:self.origine.get().index('.')])
                self.exigence = None
                self.MgrExigences.update(exige)
                self.destroy()
            else:
                exige = self.MgrExigences.read(exigence_idex)
                exige.origine = None
                self.exigence_mere= int(self.mere.get()[:self.mere.get().index('.')])
                self.MgrExigences.update(exige)
                self.destroy()
        def origine_besoin(event):
            # supression de la surcharge affichage
            for elt in liste_bind:
                elt.destroy()
            liste_bind.clear()
            # création du nouvel affichage
            Stock = list()
            for i in self.MgrBesoins.read():
                Stock.append(str(i.id_besoin) + '. ' + i.intitule)
            liste_bind.append(Combobox(self, textvariable=self.origine, values=Stock, state='readonly'))
            liste_bind.append(tk.Button(self, text="Valider", command=Update))
            for elt in liste_bind:
                elt.grid(column=1)
            self.mere = tk.StringVar(value='None')
        def origine_exigence(event):
            # supression de la surcharge affichage
            for elt in liste_bind:
                elt.destroy()
            liste_bind.clear()
            # création du nouvel affichage
            Stock = list()
            for i in self.MgrExigences.read():
                Stock.append(str(i.idex) + '. ' + i.intitule)
            liste_bind.append(Combobox(self, textvariable=self.mere, values=Stock, state='readonly'))
            liste_bind.append(tk.Button(self, text="Valider", command=Update))
            for elt in liste_bind:
                elt.grid(column=1)
            self.origine = tk.StringVar(value='None')

        tk.Label(self, text="Raffinement de l'élément :").grid()
        b = tk.Radiobutton(self, text="Besoin")
        b.grid(row= 0, column=1)
        e = tk.Radiobutton(self, text="Exigence")
        e.grid(row=0, column=2)
        # création liste contenant les objets (sous forme de radiobutton) liés à l'exigence
        liste_bind = list()
        b.bind('<1>', origine_besoin)
        e.bind('<1>', origine_exigence)

    def Verify_exigence(self):
        liste_ex = list()
        for exigence in self.MgrExigences.read():
            liste_ex.append(exigence)
        def test(i):
            if liste_ex[i].origine == None and liste_ex[i].exigence_mere == None:
                if askquestion('Origine des exigences',
                               """l'exigence "{}" n'est pas liée à un besoin ou à une autre exigence, voulez vous la
                               renseigner ?""".format(exigence.intitule)):
                    self.update_origin(liste_ex[i].idex)
                    tk.Button(self, text=Valider, command=lambda x=i+1: test(i)).grid()
                elif:
                    i == len(liste_ex)
                    self.destroy()
                else:
                    test(i+1)



