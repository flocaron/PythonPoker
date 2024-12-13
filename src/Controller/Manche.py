from Controller.Table import Table
from Controller.Deck import Deck


class Manche:

    def __init__(self, joueurs):
        self.table = Table()
        self.deck = Deck()
        self.joueurs = joueurs

    def jouer(self):
        print("Début d'une nouvelle manche.")
        self.deck.melanger()
        self.distribuer_cartes()

        # Forcer les blinds
        self.forcer_blinds()

        # Effectuer les phases du jeu
        self.phases()

        # Déterminer le ou les gagnants
        gagnant = self.determiner_gagnant()
        return gagnant

    def forcer_blinds(self):
        """Phase de blind obligatoire : chaque joueur doit miser ou se coucher."""
        print("Phase de blinds obligatoire : chaque joueur doit miser ou se coucher.")
        joueurs_actifs = self.joueurs.copy()

        for joueur in joueurs_actifs:
            choix = None
            while choix not in {"miser", "se_coucher"}:
                print(f"{joueur.nom}, vous devez miser ou vous coucher.")
                choix = input("Choix (miser/se_coucher) > ").strip().lower()

            if choix == "miser":
                self.miser(joueur)
            elif choix == "se_coucher":
                joueur.se_coucher()
                self.joueurs.remove(joueur)

    def phases(self):
        """Effectue les différentes phases du jeu."""
        print("Début des phases.")
        self.flop()
        self.tour()
        self.turn()
        self.tour()
        self.river()
        self.tour()

    def flop(self):
        """Distribution du Flop."""
        print("Distribution du Flop...")
        for _ in range(3):  # Le flop : 3 cartes
            self.table.ajouter_carte_commune(self.deck.piocher())

    def turn(self):
        """Distribution du Turn."""
        print("Distribution du Turn...")
        self.table.ajouter_carte_commune(self.deck.piocher())

    def river(self):
        """Distribution de la River."""
        print("Distribution de la River...")
        self.table.ajouter_carte_commune(self.deck.piocher())

    def tour(self):
        """Gère un tour des joueurs actifs."""
        print("Début du tour.")
        joueurs_actifs = self.joueurs.copy()

        while joueurs_actifs:
            joueur = joueurs_actifs.pop(0)
            self.table.afficher()
            joueur.debut_tour()
            joueur.afficher_cartes()

            choix = None
            while choix not in {"parole", "miser", "suivre", "se_coucher"}:
                print(f"{joueur.nom}, choisissez votre action.")
                print("<parole> <miser> <suivre> <se_coucher>")
                choix = input("> ").strip().lower()

            if choix == "parole":
                joueur.parole()
            elif choix == "miser":
                self.miser(joueur)
                self.gestion_mise(joueurs_actifs, joueur)
            elif choix == "suivre":
                self.suivre(joueur)
            elif choix == "se_coucher":
                joueur.se_coucher()
                self.joueurs.remove(joueur)



    def gestion_mise(self, joueurs_actifs, joueur_initial):
        """Gère les réponses des autres joueurs à une mise."""
        print(f"{joueur_initial.nom} a misé. Les autres joueurs doivent suivre ou se coucher.")
        for joueur in list(joueurs_actifs):  # Copier la liste pour modifications
            choix = None
            while choix not in {"suivre", "se_coucher"}:
                print(f"{joueur.nom}, choisissez votre action.")
                print("<suivre> <se_coucher>")
                choix = input("> ").strip().lower()

            if choix == "suivre":
                self.suivre(joueur)
            elif choix == "se_coucher":
                joueur.se_coucher()
                joueurs_actifs.remove(joueur)



    def distribuer_cartes(self):
        """Distribue deux cartes à chaque joueur."""
        for joueur in self.joueurs:
            for _ in range(2):
                joueur.recevoir_carte(self.deck.piocher())

    def determiner_gagnant(self):
        """
        Détermine le ou les gagnants de la manche.
        """
        # Liste pour garder les meilleurs joueurs en cas d'égalité
        meilleurs_joueurs = [self.joueurs[0]]

        for joueur in self.joueurs[1:]:
            meilleur_actuel = self.table.comparer_mains(meilleurs_joueurs[0], joueur)

            if meilleur_actuel == meilleurs_joueurs[0]:
                continue  # Le joueur actuel reste le meilleur
            elif meilleur_actuel == joueur:
                meilleurs_joueurs = [joueur]  # Nouveau meilleur joueur
            else:  # Égalité
                meilleurs_joueurs.append(joueur)

        # Résultat
        if len(meilleurs_joueurs) == 1:
            gagnant = meilleurs_joueurs[0]
            print(f"Le gagnant de la manche est {gagnant.nom} avec la meilleure main.")
            gagnant.recevoir_jetons(self.table.pot)
            self.table.pot = 0  # Réinitialiser le pot
            return gagnant.nom
        else:
            # Gestion des égalités
            print(f"Égalité entre {', '.join(j.nom for j in meilleurs_joueurs)}.")
            partage = self.table.pot // len(meilleurs_joueurs)
            for joueur in meilleurs_joueurs:
                joueur.recevoir_jetons(partage)
            self.table.pot = 0  # Réinitialiser le pot
            return [j.nom for j in meilleurs_joueurs]


    def miser(self, joueur):
        """Le joueur mise une somme."""
        try:
            montant = int(input("Saisissez le montant que vous voulez miser.\nMise> "))
            while not joueur.miser(montant):
                print("Misez une somme possible.")
                montant = int(input("Saisissez le montant que vous voulez miser.\nMise> "))
            self.table.ajouter_mise(montant)
        except ValueError:
            print("Veuillez entrer un montant valide.")
            self.miser(joueur)



    def suivre(self, joueur):
        """Le joueur suit la mise."""
        montant = self.table.derniere_mise
        if joueur.miser(montant):
            self.table.ajouter_mise(montant)
        else:
            print(f"{joueur.nom} ne peut pas suivre la mise de {montant}.")
            joueur.se_coucher()
