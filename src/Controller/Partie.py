from Controller.Table import Table
from Controller.Deck import Deck
from Model.Joueur import Joueur


class Partie:
    def __init__(self, joueurs, jetons_par_defaut=100):
        self.table = Table()
        self.deck = Deck()
        self.joueurs = [Joueur(nom, jetons_par_defaut) for nom in joueurs]

    def demarrer(self):
        self.deck.melanger()
        self.distribuer_cartes()
        self.flop()
        self.turn()
        self.river()
        self.determiner_gagnant()

    def distribuer_cartes(self):
        for joueur in self.joueurs:
            for _ in range(2):  # Chaque joueur reçoit 2 cartes
                joueur.recevoir_carte(self.deck.piocher())
        print("Cartes distribuées.")

    def flop(self):
        print("Flop...")
        for _ in range(3):  # Le flop : 3 cartes
            self.table.ajouter_carte_commune(self.deck.piocher())

    def turn(self):
        print("Turn...")
        self.table.ajouter_carte_commune(self.deck.piocher())

    def river(self):
        print("River...")
        self.table.ajouter_carte_commune(self.deck.piocher())

    def determiner_gagnant(self):
        print("Déterminer le gagnant... (implémentation nécessaire)")
        # Logique pour évaluer les mains et déterminer le gagnant.
