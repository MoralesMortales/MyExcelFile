from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
import sys
from PyQt6.QtGui import QIcon, QFont

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Model 1.0 MyExcelFile")
        self.setWindowIcon(QIcon("banio.jpg"))
        self.setGeometry(400,400,400,400)
        # self.setStyleSheet('background-color:#a1a')
        # self.setFixedHeight(700)
        # self.setFixedWidth(700)

        self.counter = 0

        styleSheet = (
        'background-color:#21a'
        )
        self.setStyleSheet(styleSheet)

        vbox = QVBoxLayout()

        btn1 = QPushButton("Btn one")
        btn2 = QPushButton("Btn two")
        btn3 = QPushButton("Btn three")
        btn4 = QPushButton("Btn four")

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)


        self.setLayout(vbox)

app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())
