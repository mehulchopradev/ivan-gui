from PyQt5 import QtWidgets
from libmgmtui import Ui_MainWindow

class LibmgmtMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.mainwindow = Ui_MainWindow()
        self.mainwindow.setupUi(self)
        self.setVisible(True)

    def navigate_register(self):
        self.mainwindow.stackedWidget.setCurrentIndex(1)

    def navigate_login(self):
        self.mainwindow.stackedWidget.setCurrentIndex(0)

app = QtWidgets.QApplication([])
calcwindow = LibmgmtMainWindow()
app.exec_()
