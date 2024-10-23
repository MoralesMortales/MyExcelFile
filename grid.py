from PyQt6.QtWidgets import QApplication, QGridLayout, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget
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

        grid = QGridLayout()

        btn1 = QPushButton("Btn one")
        btn2 = QPushButton("Btn two")
        btn3 = QPushButton("Btn three")
        btn4 = QPushButton("Btn four")
        btn5 = QPushButton("Btn five")
        btn6 = QPushButton("Btn six")
        btn7 = QPushButton("Btn seven")
        btn8 = QPushButton("Btn eight")
        
        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 0, 1)
        grid.addWidget(btn3, 0, 2)
        grid.addWidget(btn4, 1, 0)
        grid.addWidget(btn5, 1, 1)
        grid.addWidget(btn6, 1, 2)
        grid.addWidget(btn7, 2, 0)
        grid.addWidget(btn8, 2, 1)

        self.setLayout(grid)

app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())
