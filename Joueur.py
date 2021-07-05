class Joueur:
    def __init__(self, nom, prénom = "couillon", age = "de raison", score = "Pour l'instant 0"):
        self.nom = nom
        self.prénom = prénom
        self.age = age
        self.score = score

    def Afficher_Score(self):
        print(f"Votre score est de {self.score}")

    
        