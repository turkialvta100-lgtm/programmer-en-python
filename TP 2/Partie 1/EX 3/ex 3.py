n1 = float(input("Entrez la note 1: "))
n2 = float(input("Entrez la note 2: "))
n3 = float(input("Entrez la note 3: "))

moyenne = (n1 + n2 + n3) / 3

print("La moyenne est:", moyenne)

if moyenne < 0 or moyenne > 20:
    print("Erreur: note invalide")

elif moyenne < 10:
    print("Mention: Insuffisant")

elif moyenne < 12:
    print("Mention: Passable")

elif moyenne < 14:
    print("Mention: Assez bien")

elif moyenne < 16:
    print("Mention: Bien")

elif moyenne < 18:
    print("Mention: Très bien")

else:
    print("Mention: Excellent")