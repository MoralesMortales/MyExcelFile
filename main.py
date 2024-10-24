from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget
from menu import Ui_Form


class MainApp(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(MainApp, self).__init__()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
