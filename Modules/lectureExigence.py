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


def assigne_ex(x):
    if x == 0:
        return 'Exigence fonctionnelle'
    elif x == 1:
        return "Exigence d'efficacité"
    elif x == 2 or x == 3:
        return "Exigence d'intéraction"
    elif 3<x<6:
        return "Exigence de sécurité"
    elif 5<x<8:
        return "Exigence d'environnement"
    else:
        return "Exigence de contrainte"

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

def read_exigence(path, MgrExigences, MgrBesoins):
    Stock = ["F  ", "Eff", "IC ", "FH ", "SF ", "SI ", "Env", "TS ", "Rea", "MeS", "RdS", "Pro", "Reg", "CD "]
    Stockb = ["Ser ", "Eff", "IC ", "FH ", "SF ", "SI ", "Env", "TS ", "Rea", "MeS", "RdS", "Pro", "Reg", "CD "]
    file = open(path,"r")
    exigence = csv.reader(file, LectureDialect)
    elt = 1
    bp = 0
    liste_bp = {'Besoin de service': [], "Beosin d'efficacité":[], "Besoin d'intéraction":[], "Besoin de sécurité":[],
                 "Besoin de contrainte":[], "Besoin d'environnement":[]}
    for elt in MgrBesoins.read():
        if elt.primaire == None or elt.primaire == '':
            liste_bp[elt.nature].append(elt)
    def IsMother(x):
        global bp
        if len(x[(x.index(' ') + 1):]) > 1:
            # si le csv est classé (logique et indispensable) le besoin dont il dépend est le primaire d'avant
            return bp
        bp = elt
        return None
    def IsBesoin(x, y):
        if x != '' or x != ' ':
            bes = len(x[(x.index('.') + 3)])
            var = Stockb.index(bes)
            for i in liste_bp.values:
                for elt in i:
                    if elt.intitule == y:
                        return elt.id_besoin
        return None

    for row in exigence:
        pos = Stock.index(row[0][2:5])
        modele = assigne_ex(pos)
        MgrExigences.create(row[1], row[2], espece=modele, origine=IsBesoin(row[2], row[1]), niveau =row[4], exigence_mere=IsMother(row[0]))
