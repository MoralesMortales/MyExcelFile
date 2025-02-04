from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPushButton

class ConfirmDialog(QDialog):
    def __init__(self, message="¿Estás seguro?"):
        super().__init__()
        self.setGeometry(100, 100, 300, 150)
        self.result = False  # Almacena el resultado de la selección

        # Crear widgets
        self.label = QLabel(message, self)
        self.confirm_button = QPushButton("Confirmar", self)
        self.cancel_button = QPushButton("Cancelar", self)

        # Conectar señales
        self.confirm_button.clicked.connect(self.confirm_action)
        self.cancel_button.clicked.connect(self.cancel_action)

        # Configurar layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.confirm_button)
        layout.addWidget(self.cancel_button)
        self.setLayout(layout)

    def confirm_action(self):
        self.result = True  # El usuario confirmó
        print('eliminando')
        self.accept()      # Cierra el diálogo con resultado "aceptado"

    def cancel_action(self):
        self.result = False  # El usuario canceló
        self.reject()        # Cierra el diálogo con resultado "rechazado"


# Ejemplo de uso
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    # Crear y mostrar el diálogo
    dialog = ConfirmDialog("¿Deseas continuar con esta acción?")
    if dialog.exec_():  # Ejecutar el diálogo
        if dialog.result:
            print("El usuario confirmó.")
        else:
            print("El usuario canceló.")
    else:
        print("Diálogo cerrado sin confirmar.")

    sys.exit(app.exec_())
