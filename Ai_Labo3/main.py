# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow,QPushButton

from ui_calculatrice import Ui_MainWindow
from Calculator import Calculator

class MainWindow(QMainWindow):
    number1:int
    number2:int
    numberEntered:bool
    operand:str
    def __init__(self,x=0,y=0, w=411,h=489):
         super(MainWindow, self).__init__()
         self.calc = Calculator()
         self.initUi()
         self.numberEntered = True
         for i in range(0, 10):
             getattr(self.ui, "num_" + str(i)).clicked.connect(self.addNumber)
         self.ui.Plus.clicked.connect(self.plusButton)
         self.ui.Equal.clicked.connect(self.equalButton)
         self.ui.Multiply.clicked.connect(self.multiplyButton)
         self.ui.Divise.clicked.connect(self.diviseButton)
         self.ui.RootSquare.clicked.connect(self.rootSquareButton)
         self.ui.Square.clicked.connect(self.squareButton)
         self.ui.fraction.clicked.connect(self.fractionButton)
         self.ui.ClearEverything.clicked.connect(self.CEButton)
         self.ui.Clear.clicked.connect(self.clearButton)
         self.ui.Erase.clicked.connect(self.eraseButton)
         self.setWindowTitle("Calculatrice à Julien")

    #.clearHistory(backward()) pour effacer par en arriere

    def initUi(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def addNumber(self):
        if(self.numberEntered == True):
            self.ui.Montrer.clear()
            self.numberEntered = False
        butt = self.sender()
        old = self.ui.Montrer.toPlainText()
        newText = old + butt.text()
        self.ui.Montrer.setText(newText)

    def plusButton(self):
        self.number1 = int(self.ui.Montrer.toPlainText())
        self.operand = "+"
        self.ui.Montrer.setText("+")
        self.numberEntered = True

    def minusButton(self):
        self.number1 = int(self.ui.Montrer.toPlainText())
        self.operand = "-"
        self.ui.Montrer.setText("-")
        self.numberEntered = True


    def multiplyButton(self):
        self.number1 = int(self.ui.Montrer.toPlainText())
        self.operand = "x"
        self.ui.Montrer.setText("*")
        self.numberEntered = True
    def diviseButton(self):
        self.number1 = int(self.ui.Montrer.toPlainText())
        self.operand = "/"
        self.ui.Montrer.setText("/")
        self.numberEntered = True
    def rootSquareButton(self):
        self.number1 = int(self.ui.Montrer.toPlainText())
        self.operand = "rootSquare"
        #self.ui.Montrer.setText("√")
        self.numberEntered = True
        self.equalButton()

    def squareButton(self):
        self.number1 = int(self.ui.Montrer.toPlainText())
        self.operand = "Square"
        #self.ui.Montrer.setText("√")
        self.numberEntered = True
        self.equalButton()
    def fractionButton(self):
        self.number1 = int(self.ui.Montrer.toPlainText())
        self.operand = "Fraction"
        #self.ui.Montrer.setText("√")
        self.numberEntered = True
        self.equalButton()

    def moduloButton(self):
        self.number1 = int(self.ui.Montrer.toPlainText())
        self.operand = "%"
        #self.ui.Montrer.setText("√")
        self.numberEntered = True
        self.equalButton()

    def equalButton(self):
        self.number2 = int(self.ui.Montrer.toPlainText())
        if(self.operand == "+"):
            total = self.calc.Plus(self.number1, self.number2)
        elif(self.operand == "-"):
            total = self.calc.Minus(self.number1, self.number2)
        elif(self.operand == "*"):
            total = self.calc.Multiply(self.number1, self.number2)
        elif(self.operand == "/"):
            total = self.calc.Divise(self.number1, self.number2)
        elif(self.operand == "rootSquare"):
            total = self.calc.SquareRoot(self.number1)
        elif(self.operand == "Square"):
            total = self.calc.SquareRoot(self.number1)
        elif(self.operand == "Fraction"):
            total = self.calc.SquareRoot(self.number1)
        elif(self.operand == "%"):
            total = self.calc.Modulo(self.number1, self.number2)
        self.ui.Montrer.setText(str(total))
        #self.ui.Montrer.setText(str(int(self.number1 + self.number2)))

    def CEButton(self):
        self.number1 = 0
        self.number2 = 0
        self.ui.Montrer.clear()

    def clearButton(self):
        self.ui.Montrer.clear()

    def eraseButton(self):
        self.ui.Montrer.delete()



def window():
    app = QApplication(sys.argv)
    win = MainWindow()

    app.setActiveWindow(win)
    win.show()

    sys.exit(app.exec())

if __name__ == "__main__":
     window()
