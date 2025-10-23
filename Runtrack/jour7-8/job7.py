def my_sort(liste):
    n = len(liste)
    coups = 0
    echange = True

    # Continue tant qu'il y a eu des échanges
    while echange:
        echange = False
        for i in range(n - 1):
            if liste[i] > liste[i + 1]:
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
                coups += 1
                echange = True  

    print(f"Nombre total de coups nécessaires : {coups}")
    return liste

liste_a_trier = [5, 1, 4, 2, 8]
liste_triee = my_sort(liste_a_trier)
print("Liste triée :", liste_triee)
