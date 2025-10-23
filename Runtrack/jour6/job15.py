def get_length(liste):
    count = 0
    for _ in liste:
        count += 1
    return count

def my_round(number):
    entier = int(number)
    decimal = number - entier
    if decimal >= 0.5:
        return entier + 1
    else:
        return entier

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

liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

liste_arrondie = []
for x in liste:
    liste_arrondie.append(my_round(x))

liste_triee = sort_list(liste_arrondie)

print(liste_triee)
