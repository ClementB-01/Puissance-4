from Grille import *
from Joueur import *

grille = Grille(7,6)
grille.AfficherMatrice()

victoire = False
draw = False
while isVictory(grille) or isDraw(grille):
    print("Choisissez la colonne où vous voulez insérer votre jeton :")
    colonne = input("-> ")
    grille.addPion(colonne,1)
    grille.AfficherMatrice()

   

def isDraw(grille):
    draw = True
    for i in range(len(grille)):
        for j in range(len(grille[0])/len(grille)):
            if grille[i][j] == 0:
                draw = False
    return draw

def isVictory(grille):
    victory = False