class Joueur:

    def __init__(self, nom, jetons):
        self.nom = nom
        self.jetons = jetons
        self.main = []
        self.actif = True

    def recevoir_carte(self, carte):
        self.main.append(carte)





    # Affichage

    def __str__(self):
        etat = "Actif" if self.actif else "Couché"
        return f"{self.nom} ({etat}) - Jetons: {self.jetons} - Main: {', '.join(str(c) for c in self.main)}"

    def debut_tour(self):
        print("-- Tour de " + self.nom + " - " + str(self.jetons) + "$ --")

    def afficher_cartes(self):
        for carte in self.main:
            print(carte, end=" ")
        print()






    # function tour d'un joueur

    def se_coucher(self):
        self.actif = False

    def miser(self, montant):
        if montant > self.jetons:
            return False
        self.jetons -= montant
        return montant
    
    def parole(self):
        print("Check ...")
    


