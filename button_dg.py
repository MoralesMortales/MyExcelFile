# Form implementation generated from reading ui file 'buttonMadeWithDg.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_mainWn(object):
    def setupUi(self, mainWn):
        mainWn.setObjectName("mainWn")
        mainWn.resize(655, 693)
        mainWn.setStyleSheet("QWidget {\n"
"background-color:\"#a1deff\"\n"
"}\n"
"\n"
"QPushButton{\n"
"color:red;\n"
"border-radius:9px;\n"
"background-color: white;\n"
"}\n"
"\n"
"QLabel {\n"
"color:green;\n"
"background-color: #eee;\n"
"border-radius:9px;\n"
"\n"
"}")
        self.pushButton = QtWidgets.QPushButton(parent=mainWn)
        self.pushButton.setGeometry(QtCore.QRect(210, 110, 221, 111))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.clicked_btn)
        
        self.label = QtWidgets.QLabel(parent=mainWn)
        self.label.setGeometry(QtCore.QRect(160, 280, 321, 51))
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(mainWn)
        QtCore.QMetaObject.connectSlotsByName(mainWn)

    def retranslateUi(self, mainWn):
        _translate = QtCore.QCoreApplication.translate
        mainWn.setWindowTitle(_translate("mainWn", "Form"))
        self.pushButton.setText(_translate("mainWn", "Click Me"))
        self.label.setText(_translate("mainWn", "Hola amigus, ich bin your beste friend"))

    def clicked_btn(self):
        self.label.setText('Btn Pressed')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWn = QtWidgets.QWidget()
    ui = Ui_mainWn()
    ui.setupUi(mainWn)
    mainWn.show()
    sys.exit(app.exec())
