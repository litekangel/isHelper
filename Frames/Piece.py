import tkinter as tk
from tkinter.ttk import *

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
            print('mmmmm')
            print(int(Select.get()[:Select.get().index('.')]))
            self.MgrPieces.delete(int(Select.get()[:Select.get().index('.')]))
            self.destroy()
        Select = tk.StringVar()
        Stock = list()
        for i in self.MgrPieces.read():
            Stock.append(str(i.id_piece) + '. ' + i.nom)
        ListeElt = Combobox(self, textvariable=Select, values=Stock, state='readonly')
        ListeElt.grid()
        tk.Button(self, text="Valider", command=Valider).grid()

    def Modifier_Piece(self):
        def Update():
            pie=self.MgrPieces.read(Select.get()[:Select.get().index('.')])
            # Mise à jour des variables
            pie.nom = self.intitule_piece.get()
            pie.couleur = self.couleur.get()
            self.MgrPieces.update(pie)
            self.destroy()

        def Valider():
            for elt in self.winfo_children():
                elt.destroy()
            tk.Label(self, text='Nom de la pièce :').grid()
            tk.Entry(self, textvariable=self.intitule_piece, width=50).gid()
            tk.Label(self, text='Couleur :').grid()
            tk.Entry(self, textvariable=self.couleur, width=50).grid()
            tk.Button(self, text="Valider", command=Update).grid()
        tk.Label(self, text="Identifiant de la pièce à modifier: ").grid()
        Select = tk.StringVar()
        Stock = list()
        for i in self.MgrPieces.read():
            Stock.append(str(i.id_piece) + '. ' + i.nom)
        ListeElt = Combobox(self, textvariable=Select, values=Stock, state='readonly')
        ListeElt.grid()
        tk.Button(self, text="Valider", command=Valider).grid()