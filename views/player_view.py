from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class PlayerView(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(300, 200)
        self.layout = QVBoxLayout()

        self.name_label = QLabel(f'Nom : {self.player.name}')
        self.balance_label = QLabel(f'Solde : {self.player.balance}')
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.balance_label)

        self.properties_label = QLabel(f'Propriété :')
        self.layout.addWidget(self.properties_label)