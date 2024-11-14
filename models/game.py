from models.player import Player
from models.board import Board

class Game: 
    def __init__(self):
        self.board = Board()
        self.players = []

    def start(self):
        print("La partie commence !")

        # Boucle de jeu