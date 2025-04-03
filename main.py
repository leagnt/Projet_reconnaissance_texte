from matplotlib import pyplot as plt

from nettoyage import image
from scanner import scanner
from normaliser import Normaliser
import numpy as np
import matplotlib

def afficher_matrice(matrice):
    """
    Affiche une matrice 1000x1000 composée de 0 et 1 en noir et blanc.

    Args:
        matrice (numpy.ndarray): Matrice 1000x1000 contenant des 0 et 1.
    """
    plt.imshow(matrice, cmap='gray', interpolation='nearest')
    plt.axis('off')  # Cache les axes pour une meilleure visualisation
    plt.show()



path="images/test.png"

im=image()
pic=im.ouvrir_images(path)
afficher_matrice(pic)
pic = im.rogner_image(pic)
afficher_matrice(pic)


for i in range(-50, 0, 5):
    break
    afficher_matrice(im.enlever_ombre(pic,i))








# pic_rogner = im.rogner_image(pic_clean)
# pic_rogner = pic_rogner.tolist()
#
# scanner = scanner(pic_rogner)
# Images = scanner.scanner()
# np_Images = [np.array(sublist) for sublist in Images]
#
# Normaliser = Normaliser(np_Images)
# Images_finales = Normaliser.renvoyer_image()
#
# print(Images_finales)
# for Images in Images_finales :
#     print(Images.shape)
#     print("okkk")
#     I=Images.reshape(28,28)
#     print(I.shape)
#     afficher_matrice(I)


