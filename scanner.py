class scanner:
    def __init__(self):
        self.base = [[1,1,1],[1,1,0],[1,0,1],[1,1,0],[1,1,1],[0,0,0]]
        self.liste_hauteur = []
        self.matrice_image = [[]]

    def hauteur_ligne(self):
        #renvoie une liste avec les hauteurs de chaque ligne
        i = 0
        condition = True
        while i < len(self.base):

            taille_ligne = 0

            while i < len(self.base) and self.ligne_blanche(i) is condition :
                i +=1
                taille_ligne +=1

            self.liste_hauteur.append(taille_ligne)
            condition = self.inverse(condition)


        print(self.liste_hauteur)


    def trouve_lettre(self):

        indice_ligne = 0
        indice_taille_ligne = 1
        taille_ligne = self.liste_hauteur[indice_taille_ligne]
        print(taille_ligne)


        i = 0
        condition = True
        print(len(self.base[0]),"f")
        while i < len(self.base[0]):


            indice = i
            print(i)

            while i < len(self.base[0]) and self.colonne_blanche(i,indice_ligne,taille_ligne) is condition:
                print( self.colonne_blanche(i,indice_ligne,taille_ligne),"jfjjff")
                i += 1



            sub_matrix = [row[indice:i] for row in self.base[indice_ligne:(indice_ligne+taille_ligne)]]

            print(sub_matrix ,"hjrfjf",indice, i )

            self.matrice_image.append(sub_matrix )

            condition = self.inverse(condition)

        print(self.matrice_image)



    def inverse(self, condition):
        if condition is True:
            return False
        return True


    def ligne_blanche(self, indice):
        # pour un indice de ligne, renvoie vrai si toutes les pixels de cette ligne sont blancs, faux sinon
        for i in range(len(self.base[0])):
             if self.base[indice][i] == 0:
                 return False
        return True


    def colonne_blanche(self, indice_colonne, indice_ligne, taille):
        # pour un indice de colonne, renvoie vrai si toutes les pixels de cette colonne sont blancs, faux sinon
        for i in range(taille):
             if self.base[indice_ligne + (i) ][indice_colonne] == 0:
                 return True
        return False


scanner = scanner()
scanner.hauteur_ligne()
scanner.trouve_lettre()