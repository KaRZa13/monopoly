class Propriete:
    def __init__(self,price,name,mortage_value):
        self.price = price
        self.name = name
        self.mortage_value = mortage_value
        self.mortage = False

class Terrain(Propriete):

    def __init__(self, price, name, mortage_value, rent, housenbr):
        super().__init__(price, name, mortage_value)
        self.rent = rent
        self.housenbr = housenbr