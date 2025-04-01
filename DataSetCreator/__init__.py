import random
import numpy as np
import pandas as pd


#CHIFFRES
trainC_data = pd.read_csv('C:/Users/ghani/Documents/Desktop/TSE/Licence 3/S1/Projet Magistere/mnist_train.csv')
testC_data = pd.read_csv('C:/Users/ghani/Documents/Desktop/TSE/Licence 3/S1/Projet Magistere/mnist_test.csv')

XC_train = trainC_data.drop(labels=["label"], axis=1).to_numpy()  # convertir en numpy array
XC_test = testC_data.drop(labels=["label"], axis=1).to_numpy()

def transformation_chiffres(y):
    return np.where(y<=7,y+60,np.where(y==8,70,71))
YC_train=transformation_chiffres(trainC_data["label"].to_numpy())
YC_test=transformation_chiffres(testC_data["label"].to_numpy())

XC_train = XC_train / 255.0
XC_test = XC_test / 255.0


#LETTRES MAJ
trainLM_data = pd.read_csv('C:/Users/ghani/Documents/Desktop/TSE/Licence 3/S1/Projet Magistere/train.csv')
testLM_data = pd.read_csv('C:/Users/ghani/Documents/Desktop/TSE/Licence 3/S1/Projet Magistere/test.csv')
data_trainLM = trainLM_data.to_numpy()
data_testLM = testLM_data.to_numpy()

XLM_train = data_trainLM[:,1:]
YLM_train = data_trainLM[:,0]
XLM_test = data_testLM[:,1:]
YLM_test = data_testLM[:,0]

def transformation_lettresmaj(y):
    return ()
YLM_train=transformation_chiffres(trainLM_data["label"].to_numpy())
YLM_test=transformation_chiffres(testLM_data["label"].to_numpy())

XLM_train = XLM_train / 255.0
XLM_test = XLM_test / 255.0



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