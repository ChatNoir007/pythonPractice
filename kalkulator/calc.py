import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt6.QtGui import QPixmap

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Okienko')
        self.setGeometry(300, 300, 420, 300)

        self.label = QLabel(self)
        self.label.move(30, 40)
        self.label.setText("")

        self.num1 = 0
        self.num2 = 0
        self.oper = ""

        btn7 = QPushButton("7", self)
        btn7.move(20, 100)
        btn7.clicked.connect(self.number)

        btn8 = QPushButton("8", self)
        btn8.move(120, 100)
        btn8.clicked.connect(self.number)

        btn9 = QPushButton("9", self)
        btn9.move(220, 100)
        btn9.clicked.connect(self.number)

        btn4 = QPushButton("4", self)
        btn4.move(20, 150)
        btn4.clicked.connect(self.number)

        btn5 = QPushButton("5", self)
        btn5.move(120, 150)
        btn5.clicked.connect(self.number)

        btn6 = QPushButton("6", self)
        btn6.move(220, 150)
        btn6.clicked.connect(self.number)

        btn1 = QPushButton("1", self)
        btn1.move(20, 200)
        btn1.clicked.connect(self.number)

        btn2 = QPushButton("2", self)
        btn2.move(120, 200)
        btn2.clicked.connect(self.number)

        btn3 = QPushButton("3", self)
        btn3.move(220, 200)
        btn3.clicked.connect(self.number)

        btn0 = QPushButton("0", self)
        btn0.move(20, 250)
        btn0.clicked.connect(self.number)

        btnC = QPushButton("C", self)
        btnC.move(120, 250)
        btnC.clicked.connect(self.btnC)

        btnEqual = QPushButton("=", self)
        btnEqual.move(220, 250)
        btnEqual.clicked.connect(self.btnEqual)

        btnPlus = QPushButton("+", self)
        btnPlus.move(320, 100)
        btnPlus.clicked.connect(self.operation)

        btnMinus = QPushButton("-", self)
        btnMinus.move(320, 150)
        btnMinus.clicked.connect(self.operation)

        btnMultiply = QPushButton("*", self)
        btnMultiply.move(320, 200)
        btnMultiply.clicked.connect(self.operation)

        btnDivide = QPushButton("/", self)
        btnDivide.move(320, 250)
        btnDivide.clicked.connect(self.operation)

    def number(self):
        self.label.setText(self.label.text() + self.sender().text())
        self.label.adjustSize()

    def btnC(self):
        num1 = 0
        num2 = 0
        oper = ""
        self.label.setText("")
        self.label.adjustSize()


    def operation(self):
        self.oper = self.sender().text()
        self.num1 = self.label.text()
        self.label.setText("")
        self.label.adjustSize()

    def btnEqual(self):
        self.num2 = self.label.text()
        match self.oper:
            case "+":
                self.label.setText(str(float(self.num1) + float(self.num2)))
                self.label.adjustSize()
            case "-":
                self.label.setText(str(float(self.num1) - float(self.num2)))
                self.label.adjustSize()
            case "*":
                self.label.setText(str(float(self.num1) * float(self.num2)))
                self.label.adjustSize()
            case "/":
                if(self.num2 == "0"):
                    self.label.setText("Nie dziel przez 0")
                    self.label.adjustSize()
                else:
                    self.label.setText(str(float(self.num1) / float(self.num2)))
                    self.label.adjustSize()


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
