import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QCheckBox, QPushButton


class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Okienko')
        self.setGeometry(50,50,300,200)

        self.tekst = QLineEdit(self)
        self.tekst.setPlaceholderText("Tekst...")
        self.tekst.resize(260, 20)
        self.tekst.move(20, 20)

        btn = QPushButton("Wyświetl", self)
        btn.move(110, 45)
        btn.clicked.connect(self.buttonClicked)

        self.label = QLabel("Wpisany tekst: ", self)
        #self.label.setFixedSize(200, 200)
        self.label.move(20, 70)

        self.chk = QCheckBox("Checkbox", self)
        self.chk.move(20, 95)
        self.chk.toggled.connect(self.chkToggled)

    def buttonClicked(self):
        self.label.setText("Wpisany tekst: " + self.tekst.text())
        self.label.adjustSize()
        print(self.chk.isChecked())

    def chkToggled(self, checked):
        if checked:
            print("Włączony")
        else:
            print("Wyłączony")

app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
