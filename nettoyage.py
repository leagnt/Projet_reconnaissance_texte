import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

class image():

    def __init__(self):
        return None

    #arg: path vers l'image
    #return un reshape de l'image grisée en 100,100
    def ouvrir_images(self,path):#Chemin de l'image en entrée,renvoie une liste 2 dim de valeur entre 0 et 255
        image = Image.open(path)
        image = image.resize((1000, 1000))
        image = image.convert("L")  # Convertir en niveaux de gris
        image_array = np.asarray(image).flatten()
        image_array=image_array.reshape(1000,1000)
        print(image_array.shape)
        return image_array

    def enlever_ombre( self, matrice_image, offset=0):
        ## prend en argument l'image sous la forme d'une matrice numpy et revoie une image sous la forme d'une matrice numpy de pixels noirs ou blancs

        matrice_image = np.copy(matrice_image)
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

    def rogner_image(self,matrice):
        lignes = len(matrice)
        colonnes = len(matrice[0]) if lignes > 0 else 0

        haut, bas = 0, lignes - 1
        while haut < lignes:
            for pixel in matrice[haut]:
                if pixel != 0:
                    break
            else:
                haut += 1
                continue
            break

        while bas >= 0:
            for pixel in matrice[bas]:
                if pixel != 0:
                    break
            else:
                bas -= 1
                continue
            break

        # Trouver la première et la dernière colonne contenant des pixels non nuls
        gauche, droite = 0, colonnes - 1
        while gauche < colonnes:
            for i in range(lignes):
                if matrice[i][gauche] != 0:
                    break
            else:
                gauche += 1
                continue
            break

        while droite >= 0:
            for i in range(lignes):
                if matrice[i][droite] != 0:
                    break
            else:
                droite -= 1
                continue
            break

        # Vérifier qu'on a trouvé au moins un pixel non nul
        if bas < haut or droite < gauche:
            return []  # Retourne une image vide si aucun pixel trouvé

        return matrice[haut:bas + 1, gauche:droite + 1]


if __name__ == "__main__" :
    A=image()
    test=A.ouvrir_images()

    print(test)