from Controller.Table import Table
from Controller.Deck import Deck
from Model.Joueur import Joueur


class Partie:

    def __init__(self, joueurs, jetons_par_defaut=100):
        self.table = Table()
        self.deck = Deck()
        self.joueurs = [Joueur(nom, jetons_par_defaut) for nom in joueurs]

        self.phases = {
            "flop": self.flop,
            "turn": self.turn,
            "river": self.river,
            "determiner_gagnant": self.determiner_gagnant
        }

        self.actions = {
            "se_coucher": self.se_coucher,
            "miser": self.miser,
            "parole": self.parole
        }



    def jouer(self):
        print("Début de la partie.")
        self.deck.melanger()
        self.distribuer_cartes()

        for name, function in self.phases.items():
            self.tour()
            function()




    # Gestion du tour d'un joueur

    def tour(self):
        for joueur in self.joueurs:
            self.tour_joueur(joueur)

    def tour_joueur(self, joueur):
        self.table.afficher()
        joueur.debut_tour()
        joueur.afficher_cartes()

        for name, method in self.actions.items():
            print(f"<{name}> ", end=" ")
        print("")

        choix = input("> ")

            
        while choix not in self.actions.keys():
            print('Mauvais Choix')
            choix = input("> ")

        action_method = self.actions[choix]
        action_method(joueur)






    # Fonctions choix du joueur
    
    def se_coucher(joueur):
        joueur.se_coucher()
    
    def miser(self, joueur):

        montant = joueur.miser(int(input("Saisissez Le montant que vous voulez miser.\nMise> ")))

        while not montant:
            print("Misez une somme possible")
            montant = joueur.miser(int(input("Saisissez Le montant que vous voulez miser.\nMise> ")))

        self.table.ajouter_mise(montant)

    def suivre(self, joueur):
        raise Exception("Not implemented Yet")


    def parole(self, joueur):
        joueur.parole()






    # Fonctions des phases

    def distribuer_cartes(self):
        for joueur in self.joueurs:
            for _ in range(2):  # Chaque joueur reçoit 2 cartes
                joueur.recevoir_carte(self.deck.piocher())

    def flop(self):
        print("Distribution du Flop...")
        for _ in range(3):  # Le flop : 3 cartes
            self.table.ajouter_carte_commune(self.deck.piocher())

    def turn(self):
        print("Distribution du Turn...")
        self.table.ajouter_carte_commune(self.deck.piocher())

    def river(self):
        print("Distribution de la River...")
        self.table.ajouter_carte_commune(self.deck.piocher())

    def determiner_gagnant(self):
        print("Déterminer le gagnant... (implémentation nécessaire)")
        # Logique pour évaluer les mains et déterminer le gagnant.
