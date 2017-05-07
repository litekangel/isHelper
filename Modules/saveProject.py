def trier_besoins(MgrBesoins):
    Stock = ['Besoin de service', "Beosin d'efficacité", "Besoin d'intéraction", "Besoin de sécurité",
             "Besoin de contrainte", "Besoin d'environnement"]
    liste_besoins =[[],[],[],[],[],[],[]]
    for elt in MgrBesoins.read():
        if elt.nature == None or elt.nature == '':
            liste_besoins[-1].append(elt)
        else:
            liste_besoins[Stock.index(elt.nature)].append(elt)
    return liste_besoins

def trier_exigences(MgrExigences):
    Stock = ['Exigence fonctionnelle', "Exigence d'efficacité", "Exigence d'intéraction", "Exigence de sécurité",
             "Exigence de contrainte", "Exigence d'environnement"]
    liste_exigences =[[],[],[],[],[],[],[]]
    for elt in MgrExigences.read():
        if elt.espece == None or elt.espece == '':
            liste_exigences[-1].append(elt)
        else:
            liste_exigences[Stock.index(elt.espece)].append(elt)
    return liste_exigences



def save_project(path, MgrBesoins, MgrExigences):
    file = open(path+".csv", "w")
    liste_besoins = trier_besoins(MgrBesoins)
    liste_exigences = trier_exigences(MgrExigences)
    for l_besoin in liste_besoins:
        if len(l_besoin) != 0:
            for besoin in l_besoin:
                ligne=str(besoin.nature)+';'+besoin.intitule+';'+str(besoin.origine)+'\n'
                file.write(ligne)
    for l_exigence in liste_exigences:
        if len(l_exigence) != 0:
            for exigence in l_exigence:
                ligne=str(exigence.espece)+';'+str(exigence.intitule)+';'+str(exigence.critere)+';'+str(exigence.niveau)+';'+str(exigence.origine)+';'+str(exigence.exigence_mere)+'\n'
                file.write(ligne)

