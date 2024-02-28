from sklearn import svm
import matplotlib.pyplot as plt
import numpy as np
import main2 as m

donnees1_abscisses = [3, 2, 3, 4]
donnees1_ordonnees = [5, 6, 7, 8]

donnees2_abscisses = [3, 4, 5, 6]
donnees2_ordonnees = [3, 2, 9,10]

donnees = [(donnees1_abscisses[i], donnees1_ordonnees[i]) for i in range(len(donnees1_abscisses))]
donnees += [(donnees2_abscisses[i], donnees2_ordonnees[i]) for i in range(len(donnees2_abscisses))]

etiquettes = [0] * len(donnees1_abscisses) + [1] * len(donnees2_abscisses)

# noyeau gaussien
classificateur = svm.SVC(kernel='rbf')

classificateur.fit(donnees, etiquettes)

# Créer une grille de points dans l'espace des abscisses et ordonnées
x_min, x_max = min(donnees1_abscisses + donnees2_abscisses), max(donnees1_abscisses + donnees2_abscisses)
y_min, y_max = min(donnees1_ordonnees + donnees2_ordonnees), max(donnees1_ordonnees + donnees2_ordonnees)
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))

# Faire des prédictions pour chaque point de la grille
Z = classificateur.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Afficher les données et la séparation
plt.contourf(xx, yy, Z, alpha=0.8)
plt.scatter(donnees1_abscisses, donnees1_ordonnees, c='red', label='Donnees 1')
plt.scatter(donnees2_abscisses, donnees2_ordonnees, c='blue', label='Donnees 2')
plt.xlabel('Abscisses')
plt.ylabel('Ordonnees')
plt.legend()
plt.show()

new_data = [(2.5, 3.5), (6.5, 7.5)]
predicted_labels = svm_model.predict(new_data)
# Créer un maillage pour visualiser la frontière de décision
x_min, x_max = min(x1 + x2) - 1, max(x1 + x2) + 1
y_min, y_max = min(y1 + y2) - 1, max(y1 + y2) + 1
h = 0.02  # Pas de la grille
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# Prédire la classe pour chaque point du maillage
Z = svm_model.predict(np.c_[xx.ravel(), yy.ravel()])

# Mettre les résultats dans un plot coloré
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)

# Afficher les données d'entraînement
plt.scatter(x1, y1, color='red', label='Data 1')
plt.scatter(x2, y2, color='blue', label='Data 2')

# Afficher les données de test
plt.scatter([data[0] for data in new_data], [data[1] for data in new_data], color='green', label='New Data')

plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('SVM Classification')
plt.show()
