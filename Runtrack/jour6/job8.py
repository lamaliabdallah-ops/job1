L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

somme_paire = 0
for nombre in L:
    if nombre % 2 == 0:
        somme_paire += nombre

print("Somme des nombres pairs :", somme_paire)
