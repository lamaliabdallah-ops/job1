def afficher_tapis(n):
    for i in range(n + 1):
        ligne = ""
        for j in range(n+ 1):  
            if j ==n-i:
                ligne += " "
            else:
                ligne += "#"
        print(ligne)


if __name__ == "__main__":
    taille = 10
    afficher_tapis(taille)
