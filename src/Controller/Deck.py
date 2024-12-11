import random

from Model.Carte import Carte

class Deck:
    COULEURS = ["Coeur", "Carreau", "Pique", "Trèfle"]
    VALEURS = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Valet", "Dame", "Roi", "As"]

    def __init__(self):
        self.cartes = [Carte(valeur, couleur) for couleur in self.COULEURS for valeur in self.VALEURS]

    def melanger(self):
        random.shuffle(self.cartes)

    def piocher(self):
        if not self.cartes:
            raise ValueError("Le deck est vide !")
        return self.cartes.pop()
