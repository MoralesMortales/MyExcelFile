from PyQt5.QtWidgets import QMessageBox, QWidget
import pymysql
from PyQt5.QtCore import QDate, QRegExp
from PyQt5.QtGui import QRegExpValidator, QDoubleValidator
from ui_py.editar_empleado import Ui_Form
import datetime
from PyQt5.QtCore import QDate


class editar_empleado_window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Editar Empleado")
        self.cedula = 0
        doubleRange = QDoubleValidator(0.0, 9999.9, 2, self)
        intRange = QDoubleValidator(0.0, 99.9, 0, self)
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

        self.load_employee_data()
        self.create_employee_btn.clicked.connect(self.update_employee_data)

    def load_cedula(self, cedula):
        self.cedula = cedula
        self.load_employee_data()
        self.showMaximized()

    def load_employee_data(self):
        cedula = self.cedula
        conn = pymysql.connect(
            host='localhost',
            user='user_nomina',
            password='12345678',
            database='sc_db',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor)
        try:
            with conn.cursor() as cursor:
                query = "SELECT * FROM employee WHERE cedula = %s"
                cursor.execute(query, (cedula,))
                employee = cursor.fetchone()

                if employee:
                    self.create_user_nombre_btn.setText(employee["name"])
                    self.create_user_apellido_btn.setText(employee["lastname"])
                    self.create_user_cedula_btn.setText(str(employee["cedula"]))
                    self.create_user_academic_level_btn.setCurrentText(employee["academic_level"])
                    self.create_user_job_btn.setText(employee["job"])
                    self.create_user_proffesion_btn.setText(employee["proffesion"])
                    self.create_user_onapre_btn.setCurrentText(employee["job_onapre"])
                    self.create_user_location_btn_3.setText(employee["job_location"])
                    self.create_user_children_btn.setText(str(employee["children"]))
                    self.create_user_worked_years_btn.setText(str(employee["service_years"]))
                    self.create_user_salary_btn.setText(str(employee["payment"]))
                    self.create_user_nomina_type_btn.setCurrentText(employee["nomina_type"])
                    self.nro_cuenta.setText(str(employee["nro_cuenta"]))
                    self.tipo_cuenta.setCurrentText(employee["tipo_cuenta"])
                    self.contrato.setCurrentText(employee["contrato"])
                    self.nro_tlfn.setText(str(employee["nro_telefono"]))
                    self.create_user_location_btn_2.setCurrentText("Activo" if employee["status"] == 1 else "Inactivo")

                    start_date = employee["start_date"]
                    if isinstance(start_date, datetime.date):
                        start_date_str = start_date.strftime("%Y-%m-%d")
                        qdate = QDate.fromString(start_date_str, "yyyy-MM-dd")
                        self.calendarWidget.setSelectedDate(qdate)

        except pymysql.MySQLError as e:
            QMessageBox.critical(self, "Error", f"Error de conexión a la base de datos: {e}")
        finally:
            conn.close()

    def update_employee_data(self):
        # Validación de campos
        name = self.create_user_nombre_btn.text().strip()
        print('El nombre es igual a ', name)
        lastname = self.create_user_apellido_btn.text().strip()
        cedula = self.create_user_cedula_btn.text().strip()
        start_date = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        academic_level = self.create_user_academic_level_btn.currentText()
        job = self.create_user_job_btn.text().strip().capitalize()
        proffesion = self.create_user_proffesion_btn.text().strip().capitalize()
        nro_telefono = self.nro_tlfn.text().strip()
        onapre = self.create_user_onapre_btn.currentText()
        salary = self.create_user_salary_btn.text().strip()
        location = self.create_user_location_btn_3.text().strip().capitalize()
        children = self.create_user_children_btn.text().strip()
        workedYears = self.create_user_worked_years_btn.text().strip()
        nomina_type = self.create_user_nomina_type_btn.currentText()
        contrato = self.contrato.currentText()
        tipo_cuenta = self.tipo_cuenta.currentText()
        nro_cuenta = self.nro_cuenta.text().strip()

        if not all([name, lastname, cedula, academic_level, job, proffesion, onapre, salary, location, children, workedYears, nro_cuenta, tipo_cuenta, nro_telefono, contrato]):
            QMessageBox.warning(self, "Faltan datos", "Por favor, complete todos los campos.")
            return

        if len(nro_cuenta) != 20:
            QMessageBox.warning(self, "Número de cuenta inválido", "El número de cuenta debe tener exactamente 20 dígitos.")
            return

        try:
            conn = pymysql.connect(
                host='localhost',
                user='user_nomina',
                password='12345678',
                database='sc_db',
                charset='utf8')

            try:
                with conn.cursor() as cursor:
                    query = """
                    UPDATE employee SET
                        name = %s,
                        lastname = %s,
                        academic_level = %s,
                        job = %s,
                        proffesion = %s,
                        job_onapre = %s,
                        job_location = %s,
                        children = %s,
                        service_years = %s,
                        payment = %s,
                        nomina_type = %s,
                        start_date = %s,
                        status = %s,
                        nro_cuenta = %s,
                        tipo_cuenta = %s,
                        nro_telefono = %s,
                        contrato = %s
                    WHERE cedula = %s
                    """

                    val_status = 1 if self.create_user_location_btn_2.currentText().strip() == "Activo" else 0

                    data = (
                        name, lastname, academic_level, job, proffesion, onapre,
                        location, int(children), int(workedYears), float(salary),
                        nomina_type, start_date, val_status, nro_cuenta,
                        tipo_cuenta, nro_telefono, contrato,int(cedula)
                    )

                    cursor.execute(query, data)
                    conn.commit()

                    QMessageBox.information(self, "Éxito", "Datos actualizados correctamente.")
                    self.close()

            finally:
                conn.close()

        except pymysql.MySQLError as e:
            QMessageBox.critical(self, "Error", f"Error al actualizar los datos: {e}")
