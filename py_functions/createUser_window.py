from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMessageBox, QWidget
import pymysql
import conf
from ui_py.create_empleado import Ui_Form 
from PyQt5.QtGui import QDoubleValidator
from py_functions.successful_change_notification import successfulWidget
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from py_functions.historial import historial_view

class createUserWindow(QWidget, Ui_Form):
    def __init__(self):   
       super().__init__() 

       self.historial = historial_view()

       self.setupUi(self)
       doubleRange = QDoubleValidator(0.0,9999.9,2,self)
       intRange = QDoubleValidator(0.0,99.9,0,self)
       regex = QRegExp("^[a-zA-Z ]+$")
       text_regex = QRegExp("^[0-9]+$")
       validator_text = QRegExpValidator(regex)
       text_regex = QRegExpValidator(text_regex)
       
       self.create_user_salary_btn.setValidator(doubleRange)
       self.create_user_children_btn.setValidator(intRange)
       self.create_user_cedula_btn.setValidator(intRange)
       self.create_user_worked_years_btn.setValidator(intRange)
       self.create_user_cedula_btn.setMaxLength(9)

       self.create_user_nombre_btn.setValidator(validator_text)
       self.create_user_apellido_btn.setValidator(validator_text)
       self.create_user_job_btn.setValidator(validator_text)
       self.create_user_proffesion_btn.setValidator(validator_text)

       self.nro_cuenta.setValidator(text_regex)
       self.nro_cuenta.setMaxLength(20)
       self.create_user_salary_btn.setMaxLength(9)
       self.nro_tlfn.setValidator(text_regex)
       self.nro_tlfn.setMaxLength(12)
       self.create_user_salary_btn.setMaxLength(8)

       self.create_employee_btn.clicked.connect(self.validate)

    def validate(self):
        # Obtener los datos del formulario
        name = self.create_user_nombre_btn.text().strip().title()
        lastname = self.create_user_apellido_btn.text().strip().title()
        cedula = self.create_user_cedula_btn.text().strip()
        start_date = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        academic_level = self.create_user_academic_level_btn.currentText()
        job = self.create_user_job_btn.text().strip().capitalize()
        proffesion = self.create_user_proffesion_btn.text().strip().capitalize()
        onapre = self.create_user_onapre_btn.currentText()
        salary = self.create_user_salary_btn.text().strip()
        location = self.create_user_location_btn.text().strip()
        children = self.create_user_children_btn.text().strip()
        workedYears = self.create_user_worked_years_btn.text().strip()
        nomina_type = self.create_user_nomina_type_btn.currentText()
        tipo_cuenta = self.tipo_cuenta.currentText()
        contrato = self.contrato.currentText()
        nro_cuenta = self.nro_cuenta.text().strip()
        nro_telefono = self.nro_tlfn.text().strip()
        print(nro_telefono)

        if not all([name, contrato,lastname, cedula, academic_level, job, proffesion, onapre, salary, location, children, workedYears, nro_cuenta, tipo_cuenta, nro_telefono]):
            QMessageBox.warning(self, "Faltan datos", "Por favor, complete todos los campos.")
            return

        if len(nro_cuenta) != 20:
            QMessageBox.warning(self, "Número de cuenta inválido", "El número de cuenta debe tener exactamente 20 dígitos.")
            return
        try:
            connection = pymysql.connect(
                host='localhost',
                user='user_nomina',
                password='12345678',
                database='sc_db',
                charset='utf8')
            try:
                with connection.cursor() as cursor:
                    # Verificar si la cédula ya existe
                    query = "SELECT COUNT(*) FROM employee WHERE cedula = %s"
                    cursor.execute(query, (cedula,))
                    res = cursor.fetchone()

                    if res[0] > 0:
                        QMessageBox.warning(self, "Cédula existente", "Ya existe un empleado con esta cédula.")
                    else:
                        # Insertar en la base de datos
                        query = """
                        INSERT INTO employee 
                        (name, lastname, cedula, academic_level, job, proffesion, job_onapre, start_date, service_years, job_location, payment, nomina_type, status, children, nro_cuenta, tipo_cuenta, nro_telefono, contrato) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, True, %s, %s, %s, %s, %s);
                        """
                        cursor.execute(query, (name, lastname, cedula, academic_level, job, proffesion, onapre, start_date, workedYears, location, salary, nomina_type, children, nro_cuenta, tipo_cuenta, nro_telefono, contrato))
                        connection.commit()

                        QMessageBox.information(self, "Éxito", "Empleado creado exitosamente.")
                        self.historial.add_historial(conf.user, 'Crear Usuario', cedula)
                        self.clean_all()

            finally:
                connection.close()

        except pymysql.MySQLError as e:
            QMessageBox.critical(self, "Error", f"Error de conexión a la base de datos: {e}")


    def clean_all(self):
        self.create_user_nombre_btn.setText("")
        self.create_user_apellido_btn.setText("")
        self.create_user_cedula_btn.setText("")
        self.calendarWidget.setSelectedDate(QDate.currentDate())
        self.create_user_academic_level_btn.setCurrentIndex(0)
        self.create_user_job_btn.setText("")
        self.create_user_proffesion_btn.setText("")
        self.create_user_onapre_btn.setCurrentIndex(0)
        self.create_user_salary_btn.setText("")
        self.create_user_location_btn.setText("")
        self.create_user_children_btn.setText("")
        self.create_user_worked_years_btn.setText("")
        self.create_user_nomina_type_btn.setCurrentIndex(0)
        self.tipo_cuenta.setCurrentIndex(0)
        self.contrato.setCurrentIndex(0)
        self.nro_cuenta.setText("")
        self.nro_tlfn.setText("")


