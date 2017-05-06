# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""


class Besoin:
    def __init__(self, id_besoin, intitule, primaire=False, origine=None, nature=None):
        self.id_besoin = id_besoin
        self.primaire = primaire  # besoin primaire
        self.intitule = intitule
        self.origine = origine
        self.nature = nature

    def id_besoin(self):
        return self.id_besoin

    def primaire(self):
        return self.primaire

    def intitule(self):
        return self.intitule


class Exigence:

    def __init__(self, idex, intitule, critere, origine=None, espece = 0,niveau=None, exigence_mere = None):
        self.idex = idex
        self.exigence_mere = exigence_mere
        self.critere = critere
        self.espece = espece
        #Pour une exigence fonctionnelle vaut 1 sinon vaut 0
        self.origine = origine
        #Le besoin dont découle l'exigence
        self.intitule = intitule
        self.niveau = niveau

    def __str__(self):
        espece = "non fonctionnelle"
        if self.espece == 1:
            espece = "fonctionnelle"
        return "L'exigence N{} {} est une exigence {} d'intitulé {} ".format(self.idex, self.critere, espece,
                                                                             self.intitule)


class Piece():
    def __init__(self, id_piece, nom, couleur, quantite):
        self._nom = nom
        self.couleur = couleur
        self.id_piece = id_piece
        self.quantite = quantite


class Nomenclature():
    def __init__(self, id_piece, nom, couleur, quantite):
        self._nom = nom
        self.couleur = couleur
        self.id_piece = id_piece
        self.quantite = quantite



















