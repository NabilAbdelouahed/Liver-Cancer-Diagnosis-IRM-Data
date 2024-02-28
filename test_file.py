import csv

def lire_fichier_csv(nom_fichier):
    lignes = []
    with open(nom_fichier, 'r') as fichier:
        lecteur_csv = csv.reader(fichier)
        for ligne in lecteur_csv:
            lignes.append(ligne)
    return lignes

# Utilisation de la fonction pour lire un fichier CSV et stocker les lignes dans une liste
fichier_csv = 'voitures.csv'
lignes_csv = lire_fichier_csv(fichier_csv)

print(lignes_csv)