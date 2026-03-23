from ia.couleur_rouge import apprentissage, liste_entrees_objectifs
from ia.neurone import activation
from data.data import lire, ecrire

class Neurone:

    def __init__(self):
        self.etat = lire("neurone")
        if not self.etat:
            self.init_neurone() 

    def init_neurone(self):
        donnees = lire("donnees_entrainement")
        if not donnees:
            donnees = self.init_donnees()
        self.etat = apprentissage(donnees)
        ecrire("neurone", self.etat)

    def init_donnees(self):
        ecrire("donnees_entrainement",liste_entrees_objectifs)
        return liste_entrees_objectifs

    def is_red(self,color):
        return activation(self.etat, color)
    
    def update(self,color,is_red):
        donnees_entrainement = lire("donnees_entrainement")
        if not donnees_entrainement:
            donnees_entrainement = self.init_donnees()

        donnees_entrainement.append((color,is_red))
        ecrire("donnees_entrainement",donnees_entrainement)


        self.etat = apprentissage(donnees_entrainement)
        ecrire("neurone",self.etat)
        