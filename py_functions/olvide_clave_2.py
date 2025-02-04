from PyQt5.QtWidgets import QWidget
import pymysql
from ui_py.olvide_clave_2 import Ui_Form
import random
import yagmail
from py_functions.olvide_clave_3 import olvide_clave_3_window 

class olvide_clave_2_window(QWidget, Ui_Form):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.exit.clicked.connect(self.salir)
            self.validar.clicked.connect(self.validator)
            self.olvide_clave_3 = olvide_clave_3_window()

        def salir(self):
            self.close()

        def send_code(self):
            connection = pymysql.connect(
                host='localhost',
                user='user_nomina',
                password='12345678',
                database='sc_db',
                charset='utf8'
                )

            try:
                with connection.cursor() as cursor: 
                    query = "SELECT correo from user where cedula = %s"
                    cursor.execute(query, (self.cedula,))
                    res = cursor.fetchone()
                    print(res[0])

            except pymysql.MySQLError as e:
                print(f"Error de conexión a la base de datos: {e}")

            user = 'validador38@gmail.com'
            password = 'svgcdnaiglujawdy '

            yag = yagmail.SMTP(user,password)

            code = random.randint(1000,9999)
            self.code = code
            receiver = res[0]
            topic = 'IMPORTANT EMERGENCY'
            message = f'Bienvedio al Validador! \n\nTu codigo de un solo uso es: {code}'

            yag.send(to=receiver, subject=topic, contents=message)

            print(f'Mensaje enviado a {res[0]}')

        def asign_cedula(self, cedula):
            self.cedula = cedula
            self.showMaximized()
            self.send_code()

        def validator(self):
            self.mycode = self.ingresa_codigo.text()
            val_user = self.mycode
            val_app = str(self.code)
            print(val_user,'-',val_app)

            if val_user.strip() == val_app:
                self.olvide_clave_3.cedula_is(self.cedula)

            else:
                print('No sirves para nada')




 


