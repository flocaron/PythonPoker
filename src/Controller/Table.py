class Table:

    def __init__(self):
        self.cartes_communes = []
        self.pot = 0
        self.derniere_mise = 0



    def ajouter_carte_commune(self, carte):
        self.cartes_communes.append(carte)




    def ajouter_mise(self, montant):
        if montant < self.derniere_mise:
            return False
        self.pot += montant
        return True


    def __str__(self):
        s = "| "
        for carte in self.cartes_communes:
            s += str(carte) + " "
        s += "| Mise: " + str(self.pot) + "$"
        return s

    def afficher(self):
        print(self)
