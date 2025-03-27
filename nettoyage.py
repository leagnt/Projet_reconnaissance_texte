import random
from PIL import Image,ImageEnhance
import numpy as np

class image():

    def __init__(self):
        return None


    #arg: path vers l'image
    #return un reshape de l'image grisée en 100,100
    def ouvrir_images(self,path):
        image = Image.open(path)
        image = image.resize((1000, 1000))
        image = image.convert("L")  # Convertir en niveaux de gris
        image_array = np.asarray(image).flatten()
        image_array=255-image_array

        image_array=image_array.reshape(1000,1000)
        print(image_array.shape)
        return image_array

    #arg: matrice de l'image
    #return une image sans ombre
    def enlever_ombre(self,matrice_image):
        moyenne_pixel_image=np.mean(matrice_image)
        borne_sup=1.1*moyenne_pixel_image
        nouvelle_matrice=255*np.where[]


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

    def enlever_ombre(self,image,imagepath):
        enhancer = ImageEnhance.Brightness(image)
        image_eclairee = enhancer.enhance(1.5)
        image_eclairee.show()
        image_eclairee.save(imagepath)
    def griser_image(self,imagepath):
        image = Image.open(imagepath)
        image_grise = image.convert("L")
        pixels = list(image_grise.getdata())

A=image()
test=A.ouvrir_images()

print(test)