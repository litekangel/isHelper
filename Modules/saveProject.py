def save_project(path, MgrBesoins, MgrExigences):
    file = open(path+".csv", "w")
    for besoin in MgrBesoins.read():
        ligne=str(besoin.primaire)+';'+besoin.intitule+';'+str(besoin.origine)+'\n'
        file.write(ligne)
    for exigence in MgrExigences.read():
        ligne=str(exigence.espece)+';'+str(exigence.intitule)+';'+str(exigence.critere)+';'+str(exigence.niveau)+';'+str(exigence.origine)+';'+str(exigence.exigence_mere)+'\n'
        file.write(ligne)

