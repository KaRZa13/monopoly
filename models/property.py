class Neighborhood:
    def __init__(self, name, color, house_price=0):
        self.name = name
        self.color = color
        self.house_price = house_price
        self.properties = []

    def add_property(self, property_):
        self.properties.append(property_)

    def is_monopoly(self, player):
        if not self.properties:
            return False
        return all(prop.owner == player for prop in self.properties)

    def __str__(self):
        result = f"Quartier {self.color} - Prix d'une maison : {self.house_price}€\nPropriétés :\n"
        for prop in self.properties:
            result += f"- {prop.name} (Propriétaire : {prop.owner if prop.owner else 'Libre'})\n"
        return result

class Property:
    def __init__(self, name, rent: list, price=0, owner=None):

        self.name = name
        self.price = price
        self.rent = rent
        self.mortage_value = self.price/2
        self.mortage = False
        self.owner = owner

    def buy(self, player):
        pass

class Terrain(Property):
    def __init__(self, name, rent, houseNbr, price=0, owner=None):
        super().__init__(name, price, rent, owner)
        self.houseNbr = houseNbr

class Station(Property):
    def __init__(self, name, rent, price=0, owner=None):
        super().__init__(name, price, rent, owner)

class Company(Property):
    def __init__(self, name, rent, price=0, owner=None):
        super().__init__(name, price, rent, owner)




