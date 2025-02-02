
from datetime import datetime
#from py_functions.historial import send_to_history
from PyQt5.QtCore import QModelIndex, QSortFilterProxyModel, Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel
import pymysql
from ui_py.create_nomina_semanal import Ui_Form
from py_functions.edit_info_nomina import edit_info_nomina 
from PyQt5.QtWidgets import QHeaderView, QWidget
from py_functions.pdf_create_quincena import generate_pdf
from py_functions.successful_change_notification import successfulWidget
import conf
from datetime import datetime
import calendar
from py_functions.historial import historial_view
from py_functions.pdf_listado_nomina_q1 import generate_pdf_lista 


class createNominasSemanal(QWidget, Ui_Form):
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
       self.week = 0

    def execute_pdf(self):
        generate_pdf('S')

    def execute_list(self):
        generate_pdf_lista('S')

    def vals(self):

        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='sc_db',
            charset='utf8'
        )
        
        print('showinggg')
        try:
            with connection.cursor() as cursor:
                # Realizar la primera consulta para obtener las filas
                query = "truncate table employee_prev;"
                cursor.execute(query)
                connection.commit()
                print(self.week)

                if self.week == 1:
                    query = """
                SELECT e.cedula, CONCAT(e.name, ' ', e.lastname) AS fullname, e.job_location, e.nomina_type
                FROM employee e
                LEFT JOIN nomina_semanal_prev n ON e.cedula = n.cedula
                LEFT JOIN (
                    SELECT cedula, MONTH(fecha) AS mes, YEAR(fecha) AS anio, 
                           COUNT(*) AS cantidad_nominas 
                    FROM nomina_semanal 
                    GROUP BY cedula, YEAR(fecha), MONTH(fecha) 
                    HAVING cantidad_nominas < 2
                ) t ON n.cedula = t.cedula AND MONTH(n.fecha) = t.mes AND YEAR(n.fecha) = t.anio
                WHERE e.nomina_type = 'Semanal' 
                AND e.status = 1
                AND NOT EXISTS (
                    SELECT 1 
                    FROM nomina_semanal n_sub 
                    WHERE n_sub.cedula = e.cedula 
                      AND YEAR(n_sub.fecha_fin) = YEAR(CURDATE()) 
                      AND MONTH(n_sub.fecha_fin) = MONTH(CURDATE()) 
                      AND DAY(n_sub.fecha) IN (1));
                """
                elif self.week == 2:
                    query = """
                SELECT e.cedula, CONCAT(e.name, ' ', e.lastname) AS fullname, e.job_location, e.nomina_type
                FROM employee e
                LEFT JOIN nomina_semanal_prev n ON e.cedula = n.cedula
                LEFT JOIN (
                    SELECT cedula, MONTH(fecha) AS mes, YEAR(fecha) AS anio, 
                           COUNT(*) AS cantidad_nominas 
                    FROM nomina_semanal 
                    GROUP BY cedula, YEAR(fecha), MONTH(fecha) 
                    HAVING cantidad_nominas < 2
                ) t ON n.cedula = t.cedula AND MONTH(n.fecha) = t.mes AND YEAR(n.fecha) = t.anio
                WHERE e.nomina_type = 'Semanal' 
                AND e.status = 1
                AND NOT EXISTS (
                    SELECT 1 
                    FROM nomina_semanal n_sub 
                    WHERE n_sub.cedula = e.cedula 
                      AND YEAR(n_sub.fecha_fin) = YEAR(CURDATE()) 
                      AND MONTH(n_sub.fecha_fin) = MONTH(CURDATE()) 
                      AND DAY(n_sub.fecha) IN (8));
                """
                elif self.week == 3:
                    query = """
                SELECT e.cedula, CONCAT(e.name, ' ', e.lastname) AS fullname, e.job_location, e.nomina_type
                FROM employee e
                LEFT JOIN nomina_semanal_prev n ON e.cedula = n.cedula
                LEFT JOIN (
                    SELECT cedula, MONTH(fecha) AS mes, YEAR(fecha) AS anio, 
                           COUNT(*) AS cantidad_nominas 
                    FROM nomina_semanal 
                    GROUP BY cedula, YEAR(fecha), MONTH(fecha) 
                    HAVING cantidad_nominas < 2
                ) t ON n.cedula = t.cedula AND MONTH(n.fecha) = t.mes AND YEAR(n.fecha) = t.anio
                WHERE e.nomina_type = 'Semanal' 
                AND e.status = 1
                AND NOT EXISTS (
                    SELECT 1 
                    FROM nomina_semanal n_sub 
                    WHERE n_sub.cedula = e.cedula 
                      AND YEAR(n_sub.fecha_fin) = YEAR(CURDATE()) 
                      AND MONTH(n_sub.fecha_fin) = MONTH(CURDATE()) 
                      AND DAY(n_sub.fecha) IN (15)
                );
                """
                elif self.week == 4:
                    query = """
                SELECT e.cedula, CONCAT(e.name, ' ', e.lastname) AS fullname, e.job_location, e.nomina_type
                FROM employee e
                LEFT JOIN nomina_semanal_prev n ON e.cedula = n.cedula
                LEFT JOIN (
                    SELECT cedula, MONTH(fecha) AS mes, YEAR(fecha) AS anio, 
                           COUNT(*) AS cantidad_nominas 
                    FROM nomina_semanal 
                    GROUP BY cedula, YEAR(fecha), MONTH(fecha) 
                    HAVING cantidad_nominas < 2
                ) t ON n.cedula = t.cedula AND MONTH(n.fecha) = t.mes AND YEAR(n.fecha) = t.anio
                WHERE e.nomina_type = 'Semanal' 
                AND e.status = 1
                AND NOT EXISTS (
                    SELECT 1 
                    FROM nomina_semanal n_sub 
                    WHERE n_sub.cedula = e.cedula 
                      AND YEAR(n_sub.fecha_fin) = YEAR(CURDATE()) 
                      AND MONTH(n_sub.fecha_fin) = MONTH(CURDATE()) 
                      AND DAY(n_sub.fecha) IN (22)
                );
                """

                else:
                    print('eror situsabe')

                print('here done')
                    
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

                headers = ["Cedula de Empleado", "Nombre de Empleado", "Ubicacion Laboral", "Total Neto", "Descuentos"]
                self.model.setHorizontalHeaderLabels(headers)

                # Insertar los datos en la tabla 'nominas'
                insert_query = """
                INSERT INTO employee_prev (cedula, name, location, nomina_type) VALUES (%s, %s, %s, %s);
                """
                for nomina in rows:
                    print("Insertando los siguientes datos:", nomina[0], nomina[1], nomina[2], nomina[3])  # Depuración
                    cursor.execute(insert_query, (nomina[0], nomina[1], nomina[2], nomina[3]))

                # Confirmar la transacción
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
        try:
            connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='sc_db',
        charset='utf8'
    )
            cursor = connection.cursor()

            query = "SELECT * FROM nomina_semanal_prev"
            cursor.execute(query)
            nominas = cursor.fetchall()
            send_history = historial_view()
 
            for nomina in nominas:
                query = "INSERT INTO nomina_semanal(cedula, sueldo_base, prima_transporte, prima_hogar, prima_alimentacion, prima_hijo, prima_antiguedad, prima_profesion, asignaciones, deducciones_T,pf,ivss,faov,cuota_sindical,total_neto,fecha,type,fecha_fin,made_by, retributions, created) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, curdate())"
                cursor.execute(query, (nomina[0], nomina[1], nomina[2], nomina[3], nomina[4], nomina[5], nomina[6], nomina[7], nomina[8], nomina[9], nomina[10], nomina[11], nomina[12], nomina[13], nomina[14], nomina[15], nomina[16], nomina[17], nomina[18], nomina[19]))
                send_history.add_historial(conf.user,"Crear Nomina", nomina[0])
                connection.commit()
                print('done')
                #successfulWidget('Nominas Creadas Exitosamente')

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
        print('showing this')
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
            self.nominaInfo.open_window(cedula, 'S')

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
        query = 'truncate table nomina_semanal_prev;'
        cursor.execute(query)

        connection.commit()

        self.show_nominas()

        query = "SELECT e.cedula FROM employee_prev e WHERE e.nomina_type = 'Semanal';"
        cursor.execute(query)
        #self.vals()

        empleados= cursor.fetchall()
        print(empleados)
        for empleado in empleados:
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
             asignaciones = asignaciones_user + payment + conf.prima_hogar/4 + conf.prima_transporte/4 + conf.prima_alimentacion/4 + (conf.prima_hijo*float(hijos[0]))/4 + (conf.prima_profesion[profession]/100)*(payment) + (conf.prima_anti[min(str(service_years), '23')]/100)*(payment)
             print((conf.prima_anti[min(str(service_years), '23')]/100)*(payment), ' ', payment, ' ', cedula_user, ' ', service_years)
             ivss = ((payment)*12)/52*0.04*4
             ivss = round(ivss,2)
             faov = 0.01*asignaciones
             faov = round(faov,2)
             p_f = ((payment)*12)/52*0.005*4
             p_f = round(p_f,2)
             cuota_sindical = 0 

             current_date = datetime.now()

             if self.week == 1:
                  selected_date_start = current_date.replace(day=1).strftime('%d-%m-%Y')

                  last_day = calendar.monthrange(current_date.year, current_date.month)[1]

                  selected_date_end = current_date.replace(day=7).strftime('%d-%m-%Y') 

                  selected_date_start = datetime.strptime(selected_date_start, "%d-%m-%Y")

                  selected_date_end = datetime.strptime(selected_date_end, "%d-%m-%Y")


             elif self.week == 2: 
                  selected_date_start = current_date.replace(day=8).strftime('%d-%m-%Y')

                  last_day = calendar.monthrange(current_date.year, current_date.month)[1]

                  selected_date_end = current_date.replace(day=14).strftime('%d-%m-%Y') 

                  selected_date_start = datetime.strptime(selected_date_start, "%d-%m-%Y")

                  selected_date_end = datetime.strptime(selected_date_end, "%d-%m-%Y")


             elif self.week == 3: 

                  selected_date_start = current_date.replace(day=15).strftime('%d-%m-%Y')

                  last_day = calendar.monthrange(current_date.year, current_date.month)[1]

                  selected_date_end = current_date.replace(day=21).strftime('%d-%m-%Y') 

                  selected_date_start = datetime.strptime(selected_date_start, "%d-%m-%Y")

                  selected_date_end = datetime.strptime(selected_date_end, "%d-%m-%Y")
            
             elif self.week == 4:
                  selected_date_start = current_date.replace(day=22).strftime('%d-%m-%Y')

                  last_day = calendar.monthrange(current_date.year, current_date.month)[1]

                  selected_date_end = current_date.replace(day=28).strftime('%d-%m-%Y') 

                  selected_date_start = datetime.strptime(selected_date_start, "%d-%m-%Y")

                  selected_date_end = datetime.strptime(selected_date_end, "%d-%m-%Y")
            
             else:
                 print('SUPER ERROORRRR')
                                  

             #selected_date_start = selected_date_start.toString("yyyy-MM-dd")
             #selected_date_end = selected_date_end.toString("yyyy-MM-dd")
             
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
                                                   str(self.week),
                                                   round(conf.prima_transporte/4,2),
                                                   round(conf.prima_hogar/4,2),
                                                   round(conf.prima_alimentacion/4,2),
                                                   round(conf.prima_hijo*float(hijos[0])/4, 2),
                                                   round((conf.prima_anti[min(str(service_years), '23')]/100)*payment,2),
                                                   round((conf.prima_profesion[profession]/100)*payment,2),
                                                   asignaciones,
                                                   deducciones,
                                                   p_f,
                                                   ivss,
                                                   faov,
                                                   cuota_sindical,
                                                   neto,selected_date_start,
                                                   'Semanal',
                                                   selected_date_end,
                                                   asignaciones_user)

    def create_nomina_fnt(self, cedula, sueldo_base,n_semana, prima_transporte, prima_hogar, prima_alimentacion, prima_hijo, prima_antiguedad, prima_profesion, asignaciones, deducciones_T, pf,ivss,faov,cuota_sindical,total_neto,fecha,tipo,fecha_fin, asignaciones_user):

        print("Ejecutando create_nomina_fnt con los siguientes parámetros:")

        connection = pymysql.connect(
                host='localhost',
                user='root',
                password='root',
                database='sc_db',
                charset='utf8'
                )
        try:
            with connection.cursor() as cursor:

                query = "insert into nomina_semanal_prev(cedula, sueldo_base,n_semana, prima_transporte, prima_hogar, prima_alimentacion, prima_hijo, prima_antiguedad, prima_profesion, asignaciones, deducciones_T,pf,ivss,faov,cuota_sindical,total_neto,fecha,type,fecha_fin,made_by, retributions) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                cursor.execute(query, (cedula, sueldo_base,n_semana, prima_transporte, prima_hogar, prima_alimentacion, prima_hijo, prima_antiguedad, prima_profesion, asignaciones, deducciones_T, pf, ivss, faov, cuota_sindical, total_neto, fecha, tipo, fecha_fin, conf.user, asignaciones_user))
                connection.commit()

                self.show_nominas()
                #successfulWidget(self, message='Nominas Creadas Exitosamente')

        except pymysql.MySQLError as e:
            print(f"Error de conexión a la base de datos: {e}")

    def week_1(self):
        self.showMaximized()
        self.week = 1

    def week_2(self):
        self.showMaximized()
        self.week = 2

    def week_3(self):
        self.showMaximized()
        self.week = 3

    def week_4(self):
        self.showMaximized()
        self.week = 4
