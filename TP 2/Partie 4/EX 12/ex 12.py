
notes = [12, 15, 8, 19, 10, 6, 14]
recherche = int(input("Saisir une note à rechercher : "))
trouvee = False

for n in notes:
    if n == recherche :
        print("Trouvée !")
        trouvee = True
        break

if not trouvee:
    print("Non trouvée") 