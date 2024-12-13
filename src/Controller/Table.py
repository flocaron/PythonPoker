from treys import Card, Evaluator

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
        if len(self.cartes_communes) == 0:
            return ""
        else:
            s = "| "
            for carte in self.cartes_communes:
                s += str(carte) + " "
            s += "| Mise: " + str(self.pot) + "$"
            return s

    def afficher(self):
        print(self)

    def comparer_mains(self, joueur1, joueur2):
        """
        Compare les mains de deux joueurs et retourne le gagnant ou False en cas d'égalité.
        La méthode attend des objets Joueur avec une main composée d'objets Carte.
        """
        # Convertir les cartes des mains des joueurs et des cartes communes
        cartes_main1 = [Card.new(carte.to_treys()) for carte in joueur1.main]
        cartes_main2 = [Card.new(carte.to_treys()) for carte in joueur2.main]
        cartes_table = [Card.new(carte.to_treys()) for carte in self.cartes_communes]

        # Initialiser l'évaluateur
        evaluator = Evaluator()

        # Évaluer les scores des mains
        score_main1 = evaluator.evaluate(cartes_table, cartes_main1)
        score_main2 = evaluator.evaluate(cartes_table, cartes_main2)

        # Comparer les scores
        if score_main1 < score_main2:  # Moins c'est mieux
            return joueur1
        elif score_main2 < score_main1:
            return joueur2
        else:
            return False  # Égalité
