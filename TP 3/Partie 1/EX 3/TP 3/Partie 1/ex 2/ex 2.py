with open("etudiants.txt", "r") as f:
    contenu = f.read()
    print(contenu)


with open("etudiants.txt", "r") as f:
    premiere_ligne = f.readline()
    print(premiere_ligne.strip())


