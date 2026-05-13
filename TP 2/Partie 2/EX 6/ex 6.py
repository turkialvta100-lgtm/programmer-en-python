
n = int(input("Entrez un nombre: "))
somme = 0

for i in range(1, n+1):
    if i % 2 == 0:
        somme += i

print("La somme des nombres pairs est:", somme)