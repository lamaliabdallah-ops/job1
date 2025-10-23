hauteur = int(input("Entrez la hauteur du triangle : "))

for i in range(hauteur+1):
    espaces_gauch = hauteur - i if i != hauteur else 0
    
    if i == hauteur:
        centre = "_" * ((i) * 2)
    else:
        centre = " " * ((i) * 2)
    
    ligne = " " * espaces_gauch + "/" + centre + "\\"
print(ligne )
