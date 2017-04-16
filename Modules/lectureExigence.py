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

def read_exigence(path, MgrExigences):
    file = open(path,"r")
    exigence = csv.reader(file, LectureDialect)
    def IsFonctional(x):
        if x[2:4] == 'F ':
            return 1
        return 0
    def IsMother(x):
        # s'arrête si la ligne n'est pas complée
        if len(x[(x.index(' ') + 1):]) > 1:
            return False
        return True
    for row in exigence:
        MgrExigences.create(row[1],row[2],row[3],espece = IsFonctional(row[0]),niveau =row[4], exigence_mere=IsMother(row[0]))
