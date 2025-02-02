from datetime import datetime
import pymysql
import conf
from PyQt5.QtWidgets import QMessageBox, QHeaderView, QWidget
from PyQt5.QtCore import QModelIndex, QSortFilterProxyModel, QTimer, Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from py_functions.successful_change_notification import successfulWidget
from ui_py.create_nominas_cestaticket import Ui_Form
from py_functions.edit_cestaticket import edit_info_cestaticket
from py_functions.historial import historial_view
from py_functions.pdf_create_cesta import generate_pdf
from py_functions.pdf_listado_nomina_cesta import generate_pdf_lista

class show_cesta_window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.historial = historial_view()
        self.model = QStandardItemModel()
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.model)
        self.tableView.setModel(self.proxy_model)
        self.frame_4.mousePressEvent = self.display_updated_data

        # Conectar señales
        self.tableView.doubleClicked.connect(self.clicked_row)
        self.prev_create.clicked.connect(self.create_nomina)
        self.confirm.clicked.connect(self.confirm_all)
        self.prev_pdf.clicked.connect(generate_pdf)
        self.listado_nominas.clicked.connect(generate_pdf_lista)

    def open_cesta(self):
        self.showMaximized()

    def adjust_table_settings(self):
        """Configurar la tabla para el comportamiento deseado."""
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
            cedula_index = source_index.siblingAtColumn(1)
            cedula = self.model.itemFromIndex(cedula_index).text()
            print(cedula, '!!!')
            self.nominaInfo = edit_info_cestaticket()
            self.nominaInfo.open_window(cedula)

    def fetch_data(self, query, params=()):
        """Ejecuta consultas y devuelve los resultados."""
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='sc_db',
            charset='utf8'
        )
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()
        except pymysql.MySQLError as e:
            print(f"Error en la base de datos: {e}")
            return []
        finally:
            connection.close()

    def execute_query(self, query, params=()):
        """Ejecuta consultas sin devolver resultados."""
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='sc_db',
            charset='utf8'
        )
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                connection.commit()
        except pymysql.MySQLError as e:
            print(f"Error en la base de datos: {e}")
        finally:
            connection.close()
 
    def create_nomina(self):
        self.execute_query("TRUNCATE TABLE nomina_cestaticket_prev;")
      
        empleados_query = """
        SELECT CONCAT(e.name, ' ', e.lastname) AS fullname, e.cedula 
        FROM employee e
        WHERE e.status = 1
          AND NOT EXISTS (
          SELECT 1 
          FROM nomina_cestaticket n_sub
          WHERE n_sub.cedula = e.cedula
            AND YEAR(n_sub.fecha) = YEAR(CURDATE())
            AND MONTH(n_sub.fecha) = MONTH(CURDATE())
          );
        """
        empleados = self.fetch_data(empleados_query)
      
        insert_query = """
            INSERT INTO nomina_cestaticket_prev (nombre, cedula, total_neto, descuentos, fecha, type) 
            VALUES (%s, %s, %s, %s, CURDATE(), "Cestaticet");
        """
        for nombre, cedula in empleados:
            total_neto = conf.cesta_ticket
            descuentos = 0
            self.cedula = cedula
            self.execute_query(insert_query, (nombre, cedula, total_neto, descuentos))
      
        print(f"{len(empleados)} empleados procesados.")
        self.load_nominas()
      
 
    def load_nominas(self):
        query = "SELECT nombre, cedula, total_neto, descuentos FROM nomina_cestaticket_prev;"    
        query_ubi = "SELECT job_location FROM employee WHERE cedula = %s;"
      
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='sc_db',
            charset='utf8'
        )
      
        try:
            rows = []  # Lista para almacenar las filas completas con la ubicación
            with connection.cursor() as cursor:
                cursor.execute(query)
                results = cursor.fetchall()  # Resultados de la consulta principal
      
                for row in results:
                    nombre, cedula, total_neto, descuentos = row
                    
                    # Obtener la ubicación laboral basada en la cédula
                    cursor.execute(query_ubi, (cedula,))
                    location_result = cursor.fetchone()
                    location = location_result[0] if location_result else "N/A"
      
                    # Agregar la fila completa con la ubicación a la lista de filas
                    rows.append((nombre, cedula, location, total_neto, descuentos))
      
        except pymysql.MySQLError as e:
            print(f"Error en la base de datos: {e}")
        finally:
            connection.close()
      
        # Encabezados de la tabla
        headers = ["Nombre", "Cédula", "Ubicación Laboral", "Total Neto", "Descuentos"]
      
        # Cargar los datos en la tabla
        self.load_table_data(headers, rows)

    def load_table_data(self, headers, rows):
        """Carga datos en el modelo de la tabla."""
        print("Modelo antes de actualizar:", self.tableView.model())
        
        self.model.clear()  # Limpiar datos antiguos en el modelo fuente
        self.model.setHorizontalHeaderLabels(headers)  # Establecer encabezados
    
        # Asegúrate de que el número de filas sea suficiente
        self.model.setRowCount(len(rows))  # Establecer el número de filas según los datos
    
        for row_idx, row in enumerate(rows):
            print(f"Fila {row_idx}: {row}")  # Imprimir la fila
            for col_idx, value in enumerate(row):
                print(f"Columna {col_idx}: {value}")  # Imprimir la columna
                item = QStandardItem(str(value))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(row_idx, col_idx, item)
    
        self.tableView.viewport().update()  # Forzar la actualización de la vista
        self.adjust_table_settings()

        
        print("Modelo después de actualizar:", self.tableView.model())
        print("updated")


    def display_updated_data(self, event):
        query = "SELECT nombre, cedula, total_neto, descuentos FROM nomina_cestaticket_prev;"
        query_ubi = "SELECT job_location FROM employee WHERE cedula = %s;"
    
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='sc_db',
            charset='utf8'
        )
    
        try:
            rows = []  # Lista para almacenar las filas completas con la ubicación
            with connection.cursor() as cursor:
                cursor.execute(query)
                results = cursor.fetchall()  # Resultados de la consulta principal
    
                for row in results:
                    nombre, cedula, total_neto, descuentos = row
                    
                    # Obtener la ubicación laboral basada en la cédula
                    cursor.execute(query_ubi, (cedula,))
                    location_result = cursor.fetchone()
                    location = location_result[0] if location_result else "N/A"
    
                    # Agregar la fila completa con la ubicación a la lista de filas
                    rows.append((nombre, cedula, location, total_neto, descuentos))
    
        except pymysql.MySQLError as e:
            print(f"Error en la base de datos: {e}")
        finally:
            connection.close()
    
        if rows:
            print(f"Datos obtenidos: {rows}")
    
            headers = ["Nombre", "Cédula", "Ubicación Laboral", "Total Neto", "Descuentos"]
    
            # Ocultar la ventana antes de mostrar los datos
            self.repaint()  # Asegúrate de que esto se llame en el hilo principal
    
            # Usar QTimer para forzar un breve retraso antes de mostrar la ventana
            QTimer.singleShot(50, lambda: self.load_table_data(headers, rows))  # 50ms de retraso
        else:
            print("No hay datos para mostrar en la tabla.")

    

    def confirm_all(self):
        try:
            # Conexión a la base de datos
            connection = pymysql.connect(
                host='localhost',
                user='root',
                password='root',
                database='sc_db',
                charset='utf8'
            )
            
            cursor = connection.cursor()
            
            # Copiar datos de `nomina_cestaticket_prev` a `nomina_cestaticket`
            query = """
            INSERT INTO nomina_cestaticket (cedula, nombre, total_neto, descuentos, fecha)
            SELECT cedula, nombre, total_neto, descuentos, fecha 
            FROM nomina_cestaticket_prev;
            """
            cursor.execute(query)
            connection.commit()  # Asegurar los cambios
            print("Datos copiados exitosamente de nomina_cestaticket_prev a nomina_cestaticket.")
            
            # Recuperar las cédulas afectadas para el historial
            query_affected = "SELECT cedula FROM nomina_cestaticket_prev;"
            cursor.execute(query_affected)
            affected_rows = cursor.fetchall()
    
            # Agregar entradas al historial
            for row in affected_rows:
                cedula = row[0]
                self.historial.add_historial(cedula, "Crear Nomina Cestaticket", conf.user)
            
        except pymysql.MySQLError as e:
            # Manejo de errores de la base de datos
            print(f"Error en la base de datos: {e}")
        finally:
            # Cierre seguro de la conexión
            if connection:
                connection.close()
                if len(affected_rows) > 1:
                    successfulWidget(self, message="Nominas creadas exitosamente")
                else:
                    QMessageBox.warning(self, "Datos Insuficientes", "La tabla de nominas no tiene nominas creadas.")

    
                
