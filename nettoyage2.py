import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
def afficher_matrice(matrice):
    """
    Affiche une matrice 1000x1000 composée de 0 et 1 en noir et blanc.

    Args:
        matrice (numpy.ndarray): Matrice 1000x1000 contenant des 0 et 1.
    """
    if matrice.shape != (1000, 1000):
        raise ValueError("La matrice doit être de taille 1000x1000")

    plt.imshow(1-matrice, cmap='gray', interpolation='nearest')
    plt.axis('off')  # Cache les axes pour une meilleure visualisation
    plt.show()


def ouvrir_images(path):#Chemin de l'image en entrée,renvoie une liste 2 dim de valeur entre 0 et 255
    image = Image.open(path)
    image = image.resize((1000, 1000))
    image = image.convert("L")  # Convertir en niveaux de gris
    image_array = np.asarray(image).flatten()
    image_array=255-image_array

    image_array=image_array.reshape(1000,1000)
    print(image_array.shape)
    return image_array


def enlever_ombre_deux(self, matrice_image, offset):
    ## prend en argument l'image sous la forme d'une matrice numpy et revoie une image sous la forme d'une matrice numpy de pixels noirs ou blancs

    # application du filtre
    moyenne_pixel = np.mean(matrice_image)
    dim_mat = np.shape(matrice_image)

    for ligne in range(dim_mat[0]):
        for colonne in range(dim_mat[1]):
            if matrice_image[ligne, colonne] > (moyenne_pixel + offset):
                matrice_image[ligne, colonne] = 1
            elif matrice_image[ligne, colonne] < (moyenne_pixel + offset):
                matrice_image[ligne, colonne] = 0

    return matrice_image


def ombres_3(self, matrice_image, finesse=20):
    liste = [0 for i in range(finesse)]
    precision = 1 / finesse
    dim_mat = np.shape(matrice_image)
    for ligne in range(dim_mat[0]):
        for colonne in range(dim_mat[1]):
            valeur_pixel = matrice_image[ligne, colonne] / 255
            rang = float(valeur_pixel) // precision
            liste[rang] += 1

    minimums = []
    for i in range(1, len(liste) - 1):
        if liste[i] < liste[i + 1] and liste[i] > liste[i - 1]:
            minimums.append(i)

    seuil = minimums[0] * precision
    print()

    for ligne in range(dim_mat[0]):
        for colonne in range(dim_mat[1]):
            if matrice_image[ligne, colonne] > seuil:
                matrice_image[ligne, colonne] = 1
            elif matrice_image[ligne, colonne] < seuil:
                matrice_image[ligne, colonne] = 0
    return matrice_image

im=ouvrir_images("/Users/leagnt/Desktop/GitHub/Projet_reconnaissance_texte/images/test.png")
print(im)
im2=ombres_3(im, 30)

afficher_matrice(im2)
#ok