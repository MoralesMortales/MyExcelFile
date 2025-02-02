from PyQt5.QtWidgets import QWidget
import pymysql
from ui_py.olvide_clave_1 import Ui_Form 
from py_functions.olvide_clave_2 import olvide_clave_2_window 

class olvide_clave_1_window(QWidget, Ui_Form):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.exit.clicked.connect(self.salir)
            self.cedula = 0
            self.olvide_clave2 = olvide_clave_2_window()
            self.enviar_codigo.clicked.connect(self.send_code)
        
        def salir(self):
            self.close()

        def send_code(self):
            self.cedula = self.ingresa_cedula.text()
            connection = pymysql.connect(
                host='localhost',
                user='root',
                password='root',
                database='sc_db',
                charset='utf8'
                )

            try:
                with connection.cursor() as cursor: 
                    query = "SELECT count(*) from employee where cedula = %s"
                    cursor.execute(query, (self.cedula,))
                    res = cursor.fetchone()
                    if res[0] > 0:
                        print('Existe')
                        self.olvide_clave2.asign_cedula(self.cedula)
                        self.close()

                    else: 
                        print('No existe', self.cedula, res[0])


            except pymysql.MySQLError as e:
                print(f"Error de conexión a la base de datos: {e}")

