import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt6.QtGui import QPixmap

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Okienko')
        self.setGeometry(300, 300, 500, 500)

        btnL = QPushButton(self)
        btnL.setText("<-")
        btnL.move(100, 450)
        btnL.clicked.connect(self.btnLClicked)

        btnD = QPushButton(self)
        btnD.setText("Dane Techniczne/Opis")
        btnD.move(190, 450)
        btnD.clicked.connect(self.btnDClicked)

        btnR = QPushButton(self)
        btnR.setText("->")
        btnR.move(330, 450)
        btnR.clicked.connect(self.btnRClicked)

        self.audi = {
            "image": "audi.jpg",
            "specs": "2.0 40 TDI 163KM 120kW Diesel",
            "desc": "Bardzo porządna, bezawaryjna limuzyna klasy wyższej średniej"
        }
        self.volkswagen = {
            "image": "volkswagen.jpg",
            "specs": "2.0 TDI 190KM 140kW Diesel",
            "desc": "Porządna, bezawaryjna limuzyna klasy średniej"
        }
        self.mercedes = {
            "image": "mercedes.jpg",
            "specs": "3.0 SOHC 160KM 117,5kW",
            "desc": "Luksusowa limuzyna z dawnych lat o dużej wytrzymałości"
        }

        self.cars = [self.audi, self.volkswagen, self.mercedes]
        self.i = 0
        self.show_specs = True

        self.label = QLabel(self)
        self.label.move(80, 350)

        self.img_label = QLabel(self)
        self.update_picture()


    def update_picture(self):
        pixmap = QPixmap(self.cars[self.i]["image"])
        self.img_label.setPixmap(pixmap.scaledToWidth(500))
        self.img_label.move(0, 20)

        self.label.setText(self.cars[self.i]["specs"])
        self.show_specs = True

        self.label.adjustSize()

    def update_desc(self):
        if self.show_specs:
            self.label.setText(self.cars[self.i]["desc"])
            self.show_specs = False
        else:
            self.label.setText(self.cars[self.i]["specs"])
            self.show_specs = True

        # print(self.show_specs)
        # print(self.label.text())
        self.label.adjustSize()

    def btnLClicked(self):
        # print("W LEWO")
        self.label.adjustSize()
        self.i = (self.i - 1) % len(self.cars)
        self.update_picture()

    def btnRClicked(self):
        # print("W PRAWO")
        self.label.adjustSize()
        self.i = (self.i + 1) % len(self.cars)
        self.update_picture()

    def btnDClicked(self):
        # print("ZMIANA OPISU")
        self.update_desc()


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
