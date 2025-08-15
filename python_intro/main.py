livre = "Gatsby le Magnifique"

print(livre)

nom = "AYENI"
prenom = "Georges"
age = 256

print(f"Bonjour, je m'appelle {prenom} {nom} et j'ai {age} ans.")

plateformes_sociales = ["Facebook", "Instagram", "Snapchat", "Twitter"]

print(plateformes_sociales[0])

print(len(plateformes_sociales))

nouvelle_campagne = {
"responsable_de_campagne": "Jeanne d'Arc",
"nom_de_campagne": "Campagne nous aimons les chiens",
"date_de_début": "01/01/2020",
"influenceurs_importants": ["@MonAmourDeChien", "@MeilleuresFriandisesPourChiens"]
}

print(nouvelle_campagne["responsable_de_campagne"])

infos_labradoodle = {
    "poids": "13 à 16 kg",
    "origine": "États-Unis"
}

infos_labradoodle['nexs'] = "Le nouveau nexus"

print(infos_labradoodle)

ensoleille = False
neige = True
if ensoleille:
    print("on va à la plage !")
elif neige:
    print("on fait un bonhomme de neige")
else:
    print("on reste à la maison !")

fruit = "pomme"
match fruit:
    case "pomme":
        print("J'aime les pommes !")
    case "banane":
        print("Je n'aime pas les bananes.")
    case "orange":
        print("Les oranges sont bonnes pour la santé.")
    case _:
        print("Je ne connais pas ce fruit.")

races_de_chien = ["golden retriever", "chihuahua", "terrier", "carlin"]
for chien in races_de_chien:
    print(chien)

for x in range(100):
    print(f"{x} bouteilles de bières au mur !")

capacite_maximale = 10
capacite_actuelle = 3
while capacite_actuelle < capacite_maximale:
    capacite_actuelle += 1

liste = [1, 2, 3, 4, 5]
# Boucle for sur la liste
for element in liste:
    if element == 3:
        # Si l'élément vaut 3, on passe à l'itération suivante sans exécuter le reste du code
        continue
    # Dans tous les autres cas, on exécute le reste du code
    print(element)

def afficher_message():
    print("Bonjour, comment ça va ?")

afficher_message()

def calculer_somme(a, b):
  resultat = a + b
  return resultat

print(calculer_somme(2, 3))

while True:
    try:
        x = int(input("Entrez un nombre entier : "))
        break
    except ValueError:
        print("Oops ! Ce n'est pas un nombre entier. Essayez encore...")