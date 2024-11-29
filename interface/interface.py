from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsEllipseItem, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor

import random 
import sys

class MonopolyInterface(QMainWindow):
    def __init__(self):
        super().__init__()

        #Main window
        self.setWindowTitle("Monopoly tah le game")
        self.setGeometry(100, 100, 900, 900)

        #Drawing zone
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene, self)
        self.view.setGeometry(100, 100, 900, 900)

        #Draw Player
        self.pion = QGraphicsEllipseItem(10,10,20,20)
        self.pion.setBrush(QBrush(QColor("red")))
        self.scene.addItem(self.pion)
        self.current_position = 0

        self.pion2 = QGraphicsEllipseItem(10,10,20,20)
        self.pion2.setBrush(QBrush(QColor("blue")))
        self.scene.addItem(self.pion2)
        self.current_position = 1

        #buttons
        self.roll_button = QPushButton("Launch dices")
        self.roll_button.setGeometry(350, 870, 200, 30)
        #self.roll_button.clicked.connect()

        self.property_button = QPushButton("Buy property")
        self.property_button.setGeometry(100, 870, 200, 30)
        #self.property_button.clicked.connect()

        self.draw_board()



    def draw_board(self):
        size = 80
        for i in range(10):
            self.scene.addRect(i*size, 0, size, size)
            self.scene.addRect(i*size, 720, size, size)
            self.scene.addRect(0, i*size, size, size)
            self.scene.addRect(720, i*size, size, size)



app = QApplication(sys.argv)
game = MonopolyInterface()
game.show()
sys.exit(app.exec_())
