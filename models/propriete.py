class Propriete:
    def __init__(self, price, name):
        self.name = name
        self.price = price
        self.mortage_value = self.price/2
        self.mortage = False

class Terrain(Propriete):
    def __init__(self, price, name, rent: list, housenbr):
        super().__init__(price, name)
        self.rent = rent
        self.housenbr = housenbr

class Station(Propriete):
    def __init__(self, price, name):
        super().__init__(price, name)
