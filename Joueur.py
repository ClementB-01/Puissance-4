class Joueur:
    def __init__(self, nom, prénom, age, score):
        self.nom = nom
        self.prénom = prénom
        self.age = age
        self.score = score

    def Afficher_Score(self):
        print(f"Votre score est de {self.score}")

    
        