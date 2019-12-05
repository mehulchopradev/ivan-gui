# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(815, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 50, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.first = QtWidgets.QLineEdit(self.centralwidget)
        self.first.setGeometry(QtCore.QRect(170, 100, 113, 21))
        self.first.setObjectName("first")
        self.ops = QtWidgets.QComboBox(self.centralwidget)
        self.ops.setGeometry(QtCore.QRect(350, 100, 104, 26))
        self.ops.setObjectName("ops")
        self.second = QtWidgets.QLineEdit(self.centralwidget)
        self.second.setGeometry(QtCore.QRect(520, 100, 113, 21))
        self.second.setObjectName("second")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(340, 170, 113, 32))
        self.button.setObjectName("button")
        self.answer = QtWidgets.QLabel(self.centralwidget)
        self.answer.setGeometry(QtCore.QRect(370, 240, 60, 16))
        self.answer.setText("")
        self.answer.setObjectName("answer")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.button.clicked.connect(MainWindow.on_calculate)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "My Calculator"))
        self.first.setPlaceholderText(_translate("MainWindow", "1st No"))
        self.second.setPlaceholderText(_translate("MainWindow", "2nd No"))
        self.button.setText(_translate("MainWindow", "Calculate"))

