from PyQt6.QtWidgets import QApplication, QWidget, QLabel
import sys
from PyQt6.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Okienko")
        self.setGeometry(300,300,400,400)

        label = QLabel(self)
        label.setText("Przykladowy text")
        label.move(50,50)

        with open("malpa.jpg"):
            img_label = QLabel(self)
            pixmap = QPixmap("malpa.jpg")
            img_label.setPixmap(pixmap.scaledToWidth(300))
            img_label.move(50,100)

app = QApplication(sys.argv)
window = Window()
window.show()

app.exec()