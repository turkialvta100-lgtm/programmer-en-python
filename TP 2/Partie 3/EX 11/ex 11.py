
mot_de_passe_secret = "python123"
tentatives = 3

while tentatives > 0:
    saisie = input("Entrez le mot de passe : ")
    if saisie == mot_de_passe_secret:
        print("Accès autorisé")
        break
    tentatives -= 1
    if tentatives > 0:
        print(f"Faux ! Il vous reste {tentatives} chances.")
    else:
        print("Compte bloqué")
