import random

import pyqtgraph
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
import sys
from PyQt6.uic import loadUi

class Dialog(QDialog):
    def __init__(self, main_window):
        super().__init__()
        uic.loadUi("dialog.ui", self)
        self.main_window = main_window

    def liniowa(self):
        try:
            a = int(self.lineEdit.text())
            b = int(self.lineEdit_2.text())
            x = int(self.lineEdit_3.text())
            wspolczynnik = ""
            if(a>0):
                wspolczynnik = "rosnąca"
            elif(a<0):
                wspolczynnik = "malejąca"
            else:
                wspolczynnik = "stała"
            wzor = a * x + b
            self.main_window.label_wynik.setText("f(x) = " + str(wzor)+"\nfunkcja jest " + str(wspolczynnik))
        except:
            self.main_window.label_wynik.setText("złe wartości")

class KwadratowaDialog(QDialog):
    def __init__(self, main_window):
        super().__init__()
        uic.loadUi("kwadratowa.ui", self)
        self.main_window = main_window
        self.pushButton.clicked.connect(self.kwadratowa)


    def kwadratowa(self):
        self.a = int(self.lineEdit.text())
        self.b = int(self.lineEdit_2.text())
        self.c = int(self.lineEdit_3.text())
        self.x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.y = []
        for i in self.x:
            self.y.append((self.a * i) * (self.a * i) + self.b * i + self.c)
        self.kwadratowaWidget.plot(self.x, self.y)



class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("mainwindow.ui", self)

        self.pushButton.clicked.connect(self.btnGuess)
        self.number = random.randint(1, 50)
        self.actionLiniowa.triggered.connect(self.initLiniowa)
        self.actionKwadratowa.triggered.connect(self.initKwadratowa)

        self.a = 0
        self.b = 0
        self.kwadratowaWidget = pyqtgraph.PlotWidget()
        self.setCentralWidget(self.kwadratowaWidget)

    def btnGuess(self):
        message = QMessageBox(self)

        try:
            guess = int(self.lineEdit.text())
            if(guess == self.number):
                message.setText("Liczba zgadnięta")
            elif(guess > self.number):
                message.setText("Wpisz mniejszą liczbe")
            elif(guess < self.number):
                message.setText("Wpisz większą liczbę")
        except:
            message.setText("To nie liczba")

        message.exec()

    def initLiniowa(self):
        dialog = Dialog(self)
        dialog.exec()

    def initKwadratowa(self):
        self.KwadratowaDialog = KwadratowaDialog(self)
        self.KwadratowaDialog.exec()









app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
