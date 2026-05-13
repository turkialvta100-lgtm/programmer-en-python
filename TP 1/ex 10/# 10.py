#Etape 
etudiants = []

etudiants.append("Ahmed")
etudiants.append("Sara")
etudiants.append("Youssef")

print(etudiants)

# Modifier 2ème étudiant
etudiants[1] = "Meryem"

print(etudiants)

# Supprimer dernier
etudiants.pop()
print(etudiants)

# Position premier étudiant
print("Index :", etudiants.index(etudiants[0]))


#Etape 2
moyen = {}

moyen["Ahmed"] = 14
moyen["Meryem"] = 16

# Modifier moyenne
moyen["Ahmed"] = 15

# Supprimer étudiant
del moyen["Meryem"]

# Afficher moyenne précise
print("Moyenne Ahmed :", moyen)