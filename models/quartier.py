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

    @classmethod
    def connexionBase(cls):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database = "monopoly",
        )
        return mydb


    @classmethod
    def creationTable(cls):
        maConnexion = Quartier.connexionBase()
        monCurseur = maConnexion.cursor()
        monCurseur.execute("""
            CREATE TABLE QUARTIERS (
            id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
            couleur VARCHAR(255),
            prixMaison INT
            );""")
        
    @classmethod
    def suppressionTable(cls):
        maConnexion = Quartier.connexionBase()
        monCurseur = maConnexion.curseur()
        monCurseur.execute("DROP TABLE quartiers")
# combien y a -t-il de proprietes dans le quartier ?

# combien un jour a-t-il de proprietes dans le quartier ?

if __name__ == '__main__':
    quartierBleu = Quartier("Bleu", 200)
    print(quartierBleu)
    quartierGares = Quartier("Noir")
    print(quartierGares)