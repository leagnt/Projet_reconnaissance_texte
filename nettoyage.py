import random
from PIL import Image
import numpy as np

class image():

    def __init__(self):
        return None


    #arg: path vers l'image
    #return un reshape de l'image grisée en 100,100
    def ouvrir_images(self,path):#Chemin de l'image en entrée,renvoie une liste 2 dim de valeur entre 0 et 255
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
        # prend en argument l'image sous la forme d'une matrice numpy et revoie une image sous la forme d'une matrice de pixels noirs ou blancs
        # blanc=0 et noir=255
        #Principe : on sépare l'image en 9 régions, on calcule la moyenne de la couleur de chacune des régions et on applique un filtre
        liste_sous_matrices=[]
        dim=np.shape(matrice_image)
        ligne=dim[0]//3
        colonne=dim[1]//3

        #création des 9 sous_matrices
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

                #application du filtre
                moyenne_pixel = np.mean(sous_matrice)
                borne_sup = 1.1 * moyenne_pixel
                borne_inf= 0.9 * moyenne_pixel
                dim_sous_mat=np.shape(sous_matrice)

                for ligne in range(dim_sous_mat[0]):
                    for colonne in range(dim_sous_mat[1]):
                        if sous_matrice[ligne,colonne]>borne_sup:
                            sous_matrice[ligne, colonne]=255
                        elif sous_matrice[ligne,colonne]<borne_inf:
                            sous_matrice[ligne, colonne]=0

                liste_sous_matrices.append(sous_matrice)

        #reassemblage matrice
        #extraction des matrices pour chaque ligne
        ligne_1=[liste_sous_matrices[0],liste_sous_matrices[3],liste_sous_matrices[6]]
        ligne_2=[liste_sous_matrices[1],liste_sous_matrices[4],liste_sous_matrices[7]]
        ligne_3 =[liste_sous_matrices[2],liste_sous_matrices[5],liste_sous_matrices[8]]

        #concaténation du tout
        ligne_1=np.concatenate(ligne_1,axis=0)
        ligne_2=np.concatenate(ligne_2, axis=0)
        ligne_3=np.concatenate(ligne_3, axis=0)
        matrice_image=np.concatenate((ligne_1,ligne_2,ligne_3),axis=1)

        return matrice_image

    def enlever_ombre_deux(self,matrice_image, offset=0):
        ## prend en argument l'image sous la forme d'une matrice numpy et revoie une image sous la forme d'une matrice numpy de pixels noirs ou blancs

        # application du filtre
        moyenne_pixel = np.mean(matrice_image)
        dim_sous_mat = np.shape(matrice_image)

        for ligne in range(dim_sous_mat[0]):
            for colonne in range(dim_sous_mat[1]):
                if matrice_image[ligne, colonne] > (moyenne_pixel+offset):
                    matrice_image[ligne, colonne] = 1
                elif matrice_image[ligne, colonne] < (moyenne_pixel+offset):
                    matrice_image[ligne, colonne] = 0

        return matrice_image



    def rogner_image(self,matrice):
        lignes = len(matrice)
        colonnes = len(matrice[0]) if lignes > 0 else 0

        haut, bas = 0, lignes - 1
        while haut < lignes:
            for pixel in matrice[haut]:
                if pixel != 0:
                    break
            else:
                haut += 1
                continue
            break

        while bas >= 0:
            for pixel in matrice[bas]:
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
                if matrice[i][gauche] != 0:
                    break
            else:
                gauche += 1
                continue
            break

        while droite >= 0:
            for i in range(lignes):
                if matrice[i][droite] != 0:
                    break
            else:
                droite -= 1
                continue
            break

        # Vérifier qu'on a trouvé au moins un pixel non nul
        if bas < haut or droite < gauche:
            return []  # Retourne une image vide si aucun pixel trouvé

        return matrice[haut:bas + 1, gauche:droite + 1]

if __name__ == "__main__" :
    A=image()
    test=A.ouvrir_images()

    print(test)