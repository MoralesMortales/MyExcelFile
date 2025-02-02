from ui_py.create_nominas_mensual import Ui_Form
from py_functions.edit_info_nomina import edit_info_nomina 
from datetime import datetime
from PyQt5.QtCore import QModelIndex, QSortFilterProxyModel, Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel
import pymysql
from PyQt5.QtWidgets import QHeaderView, QWidget
from py_functions.pdf_create_quincena import generate_pdf
from py_functions.successful_change_notification import successfulWidget
import conf
from datetime import datetime
import calendar
from py_functions.historial import historial_view

from py_functions.pdf_listado_nomina_q1 import generate_pdf_lista 

class createNominasMensual(QWidget, Ui_Form):
    def __init__(self):   
       super().__init__()
       self.setupUi(self)
       self.model = QStandardItemModel()
       self.proxy_model = QSortFilterProxyModel()
       self.proxy_model.setSourceModel(self.model)
       self.tableView.setModel(self.proxy_model)
       self.tableView.doubleClicked.connect(self.clicked_row)
       self.prev_create.clicked.connect(self.create_nomina)
       self.confirm.clicked.connect(self.insert_confirm)
       self.prev_pdf.clicked.connect(self.execute_pdf)
       self.listado_nominas.clicked.connect(self.execute_list)

       self.half = False
       self.ready = False

    def execute_pdf(self):
        generate_pdf('M')

    def execute_list(self):
        generate_pdf_lista('M')


    def vals(self):

        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='sc_db',
            charset='utf8'
        )
        
        try:
            with connection.cursor() as cursor:
                # Realizar la primera consulta para obtener las filas
                query = "truncate table employee_prev;"
                cursor.execute(query)
                connection.commit()

                query = """SELECT e.cedula, CONCAT(e.name, ' ', e.lastname) AS fullname, e.job_location, e.nomina_type, COALESCE(n.fecha) AS fecha, COALESCE(n.fecha_fin) AS fecha_fin FROM employee e LEFT JOIN nominas n ON e.cedula = n.cedula WHERE e.nomina_type = 'Mensual' AND e.status = 1 AND NOT EXISTS ( SELECT 1 FROM nominas_prev n_sub WHERE n_sub.cedula = e.cedula AND YEAR(n_sub.fecha) = YEAR(CURDATE()) AND MONTH(n_sub.fecha) = MONTH(CURDATE()));"""
                cursor.execute(query)
                rows = cursor.fetchall()
                self.model.clear()

                for row_idx, row in enumerate(rows):
                    for col_idx, value in enumerate(row):
                        item = QStandardItem(str(value))
                        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                        self.model.setItem(row_idx, col_idx, item)
                        self.adjust_table_settings()

                headers = ["Cedula de Empleado", "Nombre de Empleado", "Ubicacion Laboral", "Tipo de nomina"]
                self.model.setHorizontalHeaderLabels(headers)
                insert_query = """
                INSERT INTO employee_prev (cedula, name, location, nomina_type) VALUES (%s, %s, %s, %s);
                """
                for nomina in rows:
                    print("Insertando los siguientes datos:", nomina[0], nomina[1], nomina[2], nomina[3])  # Depuración
                    cursor.execute(insert_query, (nomina[0], nomina[1], nomina[2], nomina[3]))

                connection.commit()
                print("Datos insertados exitosamente en la tabla 'nominas'.")

        except pymysql.MySQLError as e:
            print(f"Error de conexión a la base de datos: {e}")

        finally:
            connection.close()

    def insert_confirm(self):
        if self.ready:
            print('good')
        else:
            print('no good')
            return
        print('working')
        try:
            connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='sc_db',
        charset='utf8'
    )
            self.vals
            cursor = connection.cursor()

            query = "SELECT * FROM nominas"
            cursor.execute(query)
            nominas = cursor.fetchall()
            print('inserting nowwwwwwwww')
            send_history = historial_view()
 
            for nomina in nominas:
                query = "INSERT INTO nominas_prev(cedula, sueldo_base, prima_transporte, prima_hogar, prima_alimentacion, prima_hijo, prima_antiguedad, prima_profesion, asignaciones, deducciones_T,pf,ivss,faov,cuota_sindical,total_neto,fecha,type,fecha_fin,made_by, retributions, created) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, curdate())"
                cursor.execute(query, (nomina[0], nomina[1], nomina[2], nomina[3], nomina[4], nomina[5], nomina[6], nomina[7], nomina[8], nomina[9], nomina[10], nomina[11], nomina[12], nomina[13], nomina[14], nomina[15], nomina[16], nomina[17], nomina[18], nomina[19]))
                send_history.add_historial(conf.user,"Crear Nomina", nomina[0])
                connection.commit()
                print('done')

        except pymysql.MySQLError as e:
            print(f"Error al interactuar con la base de datos: {e}")

        finally:
            connection.close()
            self.vals
            self.ready = False
            if len(nominas) > 0:
                successfulWidget(self, message="Nominas creadas exitosamente")


    def show_nominas(self):
        connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='sc_db',
        charset='utf8'
    )
        print('showing')
        try:
            with connection.cursor() as cursor:
            # Realizar la primera consulta para obtener las filas
                query = """
select * from employee_prev;
"""
                cursor.execute(query)
                rows = cursor.fetchall()

        # Limpiar el modelo
                self.model.clear()

        # Llenar la tabla con los resultados
                for row_idx, row in enumerate(rows):
                    for col_idx, value in enumerate(row):    
                        item = QStandardItem(str(value))
                        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # No editable
                        self.model.setItem(row_idx, col_idx, item)
                        self.adjust_table_settings()

                headers = ["Cedula de Empleado","Nombre de Empleado",  "Ubicacion Laboral", "Tipo de nomina"]
                self.model.setHorizontalHeaderLabels(headers)

        # Insertar los datos en la tabla 'nominas'
                insert_query = """
            INSERT INTO employee_prev (cedula, name, location, nomina_type) VALUES (%s, %s, %s, %s);
            """
                for nomina in rows:
                    print("Insertando los siguientes datos:",nomina[0],nomina[1],nomina[2],nomina[3] )  # Imprimir datos para depuración
                    cursor.execute(insert_query, (nomina[0], nomina[1], nomina[2],nomina[3]))

        # Confirmar la transacción
                connection.commit()
                print("Datos insertados exitosamente en la tabla 'nominas'.")

        except pymysql.MySQLError as e:
            print(f"Error de conexión a la base de datos: {e}")
        finally:
            connection.close()
    def adjust_table_settings(self):
        """Ajustar configuración de la tabla."""
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setSelectionBehavior(self.tableView.SelectRows)
        self.tableView.setStyleSheet("""
            QTableView::item:selected {
                background-color: #4CAF50;
                color: white;
            }
        """)

    def clicked_row(self, index: QModelIndex):
            source_index = self.proxy_model.mapToSource(index)
            cedula_index = source_index.siblingAtColumn(0)
            cedula = self.model.itemFromIndex(cedula_index).text()
            print(cedula, '!!!')
            self.nominaInfo = edit_info_nomina()
            self.nominaInfo.open_window(cedula, 'M')

    def create_nomina(self):

        connection = pymysql.connect(
                host='localhost',
                user='root',
                password='root',
                database='sc_db',
                charset='utf8'
                )
        cursor = connection.cursor()
        self.ready = True
        self.vals()
        query = 'truncate table nominas;'
        cursor.execute(query)

        connection.commit()

        self.show_nominas()
        query = "SELECT e.cedula FROM employee_prev e WHERE e.nomina_type = 'Mensual';"
        cursor.execute(query)
        empleados= cursor.fetchall()
        print(empleados)
        for empleado in empleados:
             print(empleado)
             asignaciones_user = 0
             cedula_user = empleado[0]
             
             query = "SELECT payment from employee where cedula = %s "
             cursor.execute(query, cedula_user)
             payment = cursor.fetchone()
             
             query = "SELECT children from employee where cedula = %s "
             cursor.execute(query, cedula_user)   
             hijos = cursor.fetchone()
     
             query = "SELECT service_years from employee where cedula = %s "
             cursor.execute(query, cedula_user)
              
             service_years = cursor.fetchone()
             service_years = service_years[0]
                
             query = "SELECT academic_level from employee where cedula = %s "
             cursor.execute(query, cedula_user)
                
             profession = cursor.fetchone()
             profession = str(profession[0])

             payment = payment[0]
             payment = payment
             asignaciones = asignaciones_user + payment + conf.prima_hogar + conf.prima_transporte + conf.prima_alimentacion + conf.prima_hijo*float(hijos[0]) + (conf.prima_profesion[str(profession)]/100)*(payment) + (conf.prima_anti[min(str(service_years), '23')]/100)*(payment)

             ivss = ((payment)*12)/52*0.04*4
             ivss = round(ivss,2)
             faov = 0.01*asignaciones
             faov = round(faov,2)
             p_f = ((payment)*12)/52*0.005*4
             p_f = round(p_f,2)
             cuota_sindical = 0 

             current_date = datetime.now()

             selected_date_start = current_date.replace(day=1).strftime('%d-%m-%Y')

             last_day = calendar.monthrange(current_date.year, current_date.month)[1]

             selected_date_end = current_date.replace(day=last_day).strftime('%d-%m-%Y') 

             selected_date_start = datetime.strptime(selected_date_start, "%d-%m-%Y")

             selected_date_end = datetime.strptime(selected_date_end, "%d-%m-%Y")
             
             deducciones = ivss + faov + p_f + cuota_sindical
             deducciones = round(deducciones,2)
             neto = asignaciones - deducciones
             neto = round(neto,2)

             print('sending')

             #query = "truncate table employee_prev;"
             #cursor.execute(query)
             #connection.commit()

             self.create_nomina_fnt(cedula_user, 
                                                   payment,
                                                   round(conf.prima_transporte,2),
                                                   round(conf.prima_hogar,2),
                                                   round(conf.prima_alimentacion,2),
                                                   round(conf.prima_hijo*float(hijos[0]), 2),
                                                   round((conf.prima_anti[min(str(service_years), '23')]/100)*payment,2),
                                                   round((conf.prima_profesion[profession]/100)*payment,2),
                                                   asignaciones,
                                                   deducciones,
                                                   p_f,
                                                   ivss,
                                                   faov,
                                                   cuota_sindical,
                                                   neto,selected_date_start,
                                                   'Mensual',
                                                   selected_date_end,
                                                   asignaciones_user)


    def create_nomina_fnt(self, cedula, sueldo_base, prima_transporte, prima_hogar, prima_alimentacion, prima_hijo, prima_antiguedad, prima_profesion, asignaciones, deducciones_T, pf,ivss,faov,cuota_sindical,total_neto,fecha,tipo,fecha_fin, asignaciones_user):

        print("Ejecutando create_nomina_fnt con los siguientes parámetros:")
        print(f"""
cedula: {cedula}
sueldo_base: {sueldo_base}
prima_transporte: {prima_transporte}
prima_hogar: {prima_hogar}
prima_alimentacion: {prima_alimentacion}
prima_hijo: {prima_hijo}
prima_antiguedad: {prima_antiguedad}
prima_profesion: {prima_profesion}
asignaciones: {asignaciones}
deducciones_T: {deducciones_T}
pf: {pf}
ivss: {ivss}
faov: {faov}
cuota_sindical: {cuota_sindical}
total_neto: {total_neto}
fecha: {fecha}
tipo: {tipo}
fecha_fin: {fecha_fin}
extras: {asignaciones_user}
""")

        connection = pymysql.connect(
                host='localhost',
                user='root',
                password='root',
                database='sc_db',
                charset='utf8'
                )
        try:
            with connection.cursor() as cursor:
                print('inserting on nominas')

                query = "insert into nominas(cedula, sueldo_base, prima_transporte, prima_hogar, prima_alimentacion, prima_hijo, prima_antiguedad, prima_profesion, asignaciones, deducciones_T,pf,ivss,faov,cuota_sindical,total_neto,fecha,type,fecha_fin,made_by, retributions) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                cursor.execute(query, (cedula, sueldo_base, prima_transporte, prima_hogar, prima_alimentacion, prima_hijo, prima_antiguedad, prima_profesion, asignaciones, deducciones_T, pf, ivss, faov, cuota_sindical, total_neto, fecha, tipo, fecha_fin, conf.user, asignaciones_user))
                connection.commit()

                self.show_nominas()

        except pymysql.MySQLError as e:
            print(f"Error de conexión a la base de datos: {e}")
