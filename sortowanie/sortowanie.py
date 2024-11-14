import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QCheckBox, QPushButton

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Sortowanie')
        self.setGeometry(50, 50, 300, 200)

        self.tekst = QLineEdit(self)
        self.tekst.setPlaceholderText("Wpisz liczby po przecinku...")
        self.tekst.resize(260, 20)
        self.tekst.move(20, 20)

        self.chk = QCheckBox("Checkbox", self)
        self.chk.move(110, 45)

        btn = QPushButton("Sortuj", self)
        btn.move(110, 70)
        btn.clicked.connect(self.buttonClicked)

        self.label = QLabel("Sortowanie Liczb: ", self)
        self.label.move(20, 95)


    def buttonClicked(self):
        splited = self.tekst.text().split(',')
        numbers = [int(i) for i in splited]
        numbers.sort()

        if self.chk.isChecked():
            numbers.reverse()
            joined = ','.join(str(i) for i in numbers)
            self.label.setText("Posortowane malejąco: " + joined)
        else:
            numbers.sort()
            joined = ','.join(str(i) for i in numbers)
            self.label.setText("Posortowane rosnąco: " + joined)

        self.label.adjustSize()

app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
