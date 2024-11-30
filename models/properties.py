class Property:
    def __init__(self, name, price, rent: list[int], owner=None):
        self.name = name
        self.price = price
        self.rent = rent
        self.mortage_value = self.price/2
        self.mortage = False
        self.owner = owner

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
