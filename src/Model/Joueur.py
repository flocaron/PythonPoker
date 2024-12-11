class Joueur:
    def __init__(self, nom, jetons):
        self.nom = nom
        self.jetons = jetons
        self.main = []
        self.actif = True

    def recevoir_carte(self, carte):
        self.main.append(carte)

    def miser(self, montant):
        if montant > self.jetons:
            raise ValueError("Mise invalide : pas assez de jetons.")
        self.jetons -= montant
        return montant

    def se_coucher(self):
        self.actif = False

    def __str__(self):
        etat = "Actif" if self.actif else "Couché"
        return f"{self.nom} ({etat}) - Jetons: {self.jetons} - Main: {', '.join(str(c) for c in self.main)}"
