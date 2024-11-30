from neighborhood import Neighborhood

class Property:
    def __init__(self, name, price, rent: list[int], owner=None):
        self.name = name
        self.price = price
        self.rent = rent
        self.mortage_value = self.price/2
        self.mortage = False
        self.owner = owner

    def buy(self, player):
        pass

class Terrain(Property):
    def __init__(self, name, rent, price, owner=None):
        super().__init__(name, price, rent, owner)
        self.houseNbr = 0

class Station(Property):
    def __init__(self, name, rent, price, owner=None):
        super().__init__(name, price, rent, owner)

class Company(Property):
    def __init__(self, name, rent, price, owner=None):
        super().__init__(name, price, rent, owner)


noir = Neighborhood('noir', 'noir', 0)
bleu = Neighborhood('bleu', 'blue', 150)
montparnasse = Station('Montparnasse', [1, 2, 3, 4, 5], 200, None)
rue_de_la_paix = Terrain('Rue de la paix', [1, 2, 3, 4, 5], 200, None)
champ = Terrain('Champ Elysée', [1, 2, 3, 4, 5], 200, None)
noir.add_property(montparnasse)
bleu.add_property(champ)
bleu.add_property(rue_de_la_paix)
print(bleu)
print(noir)
