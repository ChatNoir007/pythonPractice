import math

from PyQt6.QtWidgets import QApplication, QDialog
import sys, json
from PyQt6.uic import loadUi

class Window(QDialog):
    def __init__(self):
        super().__init__()

        loadUi("pizza.ui", self)

        file = open("pitca.txt", "r", encoding="utf-8")
        self.loading = json.loads(file.read())

        self.combo1.addItems(self.loading.keys())
        self.combo2.addItems(self.loading.keys())

        self.combo1.currentTextChanged.connect(self.updateLabel1)
        self.combo2.currentTextChanged.connect(self.updateLabel2)

        self.btn_add.clicked.connect(self.btnAdd)
        self.btn_porownaj.clicked.connect(self.btnCompare)


    def btnAdd(self):
        name = self.edit_name.text()
        size = int(self.edit_size.text())
        price = int(self.edit_price.text())

        if name and size and price:
            self.combo1.addItem(name)
            self.combo2.addItem(name)
            print("dodalo do comba")
        else:
            self.porownanie.setText("nie wpisano danych we wszystkie pola.")


        self.loading[name] = {"name": name, "size": size, "price": price}
        with open("pitca.txt", "w", encoding="utf-8") as file:
            json.dump(self.loading, file)


    def updateLabel1(self):
        pizza = self.combo1.currentText()
        self.pizza1.setText(f"Średnica: {self.loading[pizza]['size']} cm\nCena: {self.loading[pizza]['price']} zł")

    def updateLabel2(self):
        pizza = self.combo2.currentText()
        self.pizza2.setText(f"Średnica: {self.loading[pizza]['size']} cm\nCena: {self.loading[pizza]['price']} zł")

    def btnCompare(self):
        pizza1 = self.combo1.currentText()
        pizza2 = self.combo2.currentText()



        pricePerCm1 = round(self.loading[pizza1]['price'] / (math.pi * (self.loading[pizza1]['size']/2) **2), 4)
        pricePerCm2 = round(self.loading[pizza2]['price'] / (math.pi * (self.loading[pizza2]['size']/2) **2), 4)

        if pricePerCm1 > pricePerCm2:
            self.porownanie.setText(f"Bardziej opłaca się pizza prawa ({pricePerCm1} zł/cm² vs {pricePerCm2} zł/cm²)")
        elif pricePerCm1 < pricePerCm2:
            self.porownanie.setText(f"Bardziej opłaca się pizza lewa ({pricePerCm1} zł/cm² vs {pricePerCm2} zł/cm²)")
        elif pricePerCm1 == pricePerCm2:
            self.porownanie.setText(f"Obie pizze są tak samo opłacalne ({pricePerCm1} zł/cm²)")
        else:
            self.porownanie.setText("źle dobrano pitce")




app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
