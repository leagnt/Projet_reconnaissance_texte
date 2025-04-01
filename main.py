from nettoyage import image
from scanner import scanner
import numpy as np
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
print(Images)
