import random

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