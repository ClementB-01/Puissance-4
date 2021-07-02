
from termcolor import colored, cprint

class Grille:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        A = []
        B = []
        for i in range(hauteur):
            for j in range(largeur):
                A.append(0)
            B.append(A)
        self.matrice = B
        #print(len(self.matrice))
        #print(len(self.matrice[0]))


    def AfficherMatrice(self):
        var = ' '
        color = ''
        ligne = ""
        for i in range(self.largeur):
            for j in range(self.hauteur):
                cprint("|", "blue", "on_grey", end="")

                if self.matrice[i][j] == 0: ## Condition pour identifier le caractère et lui appliquer une couleur
                    var = ' '
                    print("| ", end = "")
                else:
                    var = 'X'
                    color = "grey"
                    if self.matrice[i][j] == 1:
                        color = "red"
                    elif self.matrice[i][j] == 2:
                        color = "yellow"
                    cprint(var, color, "on_grey", end="")

            cprint("|", "red", "on_grey")
            print("bjr")

    def isColonnePleine(self, colonne):
        verite = False
        if self.matrice[0][colonne] == 1 or self.matrice[0][colonne] == 2: #in [1,2]
            verite = True
        return verite

    def addPion(self, colonne, numjoueur):
        
        ligne =

        while ligne < 0:
            if 
        