
from termcolor import colored, cprint

class Grille:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur #La largeur représente le nombre de colonne
        self.hauteur = hauteur #la hauteur représente le nombre de ligne
        A = []
        B = []
        for i in range(self.hauteur):
            for j in range(self.largeur):
                A.append(0)
            B.append(A)
        self.matrice = B
        #print(len(self.matrice))
        #print(len(self.matrice[0]))



    def AfficherMatrice(self): ## FONCTIONNEL mais penser à ajouter les coordonnées pour simplifier le jeu
        var = ' '
        color = ''
        ligne = ""
        for i in range(self.hauteur):
            for j in range(self.largeur):
                cprint("|", "blue", "on_grey", end="")

                if self.matrice[i][j] == 0: ## Condition pour identifier le caractère et lui appliquer une couleur
                    var = ' '
                    cprint(" ", "blue", "on_grey", end = "")
                else:
                    var = 'X'
                    color = "grey"
                    if self.matrice[i][j] == 1:
                        color = "red"
                    elif self.matrice[i][j] == 2:
                        color = "yellow"
                    cprint(var, color, "on_grey", end="")
                #print(j, end="")
                if j < len(self.matrice):
                    cprint("|", "blue", "on_grey", end="")
                else:
                    cprint("|", "blue", "on_grey")

           

    def isColonnePleine(self, colonne):
        verite = False
        if self.matrice[0][colonne] == 1 or self.matrice[0][colonne] == 2: #in [1,2]
            verite = True
        return verite

    def addPion(self, colonne, numjoueur):
        ligne = 0
        presence = True

        while presence == True:
            if self.matrice[ligne][colonne] not in [1,2]:
                presence = False
                print("jouable")
                print(ligne)
            else:
                ligne += 1

        
        self.matrice[ligne][colonne] = numjoueur
        return ligne
        
