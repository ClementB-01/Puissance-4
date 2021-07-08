from Grille import *
from Joueur import *

matrice = Grille(7,6)


def Main():
    victoire = False
    draw = False
    compteur = 0
    numjoueur = 0

    print("Bienvenue dans ce Puissance 4")
    joueur1 = input("Entrer le nom du premier joueur : ")
    joueur1 = Joueur(joueur1)
    joueur2 = input("Entrer le nom du second joueur : ")
    joueur2 = Joueur(joueur2)

    matrice.AfficherMatrice()
        
    while not victoire and not draw:
        print("Choisissez la colonne où vous voulez insérer votre jeton :")
        try:
            colonne = int(input("-> "))
        except: #Bloque la sortie du programme via CTRL + C || comment le résoudre ?
            print("Colonne invalide")
            colonne = matrice.largeur + 1
        if not matrice.isColonnePleine(colonne):
            if compteur % 2 == 0:
                numjoueur = 1
            else:
                numjoueur = -1

            compteur += 1
            ligne = matrice.addPion(colonne, numjoueur)
            victoire = isVictory2(matrice, colonne, ligne, numjoueur)
            matrice.AfficherMatrice()
            draw = isDraw(matrice)

        else:
            print("Veuillez rejouer")
        """except:
            print("Entrée invalide, veuillez réessayer")
            pass"""
        
        if draw:
            print("Partie nulle")
            joueur1.score = joueur2.score = "0.5"

        if victoire:
            print(f"Victoire du joueur {numjoueur}")
            if numjoueur == 1:
                joueur1.score = 1
            else:
                joueur2.score = 1
            #f"joueur{numjoueur}.score" = "1"
        
        
    
    print("Fin")    

   
def isDraw(matrice): #Fonctionnel
    draw = False
    colpleine = 0
    for i in range(0, matrice.largeur):
        if matrice.isColonnePleine(i):
            colpleine += 1
    if colpleine == 7:
        draw = True
    return draw

def isVictory(matrice, colonne, ligne, numjoueur):
    victory = False
    ##compteur = [[0,0,numjoueur,0,0], [0,0,numjoueur,0,0],[0,0,numjoueur,0,0],[0,0,numjoueur,0,0]] # Va compter le nombre de jeton
    compteur2 = [1,1,1,1]

    for i in range(ligne - 1, ligne + 2): #On regarde les environs du dernier coup joué
        for j in range(colonne - 1, colonne + 2):

            if matrice[i][j] == numjoueur and i - ligne == 0: ## Compteur sur l'horizontale
                compteur2[0] += 1
                if i < ligne: ## Vérification par continuité des bords large selon direction
                    compteur2[0] += isCLigne(matrice, i, j, "ho", 0)
                else:
                    compteur2[0] += isCLigne(matrice, i, j, "ho", 1)

            if matrice[i][j] == numjoueur and j - colonne == 0: ## Compteur sur la verticale
                compteur2[1] += 1
                if j < colonne: ## Vérification par continuité des bords large selon direction
                    compteur2[1] += isCLigne(matrice, i, j, "ve", 0)
                else:
                    compteur2[1] += isCLigne(matrice, i, j, "ve", 1)

            if matrice[i][j] == numjoueur and ((i < ligne) or (j < colonne)): ## Compteur diagonale +inf->-inf
                compteur2[2] += 1
                if i > ligne and j < colonne: ## Vérification par continuité des bords large selon direction
                    compteur2[2] += isCLigne(matrice, i, j, "d1", 0)
                else:
                    compteur2[2] += isCLigne(matrice, i, j, "d1", 1)

            if matrice[i][j] == numjoueur and (((i > ligne) and (j > colonne)) or ((i < ligne) and (j < colonne))): ## Compteur diagonale -inf->+inf
                compteur2[3] += 1
                if i < ligne and j < colonne: ## Vérification par continuité des bords large selon direction
                    compteur2[3] += isCLigne(matrice, i, j, "d1", 0)
                else:
                    compteur2[3] += isCLigne(matrice, i, j, "d1", 1)

    if compteur2[0] >= 4 or compteur2[1] >= 4 or compteur2[2] >= 4 or compteur2[3] >= 4:
        victory = True
    return victory

