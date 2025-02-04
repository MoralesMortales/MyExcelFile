from PyQt5.QtWidgets import QWidget
import pymysql
from ui_py.delete_empleado_gestion import Ui_Form 
from py_functions.successful_change_notification import successfulWidget 
import conf

class delete_secretario_window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Borrar Empleado de Gestion")
        self.aceptar.clicked.connect(self.delete_secretario)

    def delete_secretario(self):
        cedula = self.cedula.text()

        connection = pymysql.connect(
                host='localhost',
                user='user_nomina',
                password='12345678',
                database='sc_db',
                charset='utf8'
                )
        try:
            with connection.cursor() as cursor:
                
                queryc = "select cedula from employee where cedula = %s"
                cursor.execute(queryc, conf.user)
                user_cedula = cursor.fetchone()


                query = "SELECT count(*) from user where cedula = %s"
                cursor.execute(query, (cedula,))
                res = cursor.fetchone()
                print(user_cedula[0], cedula)

                if res[0] > 0 and str(user_cedula[0]) != str(cedula).strip():
                    query = 'delete from user where cedula = %s'
                    cursor.execute(query, cedula)
                    connection.commit()
                    successfulWidget(self, message="Empleado de Gestión eliminado exitosamente")

        except pymysql.MySQLError as e:
            print(f"Error de conexión a la base de datos: {e}")



        


