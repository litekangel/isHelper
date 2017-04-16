import csv

class LectureDialect(csv.Dialect):
    #Séparateur de champ
    delimiter = ";"
    #Séparateur de chaîne
    quotechar = None
    #Gestion du séparateur dans les chaînes
    escapechar = None
    doublequote = None
    #Fin de ligne
    lineterminator = "\r\n"
    #Ajout automatique du séparateur de chaîne
    quoting = csv.QUOTE_NONE
    skipinitialspace = False

def read_nomenclature(path, MgrNomenclature):
    file = open(path, "r")
    nomenclature = csv.reader(file, LectureDialect)
    for row in nomenclature:
        # s'arrête si la ligne n'est pas complée
        if row[0] != '':
            MgrNomenclature.create(row[4], row[2])
        else:
            break
