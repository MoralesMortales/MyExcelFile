from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic
import sys

class UI(QWidget):
    def __init__(self) -> None:
        super().__init__()

        uic.loadUi("Window.ui", self)

app = QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec())
