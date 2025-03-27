import numpy as np

from PIL import Image, ImageEnhance
class image():

    def __init__(self):
        return None

    def ouvrir_fenetre(self):
        return None

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