def isCLigne(matrice, i, j, numjoueur, sens, dir):
    compteur = 0
    if sens == "ho":
        if dir == 0:
            if matrice[i][j - 1] == numjoueur:
                compteur += 1
                if matrice[i][j - 2] == numjoueur:
                    compteur += 1
        else:
            if matrice[i][j + 1] == numjoueur:
                compteur += 1
                if matrice[i][j + 2] == numjoueur:
                    compteur += 1

    elif sens == "ve":
        if dir == 0:
            if matrice[i - 1][j] == numjoueur:
                compteur += 1
                if matrice[i - 2][j] == numjoueur:
                    compteur += 1
        else:
            if matrice[i + 1][j] == numjoueur:
                compteur += 1
                if matrice[i + 2][j] == numjoueur:
                    compteur += 1

    elif sens == "d1":
        if dir == 0:
            if matrice[i + 1][j - 1] == numjoueur:
                compteur += 1
                if matrice[i + 2][j - 2] == numjoueur:
                    compteur += 1
        else:
            if matrice[i - 1][j + 1] == numjoueur:
                compteur += 1
                if matrice[i - 2][j + 2] == numjoueur:
                    compteur += 1

    elif sens == "d2":
        if dir == 0:
            if matrice[i - 1][j + 1] == numjoueur:
                compteur += 1
                if matrice[i - 2][j + 2] == numjoueur:
                    compteur += 1
        else:
            if matrice[i + 1][j - 1] == numjoueur:
                compteur += 1
                if matrice[i + 2][j - 2] == numjoueur:
                    compteur += 1

    return compteur

def isVictory2(matrice, colonne, ligne, numjoueur):
    victoire = False
    compte2 = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
    pas = 0

    temp = [-1,True,-1,True,-1,True,-1,True]
    for l in range(0, 4):
        if ligne - l < 0 and temp[1]:
            temp[0] = ligne - l + 1
            temp[1] = False
        elif ligne + l >= matrice.hauteur and temp[3]:
            temp[2] = ligne + l - 2
            temp[3] = False
        if colonne - l < 0 and temp[5]:
            temp[4] = colonne - l + 1
            temp[5] = False
        elif colonne + l >= matrice.hauteur and temp[7]:
            temp[6] = colonne + l  - 2
            temp[7] = False
    if temp[0] == -1:
        temp[0] = ligne - 3
    if temp[2] == -1:
        temp[2] = ligne + 4
    if temp[4] == -1:
        temp[4] = colonne - 3
    if temp[6] == -1:
        temp[6] = colonne + 4
    #print(f"ligne - 3 = {temp[0]}, ligne + 4 = {temp[2]}, colonne - 3 = {temp[4]}, colonne + 4 = {temp[6]}")

    for i in range(temp[0], temp[1]):
        for j in range(temp[2], temp[3]):
            #print(f"i = {i}, j = {j}")
            if matrice.matrice[i][j] == numjoueur and ((i < ligne) or (j < colonne)):                
                compte2[0][pas] = numjoueur
            if matrice.matrice[i][j] == numjoueur and (((i > ligne) and (j > colonne)) or ((i < ligne) and (j < colonne))):
                compte2[1][pas] = numjoueur
            if matrice.matrice[i][j] == numjoueur and i - ligne == 0:
                compte2[2][pas] = numjoueur
            if matrice.matrice[i][j] == numjoueur and j - colonne == 0:
                compte2[3][pas] = numjoueur
            pas += 1

    compte = [1,1,1,1]
    check = 0

    for v in range(len(compte2)):
        for k in range(len(compte2[0])):
            if k == 0:
                check = compte2[v][k]
            else:
                if check == compte2[v][k] and check == numjoueur:
                    compte[v] += 1
                else:
                    if compte[v] < 4:
                        compte[v] = 1
                check = compte2[v][k]

    if compte[0] >= 4 or compte[1] >= 4 or compte[2] >= 4 or compte[3] >= 4:
        victoire = True
    print(f"compte1 = {compte[0]}, compte2 = {compte[1]}, compte3 = {compte[2]}, compte 4 = {compte[3]}")
    return victoire



Main()
