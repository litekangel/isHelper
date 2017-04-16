def save_project(path, MgrBesoins, MgrExigences):
    file = open(path+".csv", "w")
    for besoin in MgrBesoins.read():
        ligne=besoin.primaire+';'+besoin.intitule+';'+besoin.origine
        file.write(ligne)
    for exigence in MgrExigences.read():
        ligne=exigence.espece+';'+exigence.intitule+';'+exigence.critere+';'+exigence.niveau+';'+exigence.origine+';'+exigence.exigence_mere
        file.write(ligne)

