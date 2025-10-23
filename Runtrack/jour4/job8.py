def saison_produits(type, saison):
    type = type.lower()
    saison = saison.lower()
    if type == "fruits":
        if saison == "été":
            print("orange, mandarine et kiwi")
        elif saison == "été":
            print("Poire, fraise, cassis")
    elif type == "légume":
        if saison == "hiver":
            print("carotte, topinambour, endive")
        elif saison == "été":
            print("artichaut, aubergine, navet")
    else:
        print("Type ou saison non reconnu")

saison_produits("fruits", "hiver")
saison_produits("fruits", "été")
saison_produits("légume", "hiver")
saison_produits("légume", "été")
