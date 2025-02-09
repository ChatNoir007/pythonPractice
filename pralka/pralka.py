from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
import sys
from PyQt6.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Okienko")
        self.setGeometry(300,300,400,400)

        label = QLabel(self)
        label.setText("Urządzenia domowe")
        label.setStyleSheet("font-size: 24px;")
        label.move(90,10)

        author = QLabel(self)
        author.setText("Autor: Wojciech Lipiec")
        author.setStyleSheet("font-size: 16px;")
        author.move(120,50)


        img_label = QLabel(self)
        pixmap = QPixmap("pralka.jpg")
        img_label.setPixmap(pixmap.scaledToWidth(150))
        img_label.move(50,100)

        pralka = QLabel(self)
        pralka.setText("Pralka")
        pralka.setStyleSheet("font-size: 20px;")
        pralka.move(220,100)
        pralka.adjustSize()

        number = QLineEdit(self)
        number.setPlaceholderText("podaj nr. prania 1..12")
        number.move(220,140)
        number.adjustSize()

        btn1 = QPushButton(self)
        btn1.setText("Zatwierdź")
        btn1.setGeometry(220,220,100,40)

app = QApplication(sys.argv)
window = Window()
window.show()

app.exec()