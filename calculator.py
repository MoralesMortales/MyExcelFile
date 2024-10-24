# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(699, 507)
        Main.setStyleSheet("QLineEdit{\n"
"background-color:#ddd;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:#fff;\n"
"border-radius:10px;\n"
"border:1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:red;\n"
"}\n"
"\n"
"Main{\n"
"width:5000px}\n"
"\n"
"button_1{\n"
"color:red}\n"
"\n"
".QPushButton:hover{\n"
"background-color:green;\n"
"}")

        self.actualNum = ''

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(Main)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.showing = QtWidgets.QLabel(parent=Main)
        self.showing.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.showing.setFont(font)
        self.showing.setStyleSheet("background-color:white;")
        self.showing.setOpenExternalLinks(False)
        self.showing.setObjectName("showing")
        self.verticalLayout_5.addWidget(self.showing)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_1 = QtWidgets.QPushButton(parent=Main)
        self.button_1.setMinimumSize(QtCore.QSize(100, 100))
        self.button_1.setObjectName("button_1")
        self.button_1.clicked.connect(self.btn_1)
        self.horizontalLayout_2.addWidget(self.button_1)
        self.button_2 = QtWidgets.QPushButton(parent=Main)
        self.button_2.setMinimumSize(QtCore.QSize(100, 100))
        self.button_2.setObjectName("button_2")
        self.button_2.clicked.connect(self.btn_2)
        self.horizontalLayout_2.addWidget(self.button_2)
        self.button_3 = QtWidgets.QPushButton(parent=Main)
        self.button_3.setMinimumSize(QtCore.QSize(100, 100))
        self.button_3.setStyleSheet("")
        self.button_3.setObjectName("button_3")
        self.button_3.clicked.connect(self.btn_3)
        self.horizontalLayout_2.addWidget(self.button_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_4 = QtWidgets.QPushButton(parent=Main)
        self.button_4.setMinimumSize(QtCore.QSize(100, 100))
        self.button_4.setObjectName("button_4")
        self.button_4.clicked.connect(self.btn_4)
        self.horizontalLayout_3.addWidget(self.button_4)
        self.pushButton_6 = QtWidgets.QPushButton(parent=Main)
        self.pushButton_6.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.btn_5)
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.button_6 = QtWidgets.QPushButton(parent=Main)
        self.button_6.setMinimumSize(QtCore.QSize(100, 100))
        self.button_6.setObjectName("button_6")
        self.button_6.clicked.connect(self.btn_6)
        self.horizontalLayout_3.addWidget(self.button_6)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_7 = QtWidgets.QPushButton(parent=Main)
        self.button_7.setMinimumSize(QtCore.QSize(100, 100))
        self.button_7.setObjectName("button_7")
        self.button_7.clicked.connect(self.btn_7)
        self.horizontalLayout.addWidget(self.button_7)
        self.button_8 = QtWidgets.QPushButton(parent=Main)
        self.button_8.setMinimumSize(QtCore.QSize(100, 100))
        self.button_8.setObjectName("button_8")
        self.button_8.clicked.connect(self.btn_8)
        self.horizontalLayout.addWidget(self.button_8)
        self.button_9 = QtWidgets.QPushButton(parent=Main)
        self.button_9.setMinimumSize(QtCore.QSize(100, 100))
        self.button_9.setObjectName("button_9")
        self.button_9.clicked.connect(self.btn_9)
        self.horizontalLayout.addWidget(self.button_9)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.button_0 = QtWidgets.QPushButton(parent=Main)
        self.button_0.setMinimumSize(QtCore.QSize(100, 100))
        self.button_0.setObjectName("button_0")
        self.button_0.clicked.connect(self.btn_0)
        self.verticalLayout_2.addWidget(self.button_0)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.button_plus = QtWidgets.QPushButton(parent=Main)
        self.button_plus.setMinimumSize(QtCore.QSize(100, 100))
        self.button_plus.setObjectName("button_plus")
        self.verticalLayout_4.addWidget(self.button_plus)
        self.button_times = QtWidgets.QPushButton(parent=Main)
        self.button_times.setMinimumSize(QtCore.QSize(100, 100))
        self.button_times.setObjectName("button_times")
        self.verticalLayout_4.addWidget(self.button_times)
        self.button_dot = QtWidgets.QPushButton(parent=Main)
        self.button_dot.setMinimumSize(QtCore.QSize(100, 100))
        self.button_dot.setObjectName("button_dot")
        self.verticalLayout_4.addWidget(self.button_dot)
        self.button_power = QtWidgets.QPushButton(parent=Main)
        self.button_power.setMinimumSize(QtCore.QSize(100, 100))
        self.button_power.setObjectName("button_power")
        self.verticalLayout_4.addWidget(self.button_power)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.button_minus = QtWidgets.QPushButton(parent=Main)
        self.button_minus.setMinimumSize(QtCore.QSize(100, 100))
        self.button_minus.setObjectName("button_minus")
        self.verticalLayout_3.addWidget(self.button_minus)
        self.button_between = QtWidgets.QPushButton(parent=Main)
        self.button_between.setMinimumSize(QtCore.QSize(100, 100))
        self.button_between.setObjectName("button_between")
        self.verticalLayout_3.addWidget(self.button_between)
        self.equal = QtWidgets.QPushButton(parent=Main)
        self.equal.setMinimumSize(QtCore.QSize(100, 200))
        self.equal.setObjectName("equal")
        self.verticalLayout_3.addWidget(self.equal)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Form"))
        self.showing.setText(_translate("Main", "89"))
        self.button_1.setText(_translate("Main", "1"))
        self.button_2.setText(_translate("Main", "2"))
        self.button_3.setText(_translate("Main", "3"))
        self.button_4.setText(_translate("Main", "4"))
        self.pushButton_6.setText(_translate("Main", "5"))
        self.button_6.setText(_translate("Main", "6"))
        self.button_7.setText(_translate("Main", "7"))
        self.button_8.setText(_translate("Main", "8"))
        self.button_9.setText(_translate("Main", "9"))
        self.button_0.setText(_translate("Main", "0"))
        self.button_plus.setText(_translate("Main", "+"))
        self.button_times.setText(_translate("Main", "x"))
        self.button_dot.setText(_translate("Main", "."))
        self.button_power.setText(_translate("Main", "^"))
        self.button_minus.setText(_translate("Main", "-"))
        self.button_between.setText(_translate("Main", "/"))
        self.equal.setText(_translate("Main", "="))

    def btn_1(self):
        self.actualNum += '1';
        self.showing.setText(self.actualNum)
    
    def btn_2(self):
        self.actualNum += '2';
        self.showing.setText(self.actualNum)
    
    def btn_3(self):
        self.actualNum += '3';
        self.showing.setText(self.actualNum)
    
    def btn_4(self):
        self.actualNum += '4';
        self.showing.setText(self.actualNum)

    def btn_5(self):
        self.actualNum += '5';
        self.showing.setText(self.actualNum)   
    
    def btn_6(self):
        self.actualNum += '6';
        self.showing.setText(self.actualNum)       
    
    def btn_7(self):
        self.actualNum += '7';
        self.showing.setText(self.actualNum)

    def btn_8(self):
        self.actualNum += '8';
        self.showing.setText(self.actualNum)       

    def btn_9(self):
        self.actualNum += '9';
        self.showing.setText(self.actualNum)

    def btn_0(self):
        self.actualNum += '0';
        self.showing.setText(self.actualNum)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QWidget()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec())
