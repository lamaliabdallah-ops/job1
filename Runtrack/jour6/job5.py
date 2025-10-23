L = [1,2,3,4,5]

print("Deuxième valeur :", L[1])

def remplacer_par_somme_voisines(liste):
    liste[3] = liste[2] + liste[4]

remplacer_par_somme_voisines(L)

print("Liste après modification :", L)

print("Dernière valeur :", L[-1])
