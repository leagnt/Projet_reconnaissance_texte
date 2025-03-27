import random
from PIL import Image,ImageEnhance
import numpy as np

class image():

    def __init__(self):
        return None

    def ouvrir_images(self,path):#Chemin de l'image en entrée,renvoie une liste 2 dim de valeur entre 0 et 255
        image = Image.open(path)
        image = image.resize((1000, 1000))
        image = image.convert("L")  # Convertir en niveaux de gris
        image_array = np.asarray(image).flatten()
        image_array=255-image_array #O pour le blanc et 255 pour le noir

        image_array=image_array.reshape(1000,1000)
        print(image_array.shape)
        return image_array


    def enlever_ombre(self,image,imagepath):
        #prend en paramètres une matrice pour image et renvoie une matrice
        #Valeurs entre 0 et 255
        enhancer = ImageEnhance.Brightness(image)
        image_eclairee = enhancer.enhance(1.5)
        image_eclairee.show()
        image_eclairee.save(imagepath)

    def griser_image(self,imagepath):
        image = Image.open(imagepath)
        image_grise = image.convert("L")
        pixels = list(image_grise.getdata())


    def enlever_ombre(self,matrice_image):
        # prend en argument l'image sous la forme d'une matrice et revoie une image sous la forme d'une matrice de pixels noirs ou blancs
        # blanc=0 et noir=255
        #Principe : on sépare l'image en 9 régions, on calcule la moyenne de la couleur de chacune des régions et on applique un filtre

        dim=np.shape(matrice_image)
        ligne=dim[0]//3
        colonne=dim[1]//3
        for i in range(3):
            for j in range(3):
                if i==2 and j==2:
                    sous_matrice = matrice_image[i * ligne : , j*colonne :]
                elif i==2 and j!=2:
                    sous_matrice = matrice_image[i * ligne : , j * colonne:(j + 1) * colonne]
                elif i!=2 and j==2:
                    sous_matrice = matrice_image[i * ligne : (i + 1) * ligne, j * colonne :]
                else:
                    sous_matrice = matrice_image[i * ligne : (i + 1) * ligne, j * colonne : (j + 1) * colonne]
                moyenne_pixel = np.mean(sous_matrice)
                borne_sup = 1.1 * moyenne_pixel
                borne_sup = 0.9 * moyenne_pixel









    def rogner_image(self):
        lignes = len(self.matrice)
        colonnes = len(self.matrice[0]) if lignes > 0 else 0

        haut, bas = 0, lignes - 1
        while haut < lignes:
            for pixel in self.matrice[haut]:
                if pixel != 0:
                    break
            else:
                haut += 1
                continue
            break

        while bas >= 0:
            for pixel in self.matrice[bas]:
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
                if self.matrice[i][gauche] != 0:
                    break
            else:
                gauche += 1
                continue
            break

        while droite >= 0:
            for i in range(lignes):
                if self.matrice[i][droite] != 0:
                    break
            else:
                droite -= 1
                continue
            break

        # Vérifier qu'on a trouvé au moins un pixel non nul
        if bas < haut or droite < gauche:
            return []  # Retourne une image vide si aucun pixel trouvé

        # Rogner l'image pour ne garder que la zone utile
        return [ligne[gauche:droite + 1] for ligne in self.matrice[haut:bas + 1]]


chemin = "./images/test.png"
A = image()
test = A.ouvrir_images(chemin)