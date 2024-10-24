from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(891, 410)
        Form.setStyleSheet("#Form{\n"
"background-color:#F1FEFF;\n"
"}\n"
"QPushButton{\n"
"background-color:white;\n"
"border:none;\n"
"}\n"
"#btn_delete_nomina,#btn_search_nomina,#btn_add_nomina,#btn_edit_nomina {\n"
"background-color:#7ECECF;\n"
"font-family:Noto Serif Sinhala ExtraBold;\n"
"color:#fff;\n"
"font-size:10px;\n"
"height:30px;\n"
"border-radius:2px;\n"
"}")
        self.tableView = QtWidgets.QTableView(parent=Form)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 641, 391))
        self.tableView.setObjectName("tableView")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(670, 240, 211, 151))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("userOnDesktop.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(680, 20, 191, 220))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_add_nomina = QtWidgets.QPushButton(parent=self.widget)
        self.btn_add_nomina.setObjectName("btn_add_nomina")
        self.verticalLayout.addWidget(self.btn_add_nomina)
        self.btn_delete_nomina = QtWidgets.QPushButton(parent=self.widget)
        self.btn_delete_nomina.setObjectName("btn_delete_nomina")
        self.verticalLayout.addWidget(self.btn_delete_nomina)
        self.btn_edit_nomina = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Noto Serif Sinhala ExtraBold")
        font.setPointSize(-1)
        font.setBold(True)
        self.btn_edit_nomina.setFont(font)
        self.btn_edit_nomina.setStyleSheet("")
        self.btn_edit_nomina.setObjectName("btn_edit_nomina")
        self.verticalLayout.addWidget(self.btn_edit_nomina)
        self.btn_search_nomina = QtWidgets.QPushButton(parent=self.widget)
        self.btn_search_nomina.setStyleSheet("")
        self.btn_search_nomina.setObjectName("btn_search_nomina")
        self.verticalLayout.addWidget(self.btn_search_nomina)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_add_nomina.setText(_translate("Form", "Agregar nueva nomina"))
        self.btn_delete_nomina.setText(_translate("Form", "Eliminar nomina"))
        self.btn_edit_nomina.setText(_translate("Form", "Editar nomina"))
        self.btn_search_nomina.setText(_translate("Form", "Busqueda de nominas"))

