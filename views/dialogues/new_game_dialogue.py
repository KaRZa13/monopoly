from PyQt5.QtWidgets import QDialog, QFormLayout, QSpinBox, QDialogButtonBox

class NewGameDialogue(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Nouvelle partie')
        self.setFixedSize(300, 150)

        self.layout = QFormLayout()
        self.num_players_spinbox = QSpinBox()
        self.num_players_spinbox.setRange(2, 6)
        self.layout.addRow('Nombre de joueurs : ', self.num_players_spinbox)

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        self.layout.addWidget(self.button_box)
        self.setLayout(self.layout)

    def get_num_players(self):
        return self.num_players_spinbox.value()