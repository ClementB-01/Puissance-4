from Grille import *
from Joueur import *

grille = Grille(7,6)
grille.AfficherMatrice()

victoire = False
draw = False
while isVictory(grille) or isDraw(grille):
    print("Choisissez la colonne où vous voulez insérer votre jeton :")
    colonne = input("-> ")
    ligne = grille.addPion(colonne,1)
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
    compteur = [[0,0,numjoueur,0,0], [0,0,numjoueur,0,0],[0,0,numjoueur,0,0],[0,0,numjoueur,0,0]] # Va compter le nombre de jeton
    compteur2 = [1,1,1,1]
    for i in range(ligne - 1, ligne + 2): #On regarde les environs du dernier coup joué
        for j in range(colonne - 1, colonne + 2):
            if grille[i][j] == numjoueur and i - ligne == 0: ## Compteur sur l'horizontale
                compteur2[0] += 1
            if grille[i][j] == numjoueur and j - colonne == 0: ## Compteur sur la verticale
                compteur2[1] += 1
            if grille[i][j] == numjoueur and ((i < ligne) or (j < colonne)): ## Compteur diagonale +inf->-inf
                compteur2[2] += 1
            if grille[i][j] == numjoueur and (((i > ligne) and (j > colonne)) or ((i < ligne) and (j < colonne))): ## Compteur diagonale -inf->+inf
                compteur2[3] += 1

    if compteur2[0] 