import sys
from PyQt6.QtWidgets import QSizePolicy, QApplication, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt6.QtCore import Qt

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Okienko')
        self.setGeometry(50,50,300,200)

        #KALKULATOR SPOSOBEM TYPU ŻE GRID
        display = QLineEdit()
        display.setReadOnly(True)
        btn1 = QPushButton("1")
        btn2 = QPushButton("2")
        btn3 = QPushButton("3")
        btn4 = QPushButton("4")
        btn5 = QPushButton("5")
        btn6 = QPushButton("6")
        btn7 = QPushButton("7")
        btn8 = QPushButton("8")
        btn9 = QPushButton("9")
        btn0 = QPushButton("0")
        btnCE = QPushButton("CE")
        btnC = QPushButton("C")
        btnDiv = QPushButton("/")
        btnMult = QPushButton("*")
        btnMinus = QPushButton("-")
        btnPlus = QPushButton("+")
        btnDot = QPushButton(".")
        btnEq = QPushButton("=")

        display.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btn1.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btn2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btn3.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btn4.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btn5.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btn6.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btn7.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btn8.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btn9.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btn0.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btnCE.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btnC.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btnDiv.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btnDot.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btnMinus.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btnPlus.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btnMult.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btnEq.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        layout = QGridLayout(self)

        layout.addWidget(display, 0, 0, 1, 5)
        layout.addWidget(btn7, 1, 0)
        layout.addWidget(btn8, 1, 1)
        layout.addWidget(btn9, 1, 2)
        layout.addWidget(btnDiv, 1, 3)
        layout.addWidget(btnCE, 1, 4)
        layout.addWidget(btn4, 2, 0)
        layout.addWidget(btn5, 2, 1)
        layout.addWidget(btn6, 2, 2)
        layout.addWidget(btnMult, 2, 3)
        layout.addWidget(btnC, 2, 4)
        layout.addWidget(btn1, 3, 0)
        layout.addWidget(btn2, 3, 1)
        layout.addWidget(btn3, 3, 2)
        layout.addWidget(btnMinus, 3, 3)
        layout.addWidget(btnEq, 3, 4, 2, 1)
        layout.addWidget(btn0, 4, 0, 1, 2)
        layout.addWidget(btnDot, 4, 2)
        layout.addWidget(btnPlus, 4, 3)

        #self.setLayout(layout)

app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
