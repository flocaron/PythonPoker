from Controller.Partie import Partie

if __name__ == "__main__":
    noms_joueurs = ["Alice", "Bob", "Charlie"]
    partie = Partie(noms_joueurs)
    partie.jouer(nombre_manches=5)
