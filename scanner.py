class scanner:
    def __init__(self):
        self.base = [[1,1,1],[1,1,1],[0,1,0],[1,0,1],[1,1,1],[0,0,0]
                     ]
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
        i = 0
        condition = True
        while i < len(self.base):

            longueur_lettre = 0

            while i < len(self.base) and self.ligne_blanche(i) is condition:
                i += 1
                longueur_lettre += 1

            #self.liste_hauteur.append(self.base[])
            condition = self.inverse(condition)

        print(self.liste_hauteur)

    #sous_matrice = [row[20:30] for row in matrice[10:20]]

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
             if self.base[indice_ligne + i ][indice_colonne] == 0:
                 return False
        return True


scanner = scanner()
scanner.hauteur_ligne()