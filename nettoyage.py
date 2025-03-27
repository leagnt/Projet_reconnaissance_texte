import random
from PIL import Image,ImageEnhance
import numpy as np

class image():

    def __init__(self):
        return None

    def ouvrir_images(self):#Renvoie la liste d'une image
        image = Image.open("./images/test.png")
        image = image.resize((1000, 1000))
        image = image.convert("L")  # Convertir en niveaux de gris
        image_array = np.asarray(image).flatten()
        image_array=255-image_array #O pour le blanc et 255 pour le noir

        image_array=image_array.reshape(1000,1000)
        print(image_array.shape)
        return image_array


    def enlever_ombre(self,image,imagepath):
        enhancer = ImageEnhance.Brightness(image)
        image_eclairee = enhancer.enhance(1.5)
        image_eclairee.show()
        image_eclairee.save(imagepath)
    def griser_image(self,imagepath):
        image = Image.open(imagepath)
        image_grise = image.convert("L")
        pixels = list(image_grise.getdata())


    def enlever_ombre(self,matrice_image):
        ## prend en argument l'ilmage sous la forme d'une matrice et revoie une image de pixels noirs ou blancs blanc=0 et noir=255
        moyenne_pixel_image=np.mean(matrice_image)
        borne_sup=1.1*moyenne_pixel_image
        nouvelle_matrice=255*np.where[]



A=image()
test=A.ouvrir_images()

print(test)