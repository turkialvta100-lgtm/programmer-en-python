


x = int(input("Donnez la valeur de x : "))
y = int(input("Donnez la valeur de y : "))

coord = (x, y)

print(type(coord))

# Tentative de modification
coord[0] = 10

#Une erreur de type TypeError s’affiche car un tuple est une structure de données immuable.
#Après sa création, il est impossible de modifier ses éléments, même s’ils proviennent de variables x et y.

#Le tuple est immuable, on ne peut pas modifier ses éléments après sa création.