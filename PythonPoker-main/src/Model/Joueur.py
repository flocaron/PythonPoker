class Joueur:

    def __init__(self, nom, jetons):
        self.nom = nom
        self.jetons = jetons
        self.main = []
        self.actif = True
        self.mise_actuelle = 0
        

    def recevoir_carte(self, carte):
        self.main.append(carte)





    # Affichage

    def __str__(self):
        etat = "Actif" if self.actif else "Couché"
        return f"{self.nom} ({etat}) - Jetons: {self.jetons} - Main: {', '.join(str(c) for c in self.main)}"

    def debut_tour(self):
        print("-- Tour de " + self.nom + " --")

    def afficher_cartes(self):
        for carte in self.main:
            print(carte, end=" ")
        print()






    # function tour d'un joueur

    def se_coucher(self):
        self.actif = True

    def miser(self, montant):
        if montant > self.jetons:
            return False
        self.jetons -= montant
        self.mise_actuelle += montant
        return montant
    
    def parole(self):
        print("Check ...")
    


