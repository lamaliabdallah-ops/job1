def moyenne(note1, note2, note3):
    return (note1 + note2 + note3) / 3

# Saisie utilisateur
n1 = float(input("Note 1 : "))
n2 = float(input("Note 2 : "))
n3 = float(input("Note 3 : "))

moyenne_etudiant = moyenne(n1, n2, n3)
print(f"Moyenne : {moyenne_etudiant:.2f}")

if 15 <= moyenne_etudiant <= 20:
    print("Très bon élève")
elif 11 <= moyenne_etudiant <= 14:
    print("Bon élève")
elif 8 <= moyenne_etudiant <= 10:
    print("Élève moyen")
elif 0 <= moyenne_etudiant <= 7:
    print("Élève devant faire des efforts")
else:
    print("Note(s) incorrecte(s)")
