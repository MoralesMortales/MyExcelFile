from PyQt5.QtCore import Qt
import pymysql
from datetime import datetime
from ui_py.edit_info_cestaticket import Ui_Form
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIntValidator
import conf

class edit_info_cestaticket(QWidget, Ui_Form):
    def __init__(self):   
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Editar Nomina")
        self.lineEdit.setValidator(QIntValidator(0, 30))  # Solo permite valores de 0 a 30
        self.lineEdit.textChanged.connect(lambda text: self.update_off_days(text))
        self.cedula = 0
        self.confirm.clicked.connect(self.closeNow)

    def closeNow(self):
        self.close()

    def open_window(self, cedula):
        self.showMaximized()
        print(cedula, 'en edit_cesta')
        self.cedula = cedula
        self.load_data()

    def load_data(self):
        try:
            connection = pymysql.connect(
                host='localhost',
                user='user_nomina',
                password='12345678',
                database='sc_db',
                charset='utf8'
            )
            cursor = connection.cursor()
    
            # Obtener información básica del empleado
            query = 'SELECT cedula, nombre FROM nomina_cestaticket_prev WHERE cedula = %s;'
            cursor.execute(query, self.cedula)
            employee = cursor.fetchall()
    
            if employee:
                self.nombre.setText(str(employee[0][1]))
                self.trabajo.setText(str(employee[0][0]))
    
            # Obtener datos del empleado en tabla `employee`
            query = "SELECT CONCAT(name, ' ', lastname) AS fullname FROM employee WHERE cedula = %s;"
            cursor.execute(query, (conf.user,))
            employee = cursor.fetchall()
    
            if employee:
                self.estatus.setText(str(employee[0][0]))
    
            # Obtener datos financieros del empleado actual
            query = "SELECT total_neto, descuentos FROM nomina_cestaticket_prev WHERE cedula = %s;"
            cursor.execute(query, self.cedula)
            financial_data = cursor.fetchall()
    
            if financial_data:
                total_neto, descuentos = financial_data[0]
                self.salario.setText(str(total_neto))   # Actualizar el salario
                self.ubicacion_2.setText(str(descuentos))  # Actualizar descuentos
    
                # Calcular el valor para self.lineEdit
                if total_neto != float(conf.cesta_ticket):
                    off_days = 30 - round((total_neto * 30) / float(conf.cesta_ticket))
                    self.lineEdit.setText(str(off_days))  # Establecer el valor calculado
                else:
                    self.lineEdit.setText("0")  # Si es igual al original, mostrar 0
    
            current_date = datetime.now()
            start = current_date.replace(day=1).strftime('%d-%m-%Y')
            end = current_date.replace(day=1).strftime('%d-%m-%Y')
    
            self.nomina.setText(str(start))
            self.nomina_2.setText(str(end))
    
            connection.close()
    
        except pymysql.Error as e:
            print(f"Error en la base de datos: {e}")
    


    def update_off_days(self, text):
        if not self.lineEdit.text().strip():  # Verificar si está vacío o solo tiene espacios
            self.lineEdit.setText("0")
    
        if text == "0":
            value = 0  # Establecer el valor como 0
        elif text == "00":  # Evitar múltiples ceros al inicio
            self.lineEdit.setText("0")
            value = 0
            return
        elif text.startswith("0") and len(text) > 1:
            # Si comienza con "0" pero tiene más dígitos, elimina el "0" inicial
            self.lineEdit.setText(text[1:])
            return
        else:
            try:
                # Validar entrada numérica
                if not text.isdigit():
                    self.salario.setText(conf.cesta_ticket)
                    return
    
                value = int(text)
                if value > 30:  # Validar el valor máximo
                    self.lineEdit.setText("30")
                    value = 30
            except ValueError as ve:
                # Capturar errores de conversión de datos
                print(f"Error de valor: {ve}")
                self.salario.setText(conf.cesta_ticket)
                return
    
        try:
            # Cálculo de descuento y salario neto
            descuento = (float(conf.cesta_ticket) / 30) * value
            self.ubicacion_2.setText(f"{descuento:.2f}")  # Formato con 2 decimales
            print('the value is ', descuento)
    
            salario_neto = float(conf.cesta_ticket) - descuento
            self.salario.setText(f"{salario_neto:.2f}")  # Formato con 2 decimales
    
            # Validar que cedula no esté vacío
            if not self.cedula:
                raise ValueError("El campo 'cedula' está vacío.")
    
            # Conexión a la base de datos
            connection = pymysql.connect(
                host='localhost',
                user='user_nomina',
                password='12345678',
                database='sc_db',
                charset='utf8'
            )
            cursor = connection.cursor()
    
            query = 'UPDATE nomina_cestaticket_prev SET total_neto = %s, descuentos = %s WHERE cedula = %s;'
            cursor.execute(query, (round(salario_neto, 2), round(descuento, 2), self.cedula))
    
            connection.commit()  # Asegurar cambios
            connection.close()
        except pymysql.MySQLError as e:
            # Capturar errores de MySQL
            print(f"Error en la base de datos: {e}")

