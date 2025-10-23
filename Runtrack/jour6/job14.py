def get_length(chaine):
    count = 0
    for _ in chaine:
        count += 1
    return count

def my_long_word(n, chaine):
    mot = ""
    resultat = ""
    i = 0
    while i < get_length(chaine):
        if chaine[i] != " ":
            mot += chaine[i]
        else:
            if get_length(mot) > n:
                resultat += mot + " "
            mot = ""
        i += 1

    if get_length(mot) > n:
        resultat += mot

    return resultat.strip()

texte = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
resultat = my_long_word(3, texte)
print(resultat)
