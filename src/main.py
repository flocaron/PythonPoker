from Controller.Partie import Partie


if __name__ == "__main__":
    # Noms des joueurs
    noms_joueurs = ["Alice", "Bob", "Charlie"]
    
    # Initialisation et démarrage de la partie
    partie = Partie(noms_joueurs)


    partie.demarrer()

    # Afficher l'état des joueurs et de la table
    for joueur in partie.joueurs:
        print(joueur)
    print(partie.table)

