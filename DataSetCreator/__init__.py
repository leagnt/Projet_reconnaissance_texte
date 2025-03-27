import random
import numpy as np


def choix_dataset(l_maj,l_min,chiffres,ponctu_simples,ponctu_complex) :#Prend en entrée les différents dataset [label,images] et renvoie un gros data set mélangé avec tout les caractères possibles
    X_train = np.array(l_maj.iloc[:, 1:])+np.array(l_min.iloc[:, 1:])+np.array(chiffres.iloc[:, 1:])+np.array(ponctu_simples.iloc[:, 1:])+np.array(ponctu_complex.iloc[:, 1:])
    Y_train = np.array(l_maj.iloc[:, 0])+np.array(l_min.iloc[:, 0])+np.array(chiffres.iloc[:, 0])+np.array(ponctu_simples.iloc[:, 0])+np.array(ponctu_complex.iloc[:, 0])

    indices = np.arange(len(X_train))
    np.random.shuffle(indices)
    x_shuffled = X_train[indices]
    y_shuffled = Y_train[indices]


    X_test = []
    Y_test = []

    return (x_shuffled,y_shuffled,X_test,Y_test)