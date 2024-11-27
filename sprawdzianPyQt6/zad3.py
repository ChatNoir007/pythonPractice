from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QTextEdit, QCheckBox
import sys
from PyQt6.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("sprawdzian")
        self.setGeometry(300,300,400,400)

        self.chk = QCheckBox(self)
        self.chk.clicked.connect(self.check)
        self.chk.move(100,100)
        self.chk.setText("czekbox")


    def check(self):
        if (self.chk.isChecked()):
            print("Checkbox włączony")
        else:
            print("Checkbox wyłączony")


app = QApplication(sys.argv)
window = Window()
window.show()

app.exec()