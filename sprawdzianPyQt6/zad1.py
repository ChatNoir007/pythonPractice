from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
import sys
from PyQt6.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("sprawdzian")
        self.setGeometry(300,300,400,400)

        self.label = QLabel(self)
        self.label.setText("dowolny text")
        self.label.move(120,20)

        btn1 = QPushButton(self)
        btn1.setText("jeden")
        btn1.move(50, 250)
        btn1.clicked.connect(self.btnWcisniety1)

        btn2 = QPushButton(self)
        btn2.setText("dwa")
        btn2.move(150, 250)
        btn2.clicked.connect(self.btnWcisniety2)

        btn3 = QPushButton(self)
        btn3.setText("trzy")
        btn3.move(250, 250)
        btn3.clicked.connect(self.btnWcisniety3)


    def btnWcisniety1(self):
        img = QPixmap("1.png")
        self.label.setPixmap(img)
        self.label.adjustSize()

    def btnWcisniety2(self):
        img = QPixmap("2.png")
        self.label.setPixmap(img)
        self.label.adjustSize()

    def btnWcisniety3(self):
        img = QPixmap("3.png")
        self.label.setPixmap(img)
        self.label.adjustSize()

app = QApplication(sys.argv)
window = Window()
window.show()

app.exec()