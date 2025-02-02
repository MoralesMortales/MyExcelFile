from PyQt5.QtWidgets import QWidget
import pymysql
from ui_py.info_empleado import Ui_Form
from py_functions.confirm_user import ConfirmDialog
from py_functions.editar_empleado import editar_empleado_window
from py_functions.create_contancia import crear_consta 
import conf
class info_empleado_window(QWidget, Ui_Form):
    def __init__(self):   
       super().__init__() 
       self.setupUi(self)
       self.cedula = 0
       self.confirm = ConfirmDialog()
       self.edit = editar_empleado_window()
       self.eliminar_btn.clicked.connect(self.delete_user)
       self.editar_btn.clicked.connect(self.edit_user)
       self.crear_constancia.clicked.connect(self.creando_consta)

    def creando_consta(self):
        crear_consta(self.cedula)

    def edit_user(self):
        self.edit.load_cedula(self.cedula)
        self.close()

    def delete_user(self):
        dialog = ConfirmDialog("¿Deseas continuar con esta acción?")
        if dialog.exec_():  # Ejecutar el diálogo
            if dialog.result:
                connection = pymysql.connect(
                        host='localhost',
                        user='root',
                        password='root',
                        database='sc_db',
                        charset='utf8'
                        )
                try:
                    with connection.cursor() as cursor:
                        query = "select count(*) from user where cedula = %s"
                        cursor.execute(query, (self.cedula,))
                        self.val = cursor.fetchone()   
                        print(self.val[0])
                        if self.cedula == conf.user:  # Verifica si el usuario intenta eliminarse a sí mismo
                            print("No puedes eliminar tu propio usuario.")
                            return

                        elif self.val[0] == 1:
                            print("No puedes eliminar a otro secretario.")
                            return

                        # Consulta SQL para eliminar el registro
                        query = "DELETE FROM employee WHERE cedula = %s"
                        cursor.execute(query, (self.cedula,))  # Ejecuta la consulta con el ID
                        connection.commit()  # Confirma los cambios en la base de datos
                
                except pymysql.MySQLError as e:
                    print('Error', e)
                
                finally:
                    connection.close()  # Cierra la conexión
                    self.close()


            else:
                print("El usuario canceló.")
        else:
            print("Diálogo cerrado sin confirmar.")

    def load_data(self):
        connection = pymysql.connect(
                host='localhost',
                user='root',
                password='root',
                database='sc_db',
                charset='utf8'
                )

        try:
            with connection.cursor() as cursor:
                query = "select concat(name,' ',lastname) as fullname from employee where cedula = %s "
                cursor.execute(query, self.cedula)
                fullname = cursor.fetchone()
                self.nombre.setText(fullname[0])
                query = "select job from employee where cedula = %s "
                cursor.execute(query, self.cedula)
                job = cursor.fetchone()
                self.trabajo.setText(job[0])

                self.trabajo_2.setText(self.cedula)
                
                query = "select academic_level from employee where cedula = %s "
                cursor.execute(query, self.cedula)
                academic = cursor.fetchone()
                self.academico.setText(academic[0])

                query = "select proffesion from employee where cedula = %s "
                cursor.execute(query, self.cedula)
                profesion = cursor.fetchone()
                self.porfesion.setText(profesion[0])

                query = "select nro_cuenta from employee where cedula = %s "
                cursor.execute(query, self.cedula)
                nro_c = cursor.fetchone()
                self.nro_cuenta.setText(nro_c[0])

                query = "select contrato from employee where cedula = %s "
                cursor.execute(query, self.cedula)
                contra = cursor.fetchone()
                self.trabajo_3.setText(contra[0])


                query = "select tipo_cuenta from employee where cedula = %s "
                cursor.execute(query, self.cedula)
                tipo_c = cursor.fetchone()
                self.account_type.setText(tipo_c[0])

                query = "select nro_telefono from employee where cedula = %s "
                cursor.execute(query, self.cedula)
                nro_t = cursor.fetchone()
                self.nro_tlfn.setText(nro_t[0])

                query = "select job_onapre from employee where cedula = %s "
                cursor.execute(query, self.cedula)
                onapre = cursor.fetchone()
                self.onapre.setText(onapre[0])

                query = "select start_date from employee where cedula = %s "
                cursor.execute(query, self.cedula)
                inicio = cursor.fetchone()
                self.inicio.setText(inicio[0].strftime("%d/%m/%Y"))

                query = "select service_years from employee where cedula = %s "
                cursor.execute(query, self.cedula)
                servicio = cursor.fetchone()
                self.servicio.setText(str(servicio[0]))

                query = "select job_location from employee where cedula = %s "
                cursor.execute(query, self.cedula)
                location = cursor.fetchone()
                self.ubicacion.setText(location[0])

                query = "select payment from employee where cedula = %s "
                cursor.execute(query, self.cedula)
                salario = cursor.fetchone()
                self.salario.setText(str(salario[0]))

                query = "select nomina_type from employee where cedula = %s "
                cursor.execute(query, self.cedula)
                nomina = cursor.fetchone()
                self.nomina.setText(nomina[0])

                query = "select children from employee where cedula = %s "
                cursor.execute(query, self.cedula)
                hijos = cursor.fetchone()
                self.hijos.setText(str(hijos[0]))

                query = "select status from employee where cedula = %s "
                cursor.execute(query, self.cedula)
                status = cursor.fetchone()
                estado_texto = "Activo" if status[0] == 1 else "Inactivo"
                self.estatus.setText(estado_texto)

        except pymysql.MySQLError as e:
            print(f"Error de conexión a la base de datos: {e}")

    def open_window(self, cedula):
        self.show()
        print(cedula)
        self.cedula = cedula
        self.load_data()



