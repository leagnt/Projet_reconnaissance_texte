
from PIL import Image, ImageEnhance
class image():

    def __init__(self):
        return None

    def ouvrir_fenetre(self):
        return None

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
