from Controller.Partie import Partie

if __name__ == "__main__":
    print("Decruyenaere Hugo - Caron Florimond") 
    noms_joueurs = ["Alice", "Bob", "Charlie"]
    partie = Partie(noms_joueurs)
    partie.jouer(nombre_manches=5)
