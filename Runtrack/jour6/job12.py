def get_length(liste):
    count = 0
    for _ in liste:
        count += 1
    return count

def sort_list(liste):
    i = 0
    while i < get_length(liste):
        j = i + 1
        while j < get_length(liste):
            if liste[j] < liste[i]:
                temp = liste[i]
                liste[i] = liste[j]
                liste[j] = temp
            j += 1
        i += 1
    return liste

ma_liste = [6, 2, 9, 1, 4]
liste_triee = sort_list(ma_liste)
print(liste_triee)
