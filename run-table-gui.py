from PyQt5 import QtWidgets
from table_ui import Ui_MainWindow

class TableMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.mainwindow = Ui_MainWindow()
        self.mainwindow.setupUi(self)
        self.populate_data()

        self.setVisible(True)

    def on_add_student(self):
        text, status = QtWidgets.QInputDialog.getText(self, "New Student", "Enter Name|gender|roll")
        table = self.mainwindow.tableWidget

        self.rowcount += 1
        table.setRowCount(self.rowcount)
        row = self.rowcount - 1
        col = 0

        if status:
            tokens = text.split('|')

            table.setItem(row, col, QtWidgets.QTableWidgetItem(tokens[0]))
            col += 1
            table.setItem(row, col, QtWidgets.QTableWidgetItem(tokens[1]))
            col += 1
            table.setItem(row, col, QtWidgets.QTableWidgetItem(tokens[2]))

    def populate_data(self):
        # to get students from a database
        # to get students from some server service
        students = [
            ('mehul', 'm', 10),
            ('ivan', 'm', 11),
            ('jane', 'f', 23)
        ]

        row = 0
        col = 0
        table = self.mainwindow.tableWidget
        table.setRowCount(len(students))
        self.rowcount = len(students)

        for student in students:
            table.setItem(row, col, QtWidgets.QTableWidgetItem(student[0]))
            col += 1
            table.setItem(row, col, QtWidgets.QTableWidgetItem(student[1]))
            col += 1
            table.setItem(row, col, QtWidgets.QTableWidgetItem(str(student[2])))

            row += 1
            col = 0


app = QtWidgets.QApplication([])
calcwindow = TableMainWindow()
app.exec_()
