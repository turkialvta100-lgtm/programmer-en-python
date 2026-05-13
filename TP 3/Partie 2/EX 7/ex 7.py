
compteur = 0

def incrementer():
    global compteur
    compteur += 1
    print(f"Intérieur : {compteur}")

incrementer()

print(f"Extérieur : {compteur}")
