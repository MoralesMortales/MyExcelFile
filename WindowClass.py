from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QWidget
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
        self.create_widgets()

        self.counter = 0

        styleSheet = (
        'background-color:#21a'
        )
        self.setStyleSheet(styleSheet)

    def create_widgets(self):
        btn = QPushButton("Click me fella", self)
        btn.setGeometry(100, 100, 100, 100)
        btn.clicked.connect(self.change_text_event)
        self.label = QLabel("Label v1", self)
        self.label.setStyleSheet('background-color:white')

    def change_text_event(self):
        self.label.setText("Label v2!")
        self.label.setGeometry(10,70,70,70)
        if self.counter != 0:
            self.label.setText('Already changed!')
        self.counter = self.counter + 1


app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())
