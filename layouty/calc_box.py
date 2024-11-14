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

        # KALKULATOR SPOSOBEM TYPU BOX
        display = QLineEdit()
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

        layout = QVBoxLayout(self)
        layout1 = QHBoxLayout()
        layout1.addWidget(display)

        layout2 = QHBoxLayout()
        layout2.addWidget(btn7)
        layout2.addWidget(btn8)
        layout2.addWidget(btn9)
        layout2.addWidget(btnDiv)
        layout2.addWidget(btnCE)

        layout3 = QHBoxLayout()
        layout3.addWidget(btn4)
        layout3.addWidget(btn5)
        layout3.addWidget(btn6)
        layout3.addWidget(btnMult)
        layout3.addWidget(btnC)

        layout4_left_top = QHBoxLayout()
        layout4_left_top.addWidget(btn1)
        layout4_left_top.addWidget(btn2)

        layout4_left_bottom = QHBoxLayout()
        layout4_left_bottom.addWidget(btn0)

        layout4_left = QVBoxLayout()
        layout4_left.addLayout(layout4_left_top)
        layout4_left.addLayout(layout4_left_bottom)

        layout4_mid_top = QHBoxLayout()
        layout4_mid_top.addWidget(btn3)
        layout4_mid_top.addWidget(btnMinus)

        layout4_mid_bottom = QHBoxLayout()
        layout4_mid_bottom.addWidget(btnDot)
        layout4_mid_bottom.addWidget(btnPlus)

        layout4_mid = QVBoxLayout()
        layout4_mid.addLayout(layout4_mid_top)
        layout4_mid.addLayout(layout4_mid_bottom)

        layout4_right = QVBoxLayout()
        layout4_right.addWidget(btnEq)

        layout4 = QHBoxLayout()
        layout4.addLayout(layout4_left)
        layout4.addLayout(layout4_mid)
        layout4.addLayout(layout4_right)

        layout.addLayout(layout1)
        layout.addLayout(layout2)
        layout.addLayout(layout3)
        layout.addLayout(layout4)


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()

