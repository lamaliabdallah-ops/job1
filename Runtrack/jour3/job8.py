a = float(input("Entrez la longueur a : "))
b = float(input("Entrez la longueur b : "))
c = float(input("Entrez la longueur c : "))

def est_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

def est_rectangle(a, b, c):
   
    x, y, z = sorted([a, b, c])
    return abs(x**2 + y**2 - z**2) < 1e-9

def est_equilateral(a, b, c):
    return a == b == c

def est_isocèle(a, b, c):
    return a == b or b == c or a == c

if est_triangle(a, b, c):
    print("Le triangle est constructible.")
    
    rectangle = est_rectangle(a, b, c)
    equilateral = est_equilateral(a, b, c)
    isocèle = est_isocèle(a, b, c)
    
    if equilateral:
        print("Le triangle est équilatéral.")
    else:
        if rectangle:
            print("Le triangle est rectangle.", end=' ')
        if isocèle:
            print("Le triangle est isocèle.")
        elif not rectangle:
            print("Le triangle est quelconque.")
else:
    print("Les longueurs ne permettent pas de construire un triangle.")
