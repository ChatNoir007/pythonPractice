from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
import sys
from PyQt6.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Okienko")
        self.setGeometry(300, 300, 400, 500)

        label = QLabel(self)
        label.setText("Urządzenia domowe")
        label.setStyleSheet("font-size: 24px;")
        label.move(90, 10)

        author = QLabel(self)
        author.setText("Autor: Wojciech Lipiec")
        author.setStyleSheet("font-size: 16px;")
        author.move(120, 50)

        img_pralka = QLabel(self)
        pixmap = QPixmap("pralka.jpg")
        img_pralka.setPixmap(pixmap.scaledToWidth(150))
        img_pralka.move(50, 100)

        pralka = QLabel(self)
        pralka.setText("Pralka")
        pralka.setStyleSheet("font-size: 20px;")
        pralka.move(220, 100)
        pralka.adjustSize()

        self.number_edit = QLineEdit(self)
        self.number_edit.setPlaceholderText("podaj nr. prania 1..12")
        self.number_edit.move(220, 140)
        self.number_edit.adjustSize()

        btn1 = QPushButton(self)
        btn1.setText("Zatwierdź")
        btn1.setGeometry(220, 180, 100, 30)
        btn1.clicked.connect(self.laundry)

        self.number_label = QLabel(self)
        self.number_label.setText("Numer prania: nie podano")
        self.number_label.move(220, 220)
        self.number_label.adjustSize()

        img_odkurz = QLabel(self)
        pixmap = QPixmap("odkurzacz.jpg")
        img_odkurz.setPixmap(pixmap.scaledToWidth(150))
        img_odkurz.move(50, 300)

        odkurzacz = QLabel(self)
        odkurzacz.setText("Odkurzacz")
        odkurzacz.setStyleSheet("font-size: 20px;")
        odkurzacz.move(220, 300)
        odkurzacz.adjustSize()

        self.btn2 = QPushButton(self)
        self.btn2.setText("Włącz")
        self.btn2.setGeometry(220, 340, 100, 30)
        self.btn2.clicked.connect(self.vacuum)

        self.odkurz_dziala = QLabel(self)
        self.odkurz_dziala.setText("Odkurzacz wyłączony")
        self.odkurz_dziala.move(220, 380)
        self.odkurz_dziala.adjustSize()

        self.odkurz_status = QLabel(self)
        self.odkurz_status.setText("Status: naładowany")
        self.odkurz_status.move(220, 410)

    def laundry(self):
        num = self.number_edit.text()
        if num.isdigit():
            num = int(num)
            if 1 <= num <= 12:
                self.number_label.setText(f"Numer prania: {num}")
            else:
                self.number_label.setText("Podaj liczbę 1-12")
        else:
            self.number_label.setText("Nie podano liczby")
        self.number_label.adjustSize()

    def vacuum(self):
        if self.btn2.text() == "Włącz":
            self.btn2.setText("Wyłącz")
            self.odkurz_dziala.setText("Odkurzacz włączony")
        else:
            self.btn2.setText("Włącz")
            self.odkurz_dziala.setText("Odkurzacz wyłączony")
        self.btn2.adjustSize()
        self.odkurz_dziala.adjustSize()


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
