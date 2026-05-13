
somme = 0
compteur = 0
while True:
    n = float(input("Entrez un nombre (0 pour arrêter) : "))
    if n == 0:
        break
    somme += n
    compteur += 1

print(f"La somme est : {somme}")
print(f"Nombre de valeurs entrées : {compteur}")
