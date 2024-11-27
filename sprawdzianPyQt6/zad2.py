from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QTextEdit
import sys
from PyQt6.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("sprawdzian")
        self.setGeometry(300,300,400,400)

        self.edit1 = QLineEdit(self)
        self.edit1.move(50,50)
        self.edit1.setPlaceholderText("imie")

        self.edit2 = QLineEdit(self)
        self.edit2.move(50, 100)
        self.edit2.setPlaceholderText("nazwisko")

        self.edit3 = QLineEdit(self)
        self.edit3.move(50, 150)
        self.edit3.setPlaceholderText("klasa")

        btn = QPushButton(self)
        btn.setText("Zatwierdź")
        btn.move(100,200)
        btn.clicked.connect(self.btn)

    def btn(self):
        print("imie: " + self.edit1.text())
        print("nazwisko: " + self.edit2.text())
        print("klasa: " + self.edit3.text())


app = QApplication(sys.argv)
window = Window()
window.show()

app.exec()