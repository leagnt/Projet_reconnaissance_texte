from nettoyage import image
from nettoyage2 import afficher_matrice
from scanner import scanner
from normaliser import Normaliser
import numpy as np
from nettoyage2 import afficher_matrice
import matplotlib
path="images/test.png"

im=image()
pic=im.ouvrir_images(path)
print(pic)

pic_clean = im.enlever_ombre_deux(pic,50)
print(np.shape(pic_clean))

pic_rogner = im.rogner_image(pic_clean)
print(pic_rogner)
pic_rogner = pic_rogner.tolist()

scanner = scanner(pic_rogner)
Images = scanner.scanner()
np_Images = [np.array(sublist) for sublist in Images]

Normaliser = Normaliser(np_Images)
Images_finales = Normaliser.renvoyer_image()

print(Images_finales)
for Images in Images_finales :
    print(Images.shape)
    print("okkk")
    I=Images.reshape(28,28)
    print(I.shape)
    afficher_matrice(I)


