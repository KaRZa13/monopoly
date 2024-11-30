from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QMenuBar, QAction
from views.board_view import BoardView
from views.dialogues.new_game_dialogue import NewGameDialogue


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Monopoly tah le game')
        self.setGeometry(100, 100, 1000, 800)

        # Menu
        self.menu_bar = QMenuBar()
        self.setMenuBar(self.menu_bar)

        # Ajoute des menus
        game_menu = self.menu_bar.addMenu('Jeu')
        new_game_action = QAction("Nouvelle Partie", self)
        # new_game_action.triggered.connect(self.start_new_game)
        game_menu.addAction(new_game_action)

        # Zone centrale
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Titre
        self.info_label = QLabel('Monopoly')
        self.layout.addWidget(self.info_label)

        # Plateau
        self.new_game_dialogue = NewGameDialogue()
        self.layout.addWidget(self.new_game_dialogue)