# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 07:47:22 2016

@author: 2016-0687
12/12/16: 
Divers raccords sur la nomenclature
Conception et réalisation d'un algorithme de validation d'exigences
05/12/17:


"""
import sqlite3 as sql

from classes import *


class BesoinsMgr():
    def __init__(self, db):
        self.db = db

    def connect(self):
        return sql.connect(self.db)

    def create(self, intitule, primaire=False, origine=False):
        db_connect = self.connect()
        cursor = db_connect.cursor()
        cursor.execute("""INSERT INTO besoins (intitule,primaire,origine) VALUES(?,?,?)""",
                       (intitule, primaire, origine))
        id_besoin = cursor.lastrowid
        db_connect.commit()
        db_connect.close()
        return Besoin(id_besoin, intitule, primaire)

    def delete(self, besoin):
        if (isinstance(besoin, Besoin)):
            db_connect = self.connect()
            cursor = db_connect.cursor()
            cursor.execute("""DELETE * FROM besoins WHERE id_besoin = ?""", (besoin.id_besoin))
            db_connect.commit()
            db_connect.close()

    def read(self, id_besoin=None):
        db_connect = self.connect()
        print(db_connect)
        if (id_besoin):
            cursor = db_connect.cursor()
            besoin = cursor.execute("""SELECT * FROM besoins WHERE id_besoin = ?""", (str(id_besoin)))
            data = cursor.fetchone()
            db_connect.commit()
            db_connect.close()
            return Besoin(data[0], data[1], data[2])
        cursor = db_connect.cursor()
        q = cursor.execute("""SELECT * FROM besoins""")
        besoins = cursor.fetchall()
        for i, besoin in enumerate(besoins):
            besoins[i] = Besoin(besoin[0], besoin[1], besoin[2])
        print(besoins)
        db_connect.commit()
        db_connect.close()
        return besoins

    def update(self, besoin):
        if (isinstance(besoin, Besoin)):
            db_connect = self.connect()
            cursor = db_connect.cursor()
            cursor.execute("""UPDATE besoins SET intitule = ?, primaire=? WHERE id_besoin = ?""",
                           (besoin.intitule, besoin.primaire, besoin.id_besoin))
            db_connect.commit()
            db_connect.close()


class PieceMgr():
    def __init__(self, db):
        self.db = db

    def connect(self):
        return sql.connect(self.db)

    def create(self, nom_piece, couleur):
        db_connect = self.connect()
        cursor = db_connect.cursor()
        cursor.execute("""INSERT INTO pieces (nom_piece,couleur) VALUES(:nom,:couleur)""",
                       {nom: nom_piece, couleur: couleur})
        id_piece = cursor.lastrowid
        db_connect.commit()
        db_connect.close()
        return Exigence(id_piece, nom_piece, couleur)

    def delete(self, piece):
        if (isinstance(piece, Piece)):
            db_connect = self.connect()
            cursor = db_connect.cursor()
            cursor.execute("""DELETE * FROM pieces WHERE id_piece = ?""", (piece.id_piece()))
            db_connect.commit()
            db_connect.close()

    def read(self, id_piece=None):
        db_connect = self.connect()
        if (id_piece):
            cursor = db_connect.cursor()
            piece = cursor.execute("""SELECT * FROM pieces WHERE id_piece = ?""", (id_piece))
            db_connect.commit()
            db_connect.close()
            return Piece(piece[0], piece[1], piece[2])
        cursor = db_connect.cursor()
        q = cursor.execute("""SELECT * FROM pieces""")
        pieces = cursor.fetchall()
        db_connect.commit()
        db_connect.close()
        for i, piece in enumerate(pieces):
            pieces[i] = Piece(piece[0], piece[1], piece[2])
        return pieces

    def update(self, piece):
        if (isinstance(piece, Piece)):
            db_connect = self.connect()
            cursor = db_connect.cursor()
            cursor.execute(
                """UPDATE pieces SET nom_piece = ?, couleur = ? WHERE id_piece = ?""",
                (piece.nom_piece, piece.couleur, piece.id_piece))
            db_connect.commit()
            db_connect.close()


class ExigencesMgr():
    def __init__(self, db):
        self.db = db

    def connect(self):
        return sql.connect(self.db)

    def create(self, intitule, critere, besoin, espece=0, niveau=None, exigence_mere=1):
        db_connect = self.connect()
        cursor = db_connect.cursor()
        cursor.execute("""INSERT INTO exigences
        (critere,niveau,intitule,besoin,espece,exigence_mere)
        VALUES (?,?,?,?,?,?)""",
                       (critere, niveau, intitule, besoin, espece, exigence_mere))
        idex = cursor.lastrowid
        db_connect.commit()
        db_connect.close()
        return Exigence(idex, intitule, critere, besoin, espece, niveau, exigence_mere)

    def delete(self, exigence):
        if (isinstance(exigence, Exigence)):
            db_connect = self.connect()
            cursor = db_connect.cursor()
            cursor.execute("""DELETE * FROM exigences WHERE idex = ?""", (exigence.idex()))
            db_connect.commit()
            db_connect.close()

    def read(self, idex=None):
        db_connect = self.connect()
        if (idex):
            cursor = db_connect.cursor()
            exigence = cursor.execute("""SELECT * FROM exigences
            WHERE idex = ?""", (str(idex)))
            exigence = list(exigence)
            exigence = list(exigence[0])
            print(exigence)
            db_connect.commit()
            db_connect.close()
            return Exigence(int(exigence[0]), exigence[3], exigence[4], exigence[5], exigence[6], exigence[9])
        cursor = db_connect.cursor()
        exigences = cursor.execute("""SELECT * FROM exigences""")
        exigences = list(exigences)
        for i, exigence in enumerate(exigences):
            exigence = list(exigence)
            exigences[i] = Exigence(int(exigence[0]), exigence[3], exigence[4], exigence[5], exigence[6], exigence[9])
            print(exigences[i])
            print('\n')
        db_connect.commit()
        db_connect.close()
        return exigences

    def update(self, exigence):
        if (isinstance(exigence, Exigence)):
            db_connect = self.connect()
            cursor = db_connect.cursor()
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
            db_connect.commit()
            db_connect.close()

    def conclure(self, idex, conclusion):
        db_connect = self.connect()
        cursor = db_connect.cursor()
        cursor.execute("""UPDATE exigences SET conclusion = ? WHERE idex = ?""", (conclusion, idex))
        db_connect.commit()
        db_connect.close()

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

        def connect(self):
            return sql.connect(self.db)

        def read(self):
            db_connect = self.connect()
            cursor = db_connect.cursor()
            cursor.execute("""SELECT * FROM error""")

            db_connect.commit()
            db_connect.close()
            # to continue...

        def create(self, intitule, type):
            db_connect = self.connect()
            cursor = db_connect.cursor()
            cursor.execute("""INSERT INTO errors SET intitule= ?, type = ?""", (intitule, type))
            db_connect.commit()
            db_connect.close()

        def delete(self, id_error):
            db_connect = self.connect()
            cursor = db_connect.cursor()
            cursor.execute("""DELETE * FROM errors  WHERE id_error = ?""", (id_error))
            db_connect.commit()
            db_connect.close()

        def delete(self, error):
            db_connect = self.connect()
            cursor = db_connect.cursor()
            cursor.execute("""UPDATE errors SET intitule = ?,type=? WHERE id_error = ?""",
                           (error.intitule, error.type, error.id_error))
            db_connect.commit()
            db_connect.close()
