class Table:
    def __init__(self):
        self.cartes_communes = []
        self.joueurs = []
        self.pot = 0

    def ajouter_carte_commune(self, carte):
        self.cartes_communes.append(carte)

    def ajouter_mise(self, montant):
        self.pot += montant

    def afficher_cartes(self):
        return ", ".join(str(carte) for carte in self.cartes_communes)

    def __str__(self):
        return f"Cartes sur la table: {self.afficher_cartes()} | Pot: {self.pot}"
