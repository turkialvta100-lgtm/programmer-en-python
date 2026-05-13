
import calculatrice

menu = ["Addition", "Soustraction", "Multiplication", "Division"]
print(menu)
choix = input("Votre choix : ")
a = float(input("Nombre 1 : "))
b = float(input("Nombre 2 : "))

if choix == "Addition": print(calculatrice.addition(a, b))
elif choix == "Soustraction": print(calculatrice.soustraction(a, b))
elif choix == "Multiplication": print(calculatrice.multiplication(a, b))
elif choix == "Division": print(calculatrice.division(a, b))
else: print("Choix invalide")
