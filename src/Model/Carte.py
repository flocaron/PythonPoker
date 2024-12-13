from treys import Card, Evaluator

class Carte:

    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return f"{self.valeur}{self.couleur}"

    def to_treys(self):
        # Mappage des symboles de couleurs vers les lettres attendues par Treys
        couleur_map = {
            "♥": "h",  # cœur
            "♦": "d",  # carreau
            "♠": "s",  # pique
            "♣": "c"   # trèfle
        }
        
        # Conversion de la couleur
        couleur_treys = couleur_map.get(self.couleur)

        if couleur_treys is None:
            raise ValueError(f"Couleur inconnue: {self.couleur}")

        # Retourner la carte au format attendu par Treys
        return f"{self.valeur}{couleur_treys}"
