import sys
from PyQt6.QtWidgets import QSizePolicy, QApplication, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, \
    QLineEdit, QPushButton
from PyQt6.QtCore import Qt


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Okienko')
        self.setGeometry(50, 50, 300, 200)

        self.display = QLabel()
        self.display.setText("")

        btn1 = QPushButton("")
        btn2 = QPushButton("")
        btn3 = QPushButton("")
        btn4 = QPushButton("")
        btn5 = QPushButton("")
        btn6 = QPushButton("")
        btn7 = QPushButton("")
        btn8 = QPushButton("")
        btn9 = QPushButton("")

        self.btnTab = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]

        btn1.clicked.connect(self.btnTurn)
        btn2.clicked.connect(self.btnTurn)
        btn3.clicked.connect(self.btnTurn)
        btn4.clicked.connect(self.btnTurn)
        btn5.clicked.connect(self.btnTurn)
        btn6.clicked.connect(self.btnTurn)
        btn7.clicked.connect(self.btnTurn)
        btn8.clicked.connect(self.btnTurn)
        btn9.clicked.connect(self.btnTurn)

        self.display.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btn1.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btn2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btn3.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btn4.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btn5.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btn6.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btn7.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btn8.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btn9.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        layout = QGridLayout(self)
        layout.addWidget(self.display, 0, 0, 1, 5)
        layout.addWidget(btn7, 1, 0)
        layout.addWidget(btn8, 1, 1)
        layout.addWidget(btn9, 1, 2)
        layout.addWidget(btn4, 2, 0)
        layout.addWidget(btn5, 2, 1)
        layout.addWidget(btn6, 2, 2)
        layout.addWidget(btn1, 3, 0)
        layout.addWidget(btn2, 3, 1)
        layout.addWidget(btn3, 3, 2)

        self.turn = 0;
        self.list = [[btn1, btn2, btn3], [btn4, btn5, btn6], [btn7, btn8, btn9]]

    def btnTurn(self):
        if(self.turn == 0):
            self.sender().setText("X")
            self.turn = 1
        else:
            self.sender().setText("O")
            self.turn = 0
        if (self.check()):
            if (self.turn == 0):
                self.display.setText("Wygrywa O")
                for btn in self.btnTab:
                    btn.setEnabled(False)
            else:
                self.display.setText("Wygrywa X")
                for btn in self.btnTab:
                    btn.setEnabled(False)
        self.sender().setEnabled(False)

    def check(self):
        for i in range(3):
            if self.list[0][i].text() == self.list[1][i].text() and self.list[1][i].text() == self.list[2][i].text() != "":
                return True
        for i in range(3):
            if self.list[i][0].text() == self.list[i][1].text() and self.list[i][1].text() == self.list[i][2].text() != "":
                return True

        if self.list[0][0].text() == self.list[1][1].text() and self.list[1][1].text() == self.list[2][2].text() != "":
                return True
        if self.list[0][2].text() == self.list[1][1].text() and self.list[1][1].text() == self.list[2][0].text() != "":
                return True

        return False

app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
