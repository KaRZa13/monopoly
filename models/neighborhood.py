class Neighborhood:
    def __init__(self, color, house_price):
        self.id = None
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
        result = f"Quartier {self.color} - Prix d'une maison : {self.house_price}€\nProprietes :\n"
        for prop in self.properties:
            result += f"- {prop.name} (Proprietaire : {prop.owner if prop.owner else 'Libre'})\n"
        return result
