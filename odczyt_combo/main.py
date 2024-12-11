import json
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QComboBox, QPushButton, QGridLayout, QFormLayout


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Lista')
        self.setGeometry(50, 50, 300, 200)

        file = open("dane4P.txt", "r", encoding="utf-8")
        self.loading = json.loads(file.read())

        self.cmb = QComboBox()
        self.btn = QPushButton()

        self.cmb.addItems(self.loading)
        self.btn.clicked.connect(self.btnClicked)

        layout = QFormLayout(self)
        layout.addRow(self.cmb)
        layout.addRow(self.btn)

    def btnClicked(self):
        print(self.loading[self.cmb.currentText()])






app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
