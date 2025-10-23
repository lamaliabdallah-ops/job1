def get_length(liste):
    count = 0
    for _ in liste:
        count += 1
    return count

def remove_duplicates(liste):
    resultat = []
    for item in liste:
        existe = False
        for r in resultat:
            if r == item:
                existe = True
        if not existe:
            resultat.append(item)
    return resultat

liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
liste_sans_doublons = remove_duplicates(liste)
print(liste_sans_doublons)
