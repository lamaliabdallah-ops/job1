chaine = "abcdefghijklmnopqrstuvwxyz" * 10 

index = 0
ligne = 1
longueur = len(chaine)

while index + ligne <= longueur:
    print(chaine[index:index+ligne])
    index += ligne
    ligne += 1
