import random

class Dice():
    def __init__(self, faces):
        self.faces = faces
        self.is_double = False

    def __str__(self):
        return f"Je suis un de à {self.faces} faces"

    def roll_double_dice(self):
        self.is_double = False
        a, b = random.randint(1, self.faces), random.randint(1, self.faces)
        if a == b:
            self.is_double = True
        return a, b, self.is_double

