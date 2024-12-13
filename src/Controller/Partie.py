from Controller.Table import Table
from Controller.Deck import Deck
from Model.Joueur import Joueur


class Partie:

    def __init__(self, joueurs, jetons_par_defaut=100):
        self.table = Table()
        self.deck = Deck()
        self.joueurs = [Joueur(nom, jetons_par_defaut) for nom in joueurs]
        self.mise_minimale = 10
        self.blind_petite = self.mise_minimale
        self.blind_grosse = self.mise_minimale * 2

        self.phases = {
            "flop": self.flop,
            "turn": self.turn,
            "river": self.river,
            "determiner_gagnant": self.determiner_gagnant
        }

        self.actions = {
            "se_coucher": self.se_coucher,
            "miser": self.miser,
            "parole": self.parole,
            "suivre": self.suivre
        }



    def jouer(self):
        print("Début de la partie.")
        self.deck.melanger()
        self.distribuer_cartes()
        self.gestion_blinds()  

        for name, function in self.phases.items():
            self.tour()
            function()
    def gestion_blinds(self):
        # Appliquer les blinds
        self.joueurs[0].miser(self.blind_petite)
        self.table.ajouter_mise(self.blind_petite)
        print(f"{self.joueurs[0].nom} a misé la petite blind de {self.blind_petite} jetons.")

        self.joueurs[1].miser(self.blind_grosse)
        self.table.ajouter_mise(self.blind_grosse)
        print(f"{self.joueurs[1].nom} a misé la grosse blind de {self.blind_grosse} jetons.")

        # Faire jouer les deux joueurs qui ont misé les blinds
        self.tour_joueur(self.joueurs[0])  # Premier joueur
        self.tour_joueur(self.joueurs[1])  # Deuxième joueur




    # Gestion du tour d'un joueur

    def tour(self):
        for joueur in self.joueurs:
            self.tour_joueur(joueur)

    def tour_joueur(self, joueur):
        self.table.afficher()
        joueur.debut_tour()
        joueur.afficher_cartes()

        
        # Afficher les options
        if joueur.mise_actuelle == self.table.derniere_mise:
            print("<parole> ", end=" ")
        else:
            print("<suivre> ", end=" ")

        print("<miser> <se_coucher>")

        choix = input("> ")

        while choix not in self.actions.keys():
            print('Mauvais Choix')
            choix = input("> ")

        action_method = self.actions[choix]
        action_method(joueur)

        # Vérifier si tous les joueurs ont la même mise
        if self.verifier_mises():
            print("Tous les joueurs ont la même mise, passage à la phase suivante.")
            return
       
    def verifier_mises(self):
        mises = [j.mise_actuelle for j in self.joueurs if j.actif]
        return len(set(mises)) == 1  # Tous les joueurs actifs ont la même mise


    def se_coucher(self, joueur):
        joueur.se_coucher()
        joueur.actif = False
        print(f"{joueur.nom} s'est couché.")
        

    def miser(self, joueur):
        montant = int(input("Saisissez le montant que vous voulez miser (ajoutez à la mise précédente).\nMise> "))
        montant_total = joueur.miser(montant + self.table.derniere_mise)

        while not montant_total:
            print("Misez une somme possible")
            montant = int(input("Saisissez le montant que vous voulez miser (ajoutez à la mise précédente).\nMise> "))
            montant_total = joueur.miser(montant + self.table.derniere_mise)

        self.table.ajouter_mise(montant_total)

    def suivre(self, joueur):
        montant = self.table.derniere_mise - joueur.mise_actuelle
        if montant > joueur.jetons:
            print(f"{joueur.nom} ne peut pas suivre, pas assez de jetons.")
            return
        joueur.miser(montant)
        self.table.ajouter_mise(montant)
        print(f"{joueur.nom} a suivi avec {montant} jetons.")

    def parole(self, joueur):
        if joueur.mise_actuelle == self.table.derniere_mise:
            joueur.parole()
        else:
            print("Vous ne pouvez pas faire parole, vous devez suivre.")






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
