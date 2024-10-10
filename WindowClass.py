from PyQt6.QtWidgets import QApplication, QWidget
import sys
from PyQt6.QtGui import QIcon

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Model 1.0 MyExcelFile")
        self.setWindowIcon(QIcon("banio.jpg"))
        self.setGeometry(400,400,400,400)
        # self.setStyleSheet('background-color:#a1a')
        # self.setFixedHeight(700)
        # self.setFixedWidth(700)
        styleSheet = (
        'background-color:#a1a'
        )
        self.setStyleSheet(styleSheet)

app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())
