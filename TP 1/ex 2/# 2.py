nom = input("Nom : ")
age = int(input("Age : "))
filiere = input("Filière : ")
moyenne = float(input("Moyenne : "))

etudiant = {
    "nom": nom,
    "age": age,
    "filiere": filiere
}

# Ajouter moyenne
etudiant["moyenne"] = moyenne

# Modifier filière
etudiant["filiere"] = "Informatique"

# Affichage
print(etudiant)

for cle, valeur in etudiant.items():
    print(cle, ":", type(valeur))