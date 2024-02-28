from sklearn import svm
import joblib
import main2 as m
import numpy as np

def verif(l1,l2):
    error = []
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            error.append(i)
    return(error)

train_percentage = 80
mat = m.create_mat()
X_test , Y_test = m.create_vect_x_y(mat)
Y_test = m.etiquette_y(Y_test)
n = (train_percentage*len(X_test))//100
X_test , Y_test = X_test[  : ] , Y_test[  : ]

# Charger le modèle à partir du fichier
clf_loaded = joblib.load('modele_svm.joblib')

# Prédire les classes pour de nouvelles données
Y_pred = clf_loaded.predict(X_test)
# Prédire les distances signées
decision_values = clf_loaded.decision_function(X_test)
decision_values = abs(np.array(decision_values))

maxi = max(abs(decision_values))

taux_de_confiance = []
for value in decision_values :
    taux_de_confiance.append(round(value,1)*100/maxi)
error = verif(Y_test,Y_pred)

print(len(error))
print(len(Y_test))
print(taux_de_confiance)
print(min(taux_de_confiance))

for i in error :
    print(Y_test[i])