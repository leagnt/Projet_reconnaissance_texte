from nettoyage import image
import numpy as np
path="images/test.png"

im=image()
pic=im.ouvrir_images(path)

print(pic)

pic_clean = im.enlever_ombre_deux(pic)
print(np.shape(pic_clean))


pic_rogner = im.rogner_image(pic_clean)

print(pic_rogner)
