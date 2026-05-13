
largeur = int(input("Entrez la largeur: "))
hauteur = int(input("Entrez la hauteur: "))

for i in range(hauteur):
    for j in range(largeur):
        print("*", end="")
    print()