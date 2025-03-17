import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("mainwindow.ui", self)

        self.actionOtworz.triggered.connect(self.initOtworz)
        self.actionZapisz.triggered.connect(self.initZapisz)

    def initOtworz(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Otwórz plik", "", "Pliki tekstowe (*.txt);;Wszystkie pliki (*)")
        if file_name:
            with open(file_name, "r", encoding="utf-8") as file:
                self.plainTextEdit.setPlainText(file.read())

    def initZapisz(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Zapisz plik", "", "Pliki tekstowe (*.txt);;Wszystkie pliki (*)")
        if file_name:
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(self.plainTextEdit.toPlainText())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
