from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtCore import QModelIndex, Qt, QRegExp, QSortFilterProxyModel
from PyQt5.QtWidgets import QWidget, QHeaderView, QInputDialog
import pymysql
from datetime import datetime

from ui_py.historial import Ui_Form 

class historial_view(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        


        # Inicializa el modelo para la vista de tabla
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Empleado", "Administrador", "Acción", "Fecha", "Hora"])
        self.tableView.setModel(self.model)  # Conecta el modelo a un QTableView definido en tu UI
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.model)
        self.tableView.setModel(self.proxy_model)
        self.ready = False
        self.load_data()
        self.btn_search.currentIndexChanged.connect(self.apply_filter)

    def add_historial(self, cedula, action, user_e):
        try:
            # Conexión con `with` para garantizar el cierre
            with pymysql.connect(
                    host='localhost',
                    user='user_nomina',
                    password='12345678',
                    database='sc_db',
                    charset='utf8'
                    ) as connection:
                fecha_actual = datetime.now().strftime('%Y-%m-%d')
                hora_actual = datetime.now().strftime('%H:%M:%S')  # Corregido el formato de hora
                with connection.cursor() as cursor:

                            query = """
                                        INSERT INTO historial (admin, empleado, action, fecha, hora) 
                                        VALUES (%s, %s, %s, %s, %s);
                                    """

                            cursor.execute(query, (user_e, cedula, action, fecha_actual, hora_actual))
                            connection.commit()  # Guarda los cambios
        except pymysql.MySQLError as e:
            print(f"Error al interactuar con la base de datos: {e}")



    def load_data(self):
        try:
            with pymysql.connect(
                    host='localhost',
                    user='user_nomina',
                    password='12345678',
                    database='sc_db',
                    charset='utf8'
                    ) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT admin, empleado, action, fecha, hora FROM historial"
                    cursor.execute(query)
                    rows = cursor.fetchall()
    
                # Limpia los datos actuales del modelo
                self.model.removeRows(0, self.model.rowCount())
    
                # Población de la tabla
                for row_idx, row in enumerate(rows):
                    for col_idx, value in enumerate(row):
                        if col_idx == 0:
                            # Crea un nuevo cursor para la segunda consulta
                            with connection.cursor() as cursor2:
                                cursor2.execute("SELECT CONCAT(name, ' ', lastname) FROM employee WHERE cedula = %s", (value,))
                                result = cursor2.fetchone()
                                value = result[0] if result else "Desconocido"  # Si no hay resultado, usa "Desconocido"
                        if col_idx == 1:
                            # Crea un nuevo cursor para la segunda consulta
                            with connection.cursor() as cursor2:
                                cursor2.execute("SELECT CONCAT(name, ' ', lastname) FROM employee WHERE cedula = %s", (value,))
                                result = cursor2.fetchone()
                                value = result[0] if result else "Desconocido"  # Si no hay resultado, usa "Desconocido"
                        item = QStandardItem(str(value))
                        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # No editable
                        self.model.setItem(row_idx, col_idx, item)
    
                self.adjust_table_settings()
    
        except pymysql.MySQLError as e:
            print(f"Error de conexión a la base de datos: {e}")

    def apply_filter(self):
        selected_index = self.btn_search.currentIndex()

        if selected_index == 0:  # Restablecer la tabla
            self.proxy_model.setFilterRegExp(QRegExp())  # Quita cualquier filtro
            self.proxy_model.setFilterKeyColumn(-1)  # No filtrar por ninguna columna
            self.proxy_model.sort(-1)  # Quita la ordenación

        elif selected_index == 0:
            self.proxy_model.setSortCaseSensitivity(Qt.CaseInsensitive)
            self.proxy_model.sort(0, Qt.AscendingOrder)

        elif selected_index == 2:
            self.proxy_model.setSortCaseSensitivity(Qt.CaseInsensitive)
            self.proxy_model.sort(0, Qt.DescendingOrder)

        elif selected_index == 3:
            self.proxy_model.sort(2, Qt.DescendingOrder)

        elif selected_index == 4:
            self.proxy_model.sort(2, Qt.AscendingOrder)

        elif selected_index == 5:  # Búsqueda por Cédula
            nombre, ok = QInputDialog.getText(self, "Buscar por Nombre", "Ingrese el nombre:")
            if ok and nombre:
                regex = QRegExp(nombre, Qt.CaseInsensitive) #Búsqueda insensible a mayúsculas
                self.proxy_model.setFilterKeyColumn(0)
                self.proxy_model.setFilterRegExp(regex)

    def adjust_table_settings(self):
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setSelectionBehavior(self.tableView.SelectRows)
        self.tableView.setStyleSheet("""
            QTableView::item:selected {
                background-color: #4CAF50;
                color: white;
            }
        """)
