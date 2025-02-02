
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QMessageBox, QLabel, QVBoxLayout, QDialog

def successfulWidget(parent, message="Empleado Creado Exitosamente", 
                     timeout=4000):

    # Crear un QDialog personalizado para mayor control
    msgBox = QDialog(parent)
    msgBox.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)  # Sin barra de título

    # Crear un QLabel para mostrar el mensaje
    custom_label = QLabel(message, msgBox)
    custom_label.setAlignment(Qt.AlignCenter)  # Centrar el texto
    custom_label.setStyleSheet("font-size: 14px; padding: 10px;")  # Opcional: Estilizar

    # Crear un diseño y añadir el QLabel
    layout = QVBoxLayout(msgBox)
    layout.addWidget(custom_label)
    msgBox.setLayout(layout)

    # Configurar el temporizador para cerrar el QMessageBox y la ventana padre automáticamente
    auto_close_timer = QTimer(msgBox)
    auto_close_timer.setSingleShot(True)
    auto_close_timer.timeout.connect(msgBox.close)  # Cerrar el QDialog
    auto_close_timer.timeout.connect(parent.close)  # Cerrar la ventana padre
    auto_close_timer.start(timeout)

    # Mostrar el QDialog
    msgBox.exec_()

