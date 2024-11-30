from PyQt5.QtWidgets import QWidget, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtCore import QRectF


class BoardView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        # Dimension du plateau
        self.setFixedSize(600, 600)
        self.scene.setSceneRect(0, 0, 500, 500)

        # Dessiner le plateau
        self.draw_board()

    def draw_board(self):
        scene_width = self.scene.sceneRect().width()
        scene_height = self.scene.sceneRect().height()
        grid_size = 10
        size = min(scene_width, scene_height) / grid_size

        for i in range(grid_size):
            self.scene.addRect(i * size, 0, size, size)
            self.scene.addRect(i * size, (grid_size - 1) * size, size, size)
            self.scene.addRect(0, i * size, size, size)
            self.scene.addRect((grid_size - 1) * size, i * size, size, size)
