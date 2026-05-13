notes = []

for i in range(3):
    note = float(input("Note : "))
    notes.append(note)

print("Liste :", notes)
print("Moyenne :", sum(notes) / len(notes))
print("Type :", type(notes))

# Ajouter nouvelle note
notes.append(float(input("Nouvelle note : ")))

print("Longueur :", len(notes))