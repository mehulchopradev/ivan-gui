from PyQt5 import QtWidgets
from file_reader import Ui_MainWindow

class FileReaderMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.mainwindow = Ui_MainWindow()
        self.mainwindow.setupUi(self)
        self.setVisible(True)

    def on_open(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self)
        with open(file_path) as fp:
            contents = fp.read()
            self.mainwindow.textEdit.setText(contents)


app = QtWidgets.QApplication([])
calcwindow = FileReaderMainWindow()
app.exec_()
