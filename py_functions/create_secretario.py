from PyQt5.QtWidgets import QWidget
import pymysql
from ui_py.create_empleado_gestion import Ui_Form  
from py_functions.successful_change_notification import successfulWidget 

class create_secretario_window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Crear Empleado de Gestion")
        self.aceptar.clicked.connect(self.create_empleado)

    def create_empleado(self):
        connection = pymysql.connect(
                host='localhost',
                user='user_nomina',
                password='12345678',
                database='sc_db',
                charset='utf8'
                )

        cedula = self.cedula.text()
        correo = self.correo.text()
        clave = self.clave.text()
        
        try:
            with connection.cursor() as cursor:

                query = "SELECT count(*) from employee where cedula = %s"
                cursor.execute(query, (cedula,))
                res = cursor.fetchone()

                if res[0] > 0 :
                    print('Existe')

                    query = 'select count(*) from user where cedula = %s'
                    cursor.execute(query, cedula)
                    res = cursor.fetchone()

                    query2 = 'select count(*) from user where correo = %s'
                    cursor.execute(query2, correo)
                    res2 = cursor.fetchone()

                    if res[0] < 1 and res2[0] < 1:
                        query = "insert into user (cedula, clave, correo, type) values(%s,%s,%s, 'Normal')"

                        cursor.execute(query, (cedula, clave, correo))
                        connection.commit()
                        print('Hecho')
                        successfulWidget(self, message="Empleado creado exitosamente")
                        
                    else:
                        print('El correo ya esta siendo usado o ese user ya existe en secretarios')

                else:
                    print('no existe el user')
        except pymysql.MySQLError as e:
            print(f"Error de conexión a la base de datos: {e}")

        


