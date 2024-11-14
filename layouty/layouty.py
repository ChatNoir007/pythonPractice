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

        btn1 = QPushButton("Przycisk 1")
        btn2 = QPushButton("Przycisk 2")
        btn3 = QPushButton("Przycisk 3")
        btn4 = QPushButton("Przycisk 4")
        btn5 = QPushButton("Przycisk 5")
        btn6 = QPushButton("Przycisk 6")
        # btn1.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        # btn2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        # btn3.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        # btn4.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        # btn5.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        # btn6.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        layout = QGridLayout(self)
        layout.addWidget(btn1, 0, 0, 1, 2)
        layout.addWidget(btn2, 1, 0)
        layout.addWidget(btn3, 1, 1)
        layout.addWidget(btn4, 2, 0)
        layout.addWidget(btn5, 2, 1)
        layout.addWidget(btn6, 1, 2, 2, 1, alignment= Qt.AlignmentFlag.AlignCenter)



        #self.setLayout(layout)


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
