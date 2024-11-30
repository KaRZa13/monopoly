class Player:
    def __init__(self, balance):
        self.balance = balance
        

    def move(self, steps):
        pass

    def buy_property(self, property):
        pass

    def pay(self, amount):
        self.balance -= amount
        print(f"{self.name} a payé {amount}€. Nouveau solde : {self.balance}€")

    def receive(self, amount):
        self.balance += amount
        print(f"{self.name} a reçu {amount}€. Nouveau solde : {self.balance}€")

    def __str__(self):
        result = f"{self.name} - Solde : {self.balance}€\n"
        if not self.properties:
            result += "Aucune propriété.\n"
        else:
            result += "Propriétés :\n"
            for prop in self.properties:
                result += f"  - {prop.name} (Hypothèque : {'Oui' if prop.mortage else 'Non'})\n"
        return result
    
class HumanPlayer(Player):
    def __init__(self, name, balance):
        super().__init__(balance)
        self.name = name
        self.position = 0
        self.pawn = None
        self.properties = []

class Bank(Player):
    def __init__(self, balance):
        super().__init__(balance)
