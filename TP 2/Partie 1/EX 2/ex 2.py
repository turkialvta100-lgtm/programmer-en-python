
a = float(input("Entrez le premier nombre: "))
b = float(input("Entrez le deuxième nombre: "))
c = float(input("Entrez le troisième nombre: "))

if a >= b and a >= c:
    print("Le plus grand nombre est:", a)
elif b >= a and b >= c:
    print("Le plus grand nombre est:", b)
else:
    print("Le plus grand nombre est:", c)