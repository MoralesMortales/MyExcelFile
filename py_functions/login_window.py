import pymysql
from ui_py.login import Ui_Login_form
from PyQt5.QtWidgets import QWidget
from py_functions.menu_window import MainApp
from py_functions.olvide_clave_1 import olvide_clave_1_window
import conf

class LoginWindow(QWidget, Ui_Login_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.olvide_clave = olvide_clave_1_window()
        self.mainWindow = MainApp()
        self.label_9.mousePressEvent = self.forgot_password
        self.login_validation.clicked.connect(self.show_main_window)

    def show_main_window(self):
        user = self.insertCedula.text()
        password = self.InsertClave.text()
        try:
            connection = pymysql.connect(
                    host='localhost',
                    user='user_nomina',
                    password='12345678',
                    database='sc_db',
                    charset='utf8'
                )
            with connection.cursor() as cursor:
                query = "SELECT * FROM user WHERE cedula = %s AND clave = %s"
                cursor.execute(query, (user, password))
                result = cursor.fetchone()

                if result:
                    self.mainWindow.load_type(user)
                    conf.user = user
                    self.close()
                else:
                    print("Usuario o contraseña incorrectos.")
        
        except pymysql.MySQLError as e:
            print(f"Error en login: {e}")

    def forgot_password(self, event):
        self.olvide_clave.showMaximized()
        self.close()


