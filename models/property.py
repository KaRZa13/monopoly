class Property:
    def __init__(self, name, cost, rent, owner=None):
        self.name = name
        self.cost = cost
        self.rent = rent
        self.owner = owner

    def buy(self, player):
        pass

    def pay_rent(self, player):
        pass