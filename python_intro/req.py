# import requests
# from bs4 import BeautifulSoup

# url = "https://www.gov.uk/search/news-and-communications"
# page = requests.get(url)

# # Voir le code html source
# # print(page.content)

# with open("index.html", "r") as file:
#    soup = BeautifulSoup(file.read(), 'html.parser')
#    print(soup.find("h1").string)

import csv

with open('data.csv') as fichier_csv:
   reader = csv.DictReader(fichier_csv, delimiter=',')
   for ligne in reader:
      print(ligne['nom'] + " travaille en tant que " + ligne['metier'] + " et sa couleur préférée est " + ligne['couleur_preferee'])
      
# Créer une liste pour les en-têtes
en_tete = ["titre", "description"]

# Créer un nouveau fichier pour écrire dans le fichier appelé « data.csv »
with open('data.csv', 'w') as fichier_csv:
    # Créer un objet writer (écriture) avec ce fichier
    writer = csv.writer(fichier_csv, delimiter=',')
    writer.writerow(en_tete)
    # Parcourir les titres et descriptions - zip permet d'itérer sur deux listes ou plus à la fois
    for titre, description in zip(titres, descriptions):
        # Créer une nouvelle ligne avec le titre et la description à ce moment de la boucle
        ligne = [titre, description]
        writer.writerow(ligne)