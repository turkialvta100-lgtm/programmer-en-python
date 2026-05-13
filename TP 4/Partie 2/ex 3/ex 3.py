import json

etudiants = [
    {"nom": "Alice", "age": 20},
    {"nom": "Bob", "age": 22}
]

with open("etudiants.json", "w") as f:
        json.dump(etudiants, f, indent=4)

etudiants.append({"nom": "Bob", "age": 22})

with open("etudiants.json", "w") as f:
    json.dump(etudiants, f, indent=4)

print("JSON sauvegardé.")
    
