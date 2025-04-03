import numpy as np
import pandas as pd
import os
import sys
import cv2


current_dir=os.path.dirname(os.path.abspath(__file__))
project_root=os.path.abspath(os.path.join(current_dir,".."))
sys.path.append(project_root)
from DataSetCreator.handwritting.extract import bdd
print(bdd,"h")
class Multicouches:


    def __init__(self, couches, apprentissage):
        self.apprentissage = apprentissage
        self.couches = couches

        #Méthode xavier plus utilie qaund le nopmbre de couches est hautyes
        self.poids = [np.random.randn(self.couches[i], self.couches[i + 1]) * np.sqrt(1 / self.couches[i]) for i in range(len(self.couches) - 1)]

      #  self.poids = [np.random.randn(self.couches[i], self.couches[i + 1]) * self.apprentissage for i in range(len(self.couches) - 1)]
        self.biais = [np.zeros((1, self.couches[i + 1])) for i in range(len(self.couches) - 1)]

    def charger_donnees(self, lien, train=True):
        df = pd.read_csv(lien)
        if train:
            self.Y = df.iloc[:, 0].values
            self.X = df.iloc[:, 1:].values / 255.0  # Normalisation
            self.Y_one_hot = self.one_hot(self.Y, self.couches[-1])
        else:
            self.X = df.iloc[:, 1:].values / 255.0
            self.Y = df.iloc[:, 0].values


    def one_hot(self, Y, num_classes):   #exe
        return np.eye(num_classes)[Y]

    def activation_sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def activation_sigmoid_derivative(self, x):
        return x * (1 - x)

    def activation_softmax(self, x):
        exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))
        return exp_x / np.sum(exp_x, axis=1, keepdims=True)

    def forward(self, X):

        activations = [X]
        for i in range(len(self.poids) - 1):
            X = self.activation_sigmoid(np.dot(X, self.poids[i]) + self.biais[i])
            activations.append(X)

        sortie = self.activation_softmax(np.dot(X, self.poids[-1]) + self.biais[-1])
        activations.append(sortie)

        return activations

    def backward(self, activations, Y_one_hot):



        #On prepare une place pour chaque poids
        gradients_poids = [None] * len(self.poids)
        gradients_biais = [None] * len(self.biais)

        #activations -1 est la proba du softmax
        erreur = activations[-1] - Y_one_hot #cross entropy ("dériuvvée de la dernier couches")

        for i in range(len(self.poids) - 1, -1, -1):
            gradients_poids[i] = np.dot(activations[i].T, erreur) / len(Y_one_hot)
            gradients_biais[i] = np.sum(erreur, axis=0, keepdims=True) / len(Y_one_hot)
            if i > 0:

                #ici on repercutez l'erreur du poids precédent et on calcule la nouvelle erreur
                erreur = np.dot(erreur, self.poids[i].T) * self.activation_sigmoid_derivative(activations[i])

        return gradients_poids, gradients_biais

    def mise_a_jour(self, gradients_poids, gradients_biais):
        for i in range(len(self.poids)):
            self.poids[i] -= self.apprentissage * gradients_poids[i]
            self.biais[i] -= self.apprentissage * gradients_biais[i]

    def entrainer(self, nbr=10, intervalle=36):
        for y in range(nbr):

            for i in range(0, len(self.X), intervalle):
                X_i = self.X[i:i + intervalle]  # Taille du batch contrôlée par intervalle
                Y_i = self.Y_one_hot[i:i + intervalle]

                activations = self.forward(X_i)
                gradients_poids, gradients_biais = self.backward(activations, Y_i)
                self.mise_a_jour(gradients_poids, gradients_biais)

            predictions = np.argmax(self.forward(self.X)[-1], axis=1)
            accuracy = np.mean(predictions == np.argmax(self.Y_one_hot, axis=1))
            print(f"{y + 1}/{nbr} entraînement {accuracy:.4f}")

    def tester(self, lien):
        self.charger_donnees(lien, train=False)
        b = self.forward(self.X)[-1]
       # np.set_printoptions(threshold=np.inf)
        #print(b)
        #a = input()
        predictions = np.argmax(self.forward(self.X)[-1], axis=1)


        proba = np.max(self.forward(self.X)[-1], axis=1)
        print(proba)
        return predictions



    def lancer(self, lien_train, lien_test=None, nbr=10):
        self.charger_donnees(lien_train, train=True)
        self.entrainer(nbr)
        if lien_test:
            predictions = self.tester(lien_test)
            print("prédiction", predictions)
            print("valeurs", self.Y)
            print(np.sum(predictions == self.Y) / len(self.Y))





model = Multicouches([784, 64,28, 10], apprentissage=0.1)
model.lancer("mnist_train.csv", "mnist_test.csv", nbr=20)


#[784, 512, 256, 128, 128, 64, 64, 32, 32, 16, 16, 10]