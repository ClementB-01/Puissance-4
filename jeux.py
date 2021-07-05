from grille import *
from joueur import *

grille = Grille(7,6)
grille.AfficherMatrice()
def Main():
    victoire = False
    draw = False
    while True:
        print("Bienvenue dans ce Puissance 4")



        print("Choisissez la colonne où vous voulez insérer votre jeton :")
        colonne = int(input("-> "))
        
        print(grille.addPion(colonne,1))
        grille.AfficherMatrice()

   

def isDraw(grille):
    draw = True
    for i in range(len(grille)):
        for j in range(len(grille[0])/len(grille)):
            if grille[i][j] == 0:
                draw = False
    return draw

def isVictory(grille, colonne, ligne, numjoueur):
    victory = False
    ##compteur = [[0,0,numjoueur,0,0], [0,0,numjoueur,0,0],[0,0,numjoueur,0,0],[0,0,numjoueur,0,0]] # Va compter le nombre de jeton
    compteur2 = [1,1,1,1]

    for i in range(ligne - 1, ligne + 2): #On regarde les environs du dernier coup joué
        for j in range(colonne - 1, colonne + 2):

            if grille[i][j] == numjoueur and i - ligne == 0: ## Compteur sur l'horizontale
                compteur2[0] += 1
                if i < ligne: ## Vérification par continuité des bords large selon direction
                    compteur2[0] += isCLigne(grille, i, j, "ho", 0)
                else:
                    compteur2[0] += isCLigne(grille, i, j, "ho", 1)

            if grille[i][j] == numjoueur and j - colonne == 0: ## Compteur sur la verticale
                compteur2[1] += 1
                if j < colonne: ## Vérification par continuité des bords large selon direction
                    compteur2[1] += isCLigne(grille, i, j, "ve", 0)
                else:
                    compteur2[1] += isCLigne(grille, i, j, "ve", 1)

            if grille[i][j] == numjoueur and ((i < ligne) or (j < colonne)): ## Compteur diagonale +inf->-inf
                compteur2[2] += 1
                if i > ligne and j < colonne: ## Vérification par continuité des bords large selon direction
                    compteur2[2] += isCLigne(grille, i, j, "d1", 0)
                else:
                    compteur2[2] += isCLigne(grille, i, j, "d1", 1)

            if grille[i][j] == numjoueur and (((i > ligne) and (j > colonne)) or ((i < ligne) and (j < colonne))): ## Compteur diagonale -inf->+inf
                compteur2[3] += 1
                if i < ligne and j < colonne: ## Vérification par continuité des bords large selon direction
                    compteur2[3] += isCLigne(grille, i, j, "d1", 0)
                else:
                    compteur2[3] += isCLigne(grille, i, j, "d1", 1)

    if compteur2[0] >= 4 or compteur2[1] >= 4 or compteur2[2] >= 4 or compteur2[3] >= 4:
        victory = True
    return victory


def isCLigne(grille, i, j, numjoueur, sens, dir):
    compteur = 0
    if sens == "ho":
        if dir == 0:
            if grille[i][j - 1] == numjoueur:
                compteur += 1
                if grille[i][j - 2] == numjoueur:
                    compteur += 1
        else:
            if grille[i][j + 1] == numjoueur:
                compteur += 1
                if grille[i][j + 2] == numjoueur:
                    compteur += 1

    elif sens == "ve":
        if dir == 0:
            if grille[i - 1][j] == numjoueur:
                compteur += 1
                if grille[i - 2][j] == numjoueur:
                    compteur += 1
        else:
            if grille[i + 1][j] == numjoueur:
                compteur += 1
                if grille[i + 2][j] == numjoueur:
                    compteur += 1

    elif sens == "d1":
        if dir == 0:
            if grille[i + 1][j - 1] == numjoueur:
                compteur += 1
                if grille[i + 2][j - 2] == numjoueur:
                    compteur += 1
        else:
            if grille[i - 1][j + 1] == numjoueur:
                compteur += 1
                if grille[i - 2][j + 2] == numjoueur:
                    compteur += 1

    elif sens == "d2":
        if dir == 0:
            if grille[i - 1][j + 1] == numjoueur:
                compteur += 1
                if grille[i - 2][j + 2] == numjoueur:
                    compteur += 1
        else:
            if grille[i + 1][j - 1] == numjoueur:
                compteur += 1
                if grille[i + 2][j - 2] == numjoueur:
                    compteur += 1

    return compteur


Main()
