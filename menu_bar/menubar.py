import sys
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QComboBox, QPushButton, QGridLayout, QFormLayout, \
    QMainWindow


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Lista')
        self.setGeometry(50, 50, 300, 200)

        menu = self.menuBar()
        file_menu = menu.addMenu('File')

        self.open_action = QAction("Otwórz")
        file_menu.addAction(self.open_action)

        file_menu.addSeparator()
        self.exit_action = QAction("Zakończ")

        self.exit_action.triggered.connect(self.close)
        file_menu.addAction(self.exit_action)

app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
