from PyQt5.QtWidgets import QWidget
import pymysql
from ui_py.olvide_clave_3 import Ui_Form 

class olvide_clave_3_window(QWidget, Ui_Form):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.setWindowTitle("Olvide la Clave")
            self.exit.clicked.connect(self.salir)
            self.actualizar.clicked.connect(self.cambiar_clave)
#e
        def salir(self):
            self.close() 

        def cambiar_clave(self):
            if (self.nueva_contra_1.text().strip() == self.nueva_contra_2.text().strip()) and (self.nueva_contra_1.text() != '') and (self.nueva_contra_2 != ''):
                
                nueva_clave = self.nueva_contra_1.text().strip()

                self.asignar(nueva_clave)

            else:
                print('Claves no correctas')


        def asignar(self, clave):
            connection = pymysql.connect(
                host='localhost',
                user='user_nomina',
                password='12345678',
                database='sc_db',
                charset='utf8'
                )

            try:
                with connection.cursor() as cursor: 
                    query = "update user set clave = %s where cedula = %s"
                    cursor.execute(query, (clave, self.cedula,))
                    connection.commit()
                    print('Si sirves para algo')


            except pymysql.MySQLError as e:
                print(f"Error de conexión a la base de datos: {e}")

        def cedula_is(self, cedula):
            self.cedula = cedula
            self.showMaximized()
