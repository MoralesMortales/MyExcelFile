from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel 
from PyQt6.QtGui import QIcon, QFont
import sys

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Pressing buttons")
        self.setWindowIcon(QIcon("banio.jpg"))
        self.setGeometry(400, 400, 400, 400)

        self.create_widgets()

    def create_widgets(self):
        btn = QPushButton("Click me", self)
        #btn.move(100,100)
        btn.setGeometry(100,100,100,100)
        styleSheet = (
        'background-color:#a1a'
        )
        btn.setStyleSheet(styleSheet)
        btn.setIcon(QIcon("banio.jpg"))

        label = QLabel("My label", self)
        label.move(100, 200)
        label.setStyleSheet(styleSheet)
        label.setFont(QFont("New Times Roman", 15))

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
