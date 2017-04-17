# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 07:47:22 2016

@author: 2016-0687
12/12/16: 
Divers raccords sur la nomenclature
Conception et réalisation d'un algorithme de validation d'exigences
05/12/17:


"""
from classes import *


class BesoinsMgr():
    def __init__(self, db):
        self.db = db
        self.cursor = db.cursor()

    def create(self, intitule, primaire=False, origine=False):
        cursor = self.db.cursor()
        cursor.execute("""INSERT INTO besoins (intitule,primaire,origine) VALUES(?,?,?)""",
                       (intitule, primaire, origine))
        id_besoin = cursor.lastrowid
        cursor.close()
        return Besoin(id_besoin, intitule, primaire)

    def delete(self, besoin):
        if (isinstance(besoin, Besoin)):
            cursor = self.db.cursor()
            cursor.execute("""DELETE * FROM besoins WHERE id_besoin = ?""", (besoin.id_besoin))
            cursor.close()

    def read(self, id_besoin=None):
        if (id_besoin):
            cursor = self.db.cursor()
            besoin = cursor.execute("""SELECT * FROM besoins WHERE id_besoin = ?""", (str(id_besoin)))
            data = cursor.fetchone()
            return Besoin(data[0], data[1], data[2])
        cursor = self.db.cursor()
        q = cursor.execute("""SELECT * FROM besoins""")
        besoins = cursor.fetchall()
        for i, besoin in enumerate(besoins):
            besoins[i] = Besoin(besoin[0], besoin[1], besoin[2])
        print(besoins)
        cursor.close()
        return besoins

    def update(self, besoin):
        if (isinstance(besoin, Besoin)):
            cursor = self.db.cursor()
            cursor.execute("""UPDATE besoins SET intitule = ?, primaire=? WHERE id_besoin = ?""",
                                (besoin.intitule, besoin.primaire, besoin.id_besoin))
            cursor.close()


class PieceMgr():
    def __init__(self, db):
        self.db = db

    def create(self, nom_piece, couleur):
        cursor = self.db.cursor()
        cursor.execute("""INSERT INTO pieces (nom_piece,couleur) VALUES(:nom,:couleur)""",
                            {nom: nom_piece, couleur: couleur})
        id_piece = cursor.lastrowid
        cursor.close()
        return Exigence(id_piece, nom_piece, couleur)

    def delete(self, piece):
        if (isinstance(piece, Piece)):
            cursor = self.db.cursor()
            cursor.execute("""DELETE * FROM pieces WHERE id_piece = ?""", (piece.id_piece()))
            cursor.close()

    def read(self, id_piece=None):
        if (id_piece):
            cursor = self.db.cursor()
            piece = cursor.execute("""SELECT * FROM pieces WHERE id_piece = ?""", (id_piece))
            cursor.close()
            return Piece(piece[0], piece[1], piece[2])
        cursor = self.db.cursor()
        q = cursor.execute("""SELECT * FROM pieces""")
        pieces = cursor.fetchall()
        cursor.close()
        for i, piece in enumerate(pieces):
            pieces[i] = Piece(piece[0], piece[1], piece[2])
        return pieces

    def update(self, piece):
        if (isinstance(piece, Piece)):
            cursor = self.db.cursor()
            cursor.execute(
                """UPDATE pieces SET nom_piece = ?, couleur = ? WHERE id_piece = ?""",
                (piece.nom_piece, piece.couleur, piece.id_piece))
            cursor.close()


class ExigencesMgr():
    def __init__(self, db):
        self.db = db
        self.cursor = db.cursor()

    def create(self, intitule, critere, besoin, espece=0, niveau=None, exigence_mere=1):
        cursor = self.db.cursor()
        cursor.execute("""INSERT INTO exigences
        (critere,niveau,intitule,besoin,espece,exigence_mere)
        VALUES (?,?,?,?,?,?)""",
                            (critere, niveau, intitule, besoin, espece, exigence_mere))
        idex = cursor.lastrowid
        cursor.close()
        return Exigence(idex, intitule, critere, besoin, espece, niveau, exigence_mere)

    def delete(self, exigence):
        if (isinstance(exigence, Exigence)):
            cursor = self.db.cursor()
            cursor.execute("""DELETE * FROM exigences WHERE idex = ?""", (exigence.idex()))
            cursor.close()

    def read(self, idex=None):
        if (idex):
            cursor = self.db.cursor()
            exigence = cursor.execute("""SELECT * FROM exigences
            WHERE idex = ?""", (str(idex)))
            exigence = list(exigence)
            exigence = list(exigence[0])
            print(exigence)

            return Exigence(int(exigence[0]), exigence[3], exigence[4], exigence[5], exigence[6], exigence[9])
        cursor = self.db.cursor()
        exigences = cursor.execute("""SELECT * FROM exigences""")
        exigences = list(exigences)
        for i, exigence in enumerate(exigences):
            exigence = list(exigence)
            exigences[i] = Exigence(int(exigence[0]), exigence[3], exigence[4], exigence[5], exigence[6], exigence[9])
            print(exigences[i])
            print('\n')
        cursor.close()
        return exigences

    def update(self, exigence):
        if (isinstance(exigence, Exigence)):
            cursor = self.db.cursor()
            cursor.execute("""UPDATE exigences
            SET critere = ?,
            niveau = ?,
            intitule = ?,
            espece = ?,
            besoin= ?,
            exigence_mere = ?
            WHERE idex = ?""",
                                (exigence.critere, exigence.niveau, exigence.intitule, exigence.espece, exigence.besoin,
                                 exigence.exigence_mere, exigence.idex))
            cursor.close()

    def conclure(self, idex, conclusion):
        cursor = self.db.cursor()
        cursor.execute("""UPDATE exigences SET conclusion = ? WHERE idex = ?""", (conclusion, idex))
        cursor.close()

    def validerExigences(self, exigence=None):
        if isinstance(exigence, Exigence):
            conclusion = 0
            # 0: Exigence non vérifiée
            # 1: Exigence vérifiée
            # Zero tolérance, on veut que le niveau réel soit le niveau de test
            if exigence.qualite() == 0:
                if (exigence.niveauReel() == exigence.niveau()):
                    conclusion = 1
            if exigence.qualite() == 1:
                if (exigence.niveauReel() >= exigence.niveau()):
                    conclusion = 1
            if exigence.qualite() == 2:
                if (exigence.niveauReel() <= exigence.niveau()):
                    conclusion = 1
            self.conclure(exigence.idex(), conclusion)
            return True
        exigences = self.read()
        for exigence in exigences:
            self.validerExigences(exigence)

    def classerExigences(self):
        exigences = list(self.read())
        # On trouve les étages du graphe
        niveaux = []
        niveau0 = []
        for exigence in exigences:
            if exigence.exigenceMere == None:
                niveau0.append(exigence.idex)
                exigences.remove(exigence)
        niveaux.append(niveau0)
        hierarchie = self.hierarchie(exigences, niveaux)

        return hierarchie

    def hierarchie(self, exigences, niveaux):
        if (len(exigences) == 0):
            return niveaux
        else:
            meres = niveaux[-1]
            niveau = []
            for exigence in exigences:
                if exigence.exigenceMere in meres:
                    niveau.append(exigence)
                    exigences.remove(exigence)
            niveaux.append(niveau)
            self.hierarchie(exigences, niveaux)

    class ErrorMgr():
        def __init__(self, db):
            self.db = db
            self.cursor = db.cursor

        def read(self):
            cursor = self.db.cursor()
            cursor.execute("""SELECT * FROM error""")

            cursor.close()
            # to continue...

        def create(self, intitule, type):
            cursor = self.db.cursor()
            cursor.execute("""INSERT INTO errors SET intitule= ?, type = ?""", (intitule, type))
            cursor.close()

        def delete(self, id_error):
            cursor = self.db.cursor()
            cursor.execute("""DELETE * FROM errors  WHERE id_error = ?""", (id_error))
            cursor.close()

        def delete(self, error):
            cursor = self.db.cursor()
            cursor.execute("""UPDATE errors SET intitule = ?,type=? WHERE id_error = ?""",
                               (error.intitule, error.type, error.id_error))
            cursor.close()
