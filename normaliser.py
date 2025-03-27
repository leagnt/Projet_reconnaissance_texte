import numpy as np
import cv2

class Normaliser:
    def __init__(self, images_lettres, dim=(28, 28)):
        # Liste pour stocker les images normalisées
        self.images_normal = []

        for image_lettre in images_lettres:
            # Redimensionner (28x28)
            image_normal = cv2.resize(image_lettre, dim)
            # Normaliser
            image_normal = image_normal / 255.0
            # Aplatir l'image
            image_normal = image_normal.reshape(-1)  # 784 éléments pour une image 28x28
            self.images_normal.append(image_normal)

    def get_images(self):
        return np.array(self.images_normal)