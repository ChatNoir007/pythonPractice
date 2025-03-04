import random
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
import sys
from PyQt6.uic import loadUi

class Dialog(QDialog):
    def __init__(self, main_window):
        super().__init__()
        loadUi("dialog.ui", self)
        self.main_window = main_window
        self.pushButton.clicked.connect(self.liniowa)

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


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("mainwindow.ui", self)

        self.pushButton.clicked.connect(self.btnGuess)
        self.number = random.randint(1, 50)
        self.actionLiniowa.triggered.connect(self.initLiniowa)

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


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
