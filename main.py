import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import threading


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(359, 385)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        icon = QtGui.QIcon.fromTheme("Cc")
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.label1.setText("")
        self.label1.setPixmap(QtGui.QPixmap("indian money.jpg"))
        self.label1.setScaledContents(True)
        self.label1.setObjectName("label1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 101, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 101, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(True)
        self.label_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setObjectName("label_2")

        self.comboBox1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox1.setGeometry(QtCore.QRect(130, 80, 61, 21))
        self.comboBox1.setObjectName("comboBox1")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox2.setGeometry(QtCore.QRect(130, 110, 61, 21))
        self.comboBox2.setObjectName("comboBox2")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 150, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 210, 131, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(True)
        self.label_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 50, 81, 21))
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(150, 210, 141, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(True)
        self.label_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 50, 151, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setValidator(QDoubleValidator(0.99, 99.99, 3))
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(True)
        self.label_5.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Currency Converter"))
        self.label.setText(_translate("MainWindow", "Convert from:"))
        self.label_2.setText(_translate("MainWindow", "Convert to:"))
        self.comboBox1.setItemText(0, _translate("MainWindow", "BRL"))
        self.comboBox1.setItemText(1, _translate("MainWindow", "CAD"))
        self.comboBox1.setItemText(2, _translate("MainWindow", "EGP"))
        self.comboBox1.setItemText(3, _translate("MainWindow", "EGR"))
        self.comboBox1.setItemText(4, _translate("MainWindow", "INR"))
        self.comboBox1.setItemText(5, _translate("MainWindow", "ILS"))
        self.comboBox1.setItemText(6, _translate("MainWindow", "KWD"))
        self.comboBox1.setItemText(7, _translate("MainWindow", "MYR"))
        self.comboBox1.setItemText(8, _translate("MainWindow", "QAR"))
        self.comboBox1.setItemText(9, _translate("MainWindow", "USD"))
        self.comboBox2.setItemText(0, _translate("MainWindow", "BRL"))
        self.comboBox2.setItemText(1, _translate("MainWindow", "CAD"))
        self.comboBox2.setItemText(2, _translate("MainWindow", "EGP"))
        self.comboBox2.setItemText(3, _translate("MainWindow", "EUR"))
        self.comboBox2.setItemText(4, _translate("MainWindow", "INR"))
        self.comboBox2.setItemText(5, _translate("MainWindow", "ILS"))
        self.comboBox2.setItemText(6, _translate("MainWindow", "KWD"))
        self.comboBox2.setItemText(7, _translate("MainWindow", "MYR"))
        self.comboBox2.setItemText(8, _translate("MainWindow", "QAR"))
        self.comboBox2.setItemText(9, _translate("MainWindow", "USD"))
        self.pushButton.setText(_translate("MainWindow", "Convert"))
        self.label_3.setText(_translate("MainWindow", "Coverted amount:"))
        self.label_4.setText(_translate("MainWindow", "Amount:"))

        new=79.6

        self.pushButton.clicked.connect(self.pressed)






    def pressed(self):
        x = self.comboBox1.currentText()
        y = self.comboBox2.currentText()

        api_key = "FHBGGR1DA7CZ9SVX"
        url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency='+x+'&to_currency='+y+'&apikey=FHBGGR1DA7CZ9SVX'

        r = requests.get(url)
        data = r.json()
        am =self.lineEdit.text()
        amount=float(am)
        exrate= data['Realtime Currency Exchange Rate']['5. Exchange Rate']
        ex=float(exrate)
        new_amount=round(amount*ex , 3)
        self.label_5.setText(str(new_amount))


from PyQt5 import QtQuickWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

