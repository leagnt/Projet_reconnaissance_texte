from nettoyage import image
path="images/test.png"

im=image()
pic=im.ouvrir_images(path)

print(pic)

pic_clean = im.enlever_ombre(pic)
print(pic_clean)

pic_rogner = im.rogner_image(pic_clean)

print(pic_rogner)
