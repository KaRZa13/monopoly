# Models
from models.player import HumanPlayer, Bank
from models.neighborhood import Neighborhood
from models.properties import Terrain, Station, Company

# Views
from PyQt5.QtWidgets import QApplication
from views.main_window import MainWindow
from views.board_view import BoardView
from views.player_view import PlayerView
from views.dialogues.new_game_dialogue import NewGameDialogue

class Game: 
    def __init__(self, players: list):
        self.players = players
        self.current_player_index = 0

    def get_current_player(self):
        return self.player[self.current_player_index]

    def buy_property(self, property_):
        player = self.get_current_player()
        if player.buy_property(property_):
            print(f'{player.name} a acheté {property_.name} pour {property_.price}')
        else : 
            print(f'{player.name} n\'a pas assez d\'argent pour acheter {property_.name}')

    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        print(f"C'est au tour de {self.get_current_player().name}")
