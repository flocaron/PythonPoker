from Controller.Manche import Manche
from Model.Joueur import Joueur


class Partie:

    def __init__(self, noms_joueurs, jetons_par_defaut=100):
        self.joueurs = [Joueur(nom, jetons_par_defaut) for nom in noms_joueurs]
        self.historique_manches = []


        

    def jouer(self, nombre_manches=3):
        print("Début de la partie.")

        for i in range(nombre_manches):
            print(f"\n--- Manche {i + 1} ---")
            manche = Manche(self.joueurs)
            gagnants = manche.jouer()
            self.historique_manches.append(gagnants)

            # Vérifier si un joueur est éliminé
            self.joueurs = [joueur for joueur in self.joueurs if joueur.jetons > 0]

            if len(self.joueurs) < 2:
                print("Partie terminée : nombre insuffisant de joueurs.")
                break

        print("\n--- Fin de la partie ---")
        self.afficher_resultats()




    def afficher_resultats(self):
        """Affiche les résultats de la partie."""
        print("Résultats des manches :")
        for i, gagnants in enumerate(self.historique_manches, start=1):
            if isinstance(gagnants, list):
                print(f"Manche {i} : Égalité entre {', '.join(gagnants)}.")
            else:
                print(f"Manche {i} : {gagnants} a gagné.")
