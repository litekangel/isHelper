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

def assigne_besoin(x):
    if x == 0:
        return 'Besoins de Service'
    elif x == 1:
        return "Beosin d'efficacité"
    elif x == 2 or x == 3:
        return "Besoin d'intéraction"
    elif 3<x<6:
        return "Besoin de sécurité"
    elif 5<x<8:
        return "Besoin d'environnement"
    else:
        return "Besoin de contrainte"

def read_besoin(path, MgrBesoins):
    Stock = ["Ser", "Eff", "IC ", "FH ", "SF ", "SI ", "Env", "TS ", "Rea", "MeS", "RdS", "Pro", "Reg", "CD "]
    file = open(path,"r")
    besoin = csv.reader(file, LectureDialect)
    elt = 1
    bp = 0
    def IsPrimaire(x):
        global bp
        if len(x[(x.index(' ') + 1):]) > 1:
            #si le csv est classé (logique et indispensable) le besoin dont il dépend est le primaire d'avant
            return bp
        bp = elt
        return None
    for row in besoin:
        #s'arrête si la ligne n'est pas complée
        if row[0] != '':
            pos=Stock.index(row[0][2:5])
            modele=assigne_besoin(pos)
            MgrBesoins.create(row[1], primaire = IsPrimaire(row[0]), origine=row[2], nature=modele)
            elt += 1
        else:
            break