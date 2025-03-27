import numpy as np
import cv2

class Normaliser: #Normalise les image obtenu apres le découpage en liste applati de 784 pixels
    def __init__(self, images_lettres, dim=(28, 28)): #prend en entree un ensemble de matrices carees
        # Liste pour stocker les images normalisées
        self.images_normal = []

        # Traiter chaque image dans la liste
        for image_lettre in images_lettres:
            image_normal = self.resize(image_lettre, dim)
            image_normal = image_normal / 255.0
            image_normal = image_normal.reshape(-1)
            self.images_normal.append(image_normal)

    def resize(self, image_lettre, dim): #redim l'image en 28,28 et renvoie une matrice
        h, l = image_lettre.shape
        nouv_h, nouv_l = dim

        nouvelle_image = np.zeros((nouv_h, nouv_l), dtype=np.float32)

        h_ratio = h / nouv_h
        l_ratio = l / nouv_l

        for i in range(nouv_h):
            for j in range(nouv_l):
                # Trouver la position correspondante sur l'image d'origine
                x = int(j * h_ratio)
                y = int(i * l_ratio)
                nouvelle_image[i, j] = image_lettre[x, y]

        return nouvelle_image #renvoie la liste de 784 pixels


    def renvoyer_image(self): #renvoie une liste de tout les images sous forme de liste applatit (784 pixels)
        return np.array(self.images_normal)