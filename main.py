from PyQt5.QtWidgets import QApplication
from views.main_window import MainWindow
from models.game import Game
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())