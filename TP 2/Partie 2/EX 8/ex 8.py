
phrase = input("Entrez une phrase: ")

voyelles = "aeiouyAEIOUY"
nb_voyelles = 0
nb_consonnes = 0
nb_espaces = 0

for c in phrase:
    if c in voyelles:
        nb_voyelles += 1
    elif c == " ":
        nb_espaces += 1
    elif c.isalpha():
        nb_consonnes += 1

print("Nombre total de caractères:", len(phrase))
print("Nombre de voyelles:", nb_voyelles)
print("Nombre de consonnes:", nb_consonnes)
print("Nombre d'espaces:", nb_espaces)
print("Majuscules:", phrase.upper())
print("Minuscules:", phrase.lower())