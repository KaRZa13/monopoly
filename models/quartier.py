import mysql

class Quartier:
    def __init__(self, couleur, prixMaison=0):
        self.__couleur = couleur
        self.__prixMaison = prixMaison
        self.lesProprietesDuQuartier = []

    def ajouterPropriete(self, laPropriete):
        self.lesProprietesDuQuartier.append(laPropriete)
        
    def __str__(self):
        if self.__prixMaison == 0:
            resultat = f"Quartier {self.__couleur}"
        else:
            resultat = f"Quartier {self.__couleur} - Prix d'une maison : {self.__prixMaison}€"

        if len(self.lesProprietesDuQuartier) == 0:
            resultat = resultat + " - Aucune propriété"
        else:
            resultat = resultat + f" - {len(self.lesProprietesDuQuartier)} propriété(s):"
            for p in self.lesProprietesDuQuartier:
                resultat = resultat + '\n' + str(p)
            
        return resultat
