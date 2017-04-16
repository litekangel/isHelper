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

def read_besoin(path, MgrBesoins):
    file = open(path,"r")
    besoin = csv.reader(file, LectureDialect)
    def IsPrimaire(x):
        print(row)
        if len(x[(x.index(' ') + 1):]) > 1:
            return False
        return True
    for row in besoin:
        #s'arrête si la ligne n'est pas complée
        if row[0] != '':
            MgrBesoins.create(row[1], primaire = IsPrimaire(row[0]), origine=row[2])
        else:
            break