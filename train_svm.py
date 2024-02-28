from sklearn import svm
import joblib
import main2 as m

train_percentage = 80

mat = m.create_mat()
X_train , Y_train = m.create_vect_x_y(mat)
Y_train = m.etiquette_y(Y_train)
n = (train_percentage*len(X_train))//100
X_train , Y_train = X_train[ :n] , Y_train[ : n ]


# Créer un classifieur SVM
clf = svm.SVC()

# Entraîner le classifieur SVM
clf.fit(X_train, Y_train)

# Enregistrer le modèle dans un fichier binaire
joblib.dump(clf, 'modele_svm.joblib')




