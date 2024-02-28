import joblib
import numpy as np
import csv , time
import sklearn

def verif(l):
    nchc = 0
    for i in l:
        if i == 1 :
            nchc +=1
    ncck = len(l)-nchc
    if nchc < ncck:
        return('CCK')
    else :
        return('CHC')

def lire_fichier_csv(nom_fichier):
    lignes = []
    with open(nom_fichier, 'r') as fichier:
        lecteur_csv = csv.reader(fichier)
        for ligne in lecteur_csv:
            lignes.append(ligne)
    return lignes

def lire_fichier():
    while True :
        try :
            path = input("INSERT CSV FILE PATH ")
            data = lire_fichier_csv(path)
            data = data[1:]
            break
        except :
            print("PATH IS NOT VALID, PLEASE TRY AGAIN")
    return(data)

def reshape_data(data):
    X = []
    for i in range(len(data)):
        data[i] = data[i][39:-2]
        for j in range(len(data[i])):
            data[i][j] = float(data[i][j])

    for i in range(len(data)-1, 0,-1) :
        for j in range(0,i) :
            a = np.array(data[i]) - np.array(data[j])
            X.append(list(a))
    return(X)

data = lire_fichier()

X = reshape_data(data)

# Charger le modèle à partir du fichier
clf_loaded = joblib.load('D:\projects python pycharm\Diagnostic cancer du foie\output\predict_svm_executable\modele_svm.joblib')

# Prédire les classes pour de nouvelles données
Y_pred = clf_loaded.predict(X)

cancer = verif(Y_pred)

print(f'>>>>> TYPE DE CANCER  : {cancer} <<<<<')

time.sleep(10)