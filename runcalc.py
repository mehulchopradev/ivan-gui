from PyQt5 import QtWidgets
from calcui import Ui_MainWindow

class CalcMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.mainwindow = Ui_MainWindow()
        self.mainwindow.setupUi(self)
        self.setVisible(True)

        self.mainwindow.ops.addItems(['+','-','*'])

    def on_calculate(self):
        a = int(self.mainwindow.first.text())
        b = int(self.mainwindow.second.text())

        op = self.mainwindow.ops.currentText()

        if op == '+':
            ans = a + b
        elif op == '-':
            ans = a - b
        else:
            ans = a * b
        
        self.mainwindow.answer.setText(str(ans))

app = QtWidgets.QApplication([])
calcwindow = CalcMainWindow()
app.exec_()
