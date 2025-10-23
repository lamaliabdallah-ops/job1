def pair_ou_impair(nombre):
    if not isinstance(nombre, int) or nombre < 0:
        print("Veuillez entrer un entier positif")
        return
    if nombre % 2 == 0:
        print(f"{nombre} est pair")
    else:
        print(f"{nombre} est impair")

pair_ou_impair(7)
pair_ou_impair(7)
pair_ou_impair(7)
pair_ou_impair(3)
