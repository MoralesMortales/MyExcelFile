from PyQt5.QtWidgets import QWidget
import pymysql
from ui_py.info_nomina import Ui_Form 

class info_nomina_window(QWidget, Ui_Form):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.cedula = 0
            #self.confirm = ConfirmDialog()
            #self.edit = editar_empleado_window()
            #self.eliminar_btn.clicked.connect(self.delete_user)
            #self.editar_btn.clicked.connect(self.edit_user)

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
                    print('mira', self.cedula)
                    query = "select concat(name,' ',lastname) as fullname from employee where cedula = %s "
                    cursor.execute(query, self.cedula)
                    fullname = cursor.fetchone()
                    self.nombre.setText(f'{fullname[0]} (Nómina)')

                    query = "select nomina_type from employee where cedula = %s "
                    cursor.execute(query, self.cedula)
                    tipo_n = cursor.fetchone()
                    if tipo_n[0] == 'Semanal':
                        query = "select prima_transporte from nomina_semanal where cedula = %s "
                        cursor.execute(query, self.cedula)
                        academic = cursor.fetchone()
                        self.academico.setText(str(academic[0]))

                        query = "select prima_alimentacion from nomina_semanal where cedula = %s "
                        cursor.execute(query, self.cedula)
                        profesion = cursor.fetchone()
                        self.porfesion.setText(str(profesion[0]))

                        query = "select prima_antiguedad from nomina_semanal where cedula = %s "
                        cursor.execute(query, self.cedula)
                        onapre = cursor.fetchone()
                        self.onapre.setText(str(onapre[0]))

                        query = "select asignaciones from nomina_semanal where cedula = %s "
                        cursor.execute(query, self.cedula)
                        inicio = cursor.fetchone()
                        self.inicio.setText(str(inicio[0]))

                        query = "select pf from nomina_semanal where cedula = %s "
                        cursor.execute(query, self.cedula)
                        servicio = cursor.fetchone()
                        self.servicio.setText(str(servicio[0]))

                        query = "select faov from nomina_semanal where cedula = %s "
                        cursor.execute(query, self.cedula)
                        location = cursor.fetchone()
                        self.ubicacion.setText(str(location[0]))
                        query = "select total_neto from nomina_semanal where cedula = %s "
                        cursor.execute(query, self.cedula)
                        salario = cursor.fetchone()
                        self.salario.setText(str(salario[0]))
                        query = "select fecha from nomina_semanal where cedula = %s "
                        cursor.execute(query, self.cedula)
                        nomina = cursor.fetchone()
                        self.nomina.setText(nomina[0].strftime("%d/%m/%Y"))

                        query = "select made_by from nomina_semanal where cedula = %s "
                        cursor.execute(query, self.cedula)
                        made_by = cursor.fetchone()
                        query = "select concat(name,' ',lastname) as fullname from employee where cedula = %s "
                        cursor.execute(query, made_by)
                        created_by = cursor.fetchone()
                        self.estatus.setText(str(created_by[0]))

                        query = "select sueldo_base from nomina_semanal where cedula = %s "
                        cursor.execute(query, self.cedula)
                        nomina = cursor.fetchone()
                        self.trabajo_2.setText(str(nomina[0]))
                   
                        query = "select prima_hogar from nomina_semanal where cedula = %s "
                        cursor.execute(query, self.cedula)
                        academic = cursor.fetchone()
                        self.academico_2.setText(str(academic[0]))

                        query = "select prima_hijo from nomina_semanal where cedula = %s "
                        cursor.execute(query, self.cedula)
                        profesion_2 = cursor.fetchone()
                        self.porfesion_2.setText(str(profesion_2[0]))

                        query = "select prima_profesion from nomina_semanal where cedula = %s "
                        cursor.execute(query, self.cedula)
                        onapre_2 = cursor.fetchone()
                        self.onapre_2.setText(str(onapre_2[0]))

                        query = "select deducciones_T from nomina_semanal where cedula = %s "
                        cursor.execute(query, self.cedula)
                        inicio_2 = cursor.fetchone()
                        self.inicio_2.setText(str(inicio_2[0]))

                        query = "select ivss from nomina_semanal where cedula = %s "
                        cursor.execute(query, self.cedula)
                        servicio_2 = cursor.fetchone()
                        self.servicio_2.setText(str(servicio_2[0]))

                        query = "select cuota_sindical from nomina_semanal where cedula = %s "
                        cursor.execute(query, self.cedula)
                        location = cursor.fetchone()
                        self.ubicacion_2.setText(str(location[0]))

                        query = "select type from nomina_semanal where cedula = %s "
                        cursor.execute(query, self.cedula)
                        salario = cursor.fetchone()
                        self.salario_2.setText(str(salario[0]))

                        query = "select fecha_fin from nomina_semanal where cedula = %s "
                        cursor.execute(query, self.cedula)
                        nomina = cursor.fetchone()
                        self.nomina_2.setText(str(nomina[0].strftime("%d/%m/%Y")))

                    else:
                        query = "select prima_transporte from nominas_prev where cedula = %s "
                        cursor.execute(query, self.cedula)
                        academic = cursor.fetchone()
                        self.academico.setText(str(academic[0]))

                        query = "select prima_alimentacion from nominas_prev where cedula = %s "
                        cursor.execute(query, self.cedula)
                        profesion = cursor.fetchone()
                        self.porfesion.setText(str(profesion[0]))

                        query = "select prima_antiguedad from nominas_prev where cedula = %s "
                        cursor.execute(query, self.cedula)
                        onapre = cursor.fetchone()
                        self.onapre.setText(str(onapre[0]))

                        query = "select asignaciones from nominas_prev where cedula = %s "
                        cursor.execute(query, self.cedula)
                        inicio = cursor.fetchone()
                        self.inicio.setText(str(inicio[0]))

                        query = "select pf from nominas_prev where cedula = %s "
                        cursor.execute(query, self.cedula)
                        servicio = cursor.fetchone()
                        self.servicio.setText(str(servicio[0]))

                        query = "select faov from nominas_prev where cedula = %s "
                        cursor.execute(query, self.cedula)
                        location = cursor.fetchone()
                        self.ubicacion.setText(str(location[0]))
                        query = "select total_neto from nominas_prev where cedula = %s "
                        cursor.execute(query, self.cedula)
                        salario = cursor.fetchone()
                        self.salario.setText(str(salario[0]))
                        query = "select fecha from nominas_prev where cedula = %s "
                        cursor.execute(query, self.cedula)
                        nomina = cursor.fetchone()
                        self.nomina.setText(nomina[0].strftime("%d/%m/%Y"))

                        query = "select made_by from nominas_prev where cedula = %s "
                        cursor.execute(query, self.cedula)
                        made_by = cursor.fetchone()
                        query = "select concat(name,' ',lastname) as fullname from employee where cedula = %s "
                        cursor.execute(query, made_by)
                        created_by = cursor.fetchone()
                        self.estatus.setText(str(created_by[0]))

                        query = "select sueldo_base from nominas_prev where cedula = %s "
                        cursor.execute(query, self.cedula)
                        nomina = cursor.fetchone()
                        self.trabajo_2.setText(str(nomina[0]))
                   
                        query = "select prima_hogar from nominas_prev where cedula = %s "
                        cursor.execute(query, self.cedula)
                        academic = cursor.fetchone()
                        self.academico_2.setText(str(academic[0]))

                        query = "select prima_hijo from nominas_prev where cedula = %s "
                        cursor.execute(query, self.cedula)
                        profesion_2 = cursor.fetchone()
                        self.porfesion_2.setText(str(profesion_2[0]))

                        query = "select prima_profesion from nominas_prev where cedula = %s "
                        cursor.execute(query, self.cedula)
                        onapre_2 = cursor.fetchone()
                        self.onapre_2.setText(str(onapre_2[0]))

                        query = "select deducciones_T from nominas_prev where cedula = %s "
                        cursor.execute(query, self.cedula)
                        inicio_2 = cursor.fetchone()
                        self.inicio_2.setText(str(inicio_2[0]))

                        query = "select ivss from nominas_prev where cedula = %s "
                        cursor.execute(query, self.cedula)
                        servicio_2 = cursor.fetchone()
                        self.servicio_2.setText(str(servicio_2[0]))

                        query = "select cuota_sindical from nominas_prev where cedula = %s "
                        cursor.execute(query, self.cedula)
                        location = cursor.fetchone()
                        self.ubicacion_2.setText(str(location[0]))

                        query = "select type from nominas_prev where cedula = %s "
                        cursor.execute(query, self.cedula)
                        salario = cursor.fetchone()
                        self.salario_2.setText(str(salario[0]))

                        query = "select fecha_fin from nominas_prev where cedula = %s "
                        cursor.execute(query, self.cedula)
                        nomina = cursor.fetchone()
                        self.nomina_2.setText(str(nomina[0].strftime("%d/%m/%Y")))
      
            except pymysql.MySQLError as e:
                 print(f"Error de conexión a la base de datos: {e}")
            
        def open_window(self, cedula):
            self.show()
            print(cedula)
            self.cedula = cedula
            self.load_data()



            

