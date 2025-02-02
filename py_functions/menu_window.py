import pymysql
from PyQt5.QtCore import QModelIndex, QRegExp, Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QHeaderView, QInputDialog, QWidget, QMessageBox
from ui_py.menu import Ui_Form
from py_functions.createUser_window import createUserWindow
from py_functions.createNomina_window import createNominaWindow
from py_functions.configuration_window import configurationWindow
from py_functions.info_empleado import info_empleado_window
from py_functions.create_secretario import create_secretario_window 
from py_functions.delete_secretario import delete_secretario_window
from py_functions.edit_secretario import edit_secretario_window
from py_functions.info_nomina import info_nomina_window
from py_functions.create_nominas_quincena import createNominasQuincenal
from py_functions.create_nominas_mensual import createNominasMensual
from py_functions.historial import historial_view
from py_functions.create_cesta import show_cesta_window

from py_functions.create_nominas_semanal import createNominasSemanal

class MainApp(QWidget, Ui_Form):
    def __init__(self):
        super(MainApp, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Gestionador")
        self.cedula = 0
        self.info_empleado = info_empleado_window() 
        self.model = QStandardItemModel()  # Modelo principal
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.model)
        self.tableView.setModel(self.proxy_model)  # Asignar proxy al QTableView 
        self.is_in_nomina = 0
        self.is_cesta = False
        
        self.load_data()
        
        self.btn_search_nomina.currentIndexChanged.connect(self.apply_filter)  # Conectar ComboBox
        self.tableView.doubleClicked.connect(self.clicked_row)
        
        #EFECTO 
        self.nomina_quincenal_tab.clicked.connect(self.current_tab)
        self.personal_tab.clicked.connect(self.current_tab)
        self.nomina_mensual_tab.clicked.connect(self.current_tab)
        self.all_nominas.clicked.connect(self.current_tab)
        self.cestatickets_tab.clicked.connect(self.current_tab)
        self.nomina_semanal_tab.clicked.connect(self.current_tab)

        #kkk
        self.btn_add_nomina.clicked.connect(self.open_create_employee)
        self.crear_empleado_gestion.clicked.connect(self.go_to_create_empleados_gestion)
        self.eliminar_empleado_gestion.clicked.connect(self.go_to_delete_empleados_gestion)
        self.editar_empleado_gestion.clicked.connect(self.go_to_edit_empleados_gestion)

        #self.create_cesta_btn.clicked.connect(self.show_cesta_window)

        #Config Button
        self.engranaje.mousePressEvent = self.go_to_config
        self.tiempo.mousePressEvent = self.go_to_historial
        
        #Funcionalidades de Tabs
        self.all_nominas.clicked.connect(self.show_all_nominas)
        self.personal_tab.clicked.connect(self.load_data)
        self.nomina_quincenal_tab.clicked.connect(self.show_nominas_quincena)
        self.nomina_mensual_tab.clicked.connect(self.show_nominas_mensual)
        self.cestatickets_tab.clicked.connect(self.show_cesta)
        self.nomina_semanal_tab.clicked.connect(self.show_nominas_semanal)

    def go_to_config(self, event):
        self.config_window = configurationWindow()
        self.config_window.showMaximized()

    def go_to_historial(self, event):
        self.historial_window = historial_view()
        self.historial_window.showMaximized()

    def go_to_create_empleados_gestion(self):
        self.empleados_gestion = create_secretario_window()
        self.empleados_gestion.showMaximized()

    def go_to_delete_empleados_gestion(self):
        self.empleados_gestion = delete_secretario_window()
        self.empleados_gestion.showMaximized()

    def go_to_edit_empleados_gestion(self):
        self.empleados_gestion = edit_secretario_window()
        self.empleados_gestion.showMaximized()

    def current_tab(self):
        self.personal_tab.setStyleSheet("min-width:130px;min-height:40px;padding:0 20px;border-radius: 4px;border: 1px solid #000;")
        self.all_nominas.setStyleSheet("min-width:130px;min-height:40px;padding:0 20px;border-radius: 4px;border: 1px solid #000;")
        self.cestatickets_tab.setStyleSheet("min-width:130px;min-height:40px;padding:0 20px;border-radius: 4px;border: 1px solid #000;")
        self.nomina_quincenal_tab.setStyleSheet("min-width:130px;min-height:40px;padding:0 20px;border-radius: 4px;border: 1px solid #000;")
        self.nomina_mensual_tab.setStyleSheet("min-width:130px;min-height:40px;padding:0 20px;border-radius: 4px;border: 1px solid #000;")
        self.nomina_semanal_tab.setStyleSheet("min-width:130px;min-height:40px;padding:0 20px;border-radius: 4px;border: 1px solid #000;")
        
        sender = self.sender()
        sender.setStyleSheet("min-width:130px;min-height:40px; background-color: #54BCBD;color:#fff;padding:0 20px;font-weight: bold;")
    
    def open_create_nomina(self):
        self.creater_nomina = createNominaWindow()
        self.creater_nomina.showMaximized()

    def open_create_employee(self):
        self.createEmployeeWindow = createUserWindow()
        self.createEmployeeWindow.showMaximized()

    def clicked_row(self, index: QModelIndex):
        
        if self.is_in_nomina and self.is_cesta == False:
            source_index = self.proxy_model.mapToSource(index)
            cedula_index = source_index.siblingAtColumn(0)
            cedula = self.model.itemFromIndex(cedula_index).text()
            self.nominaInfo = info_nomina_window()
            self.nominaInfo.open_window(cedula)

        elif self.is_cesta == True:
            print('cesta act')
            
        else:
            source_index = self.proxy_model.mapToSource(index)
            cedula_index = source_index.siblingAtColumn(2)
            cedula = self.model.itemFromIndex(cedula_index).text()
            self.info_empleado.open_window(cedula)

    def load_data(self):
        self.is_in_nomina = 0
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='sc_db',
            charset='utf8'
        )
        try:
            with connection.cursor() as cursor:
                query = "SELECT name, lastname, cedula, job, job_location, payment, status FROM employee"
                cursor.execute(query)
                rows = cursor.fetchall()
                self.model.clear()

                headers = ["Nombre", "Apellido", "Cédula", "Trabajo", "Ubicación", "Pago", "Estado"]
                self.model.setHorizontalHeaderLabels(headers)

                for row_idx, row in enumerate(rows):
                    for col_idx, value in enumerate(row):
                        if col_idx == 6:  # Columna 'status'
                            display_value = "Activo" if value else "Inactivo"
                            item = QStandardItem(display_value)

                        elif col_idx == 2:  # Columna "Cédula"
                            try:
                                item = QStandardItem(str(int(value)))
                                item.setData(int(value), Qt.EditRole)
                            except (ValueError, TypeError):
                                item = QStandardItem(str(value))

                        elif col_idx == 4:  # Columna "Ubicación"
                            item = QStandardItem(str(value))
                            item.setData(str(value), Qt.ToolTipRole)  

                        elif col_idx == 0:  # Columna "Nombre"
                            item = QStandardItem(str(value))
                            item.setData(str(value), Qt.ToolTipRole)  
                        
                        elif col_idx == 1:  # Columna Apellido
                            item = QStandardItem(str(value))
                            item.setData(str(value), Qt.ToolTipRole)
                        
                        elif col_idx == 3:  # Columna "Profesion"
                            item = QStandardItem(str(value))
                            item.setData(str(value), Qt.ToolTipRole)  
                        
                        else:
                            item = QStandardItem(str(value))
 
                        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # No editable
                        self.model.setItem(row_idx, col_idx, item)
  
                self.proxy_model = QSortFilterProxyModel(self)
                self.proxy_model.setSourceModel(self.model)
                self.tableView.setModel(self.proxy_model)

            self.adjust_table_settings()

        except pymysql.MySQLError as e:
            print(f"Error al conectarse a la base de datos: {e}")

        if self.btn_add_nomina.text() != 'Añadir Nuevo Empleado':
            self.btn_add_nomina.setText("Crear Nuevo Empleado")
            self.btn_add_nomina.setObjectName("btn_all_create_nomina")
            self.btn_add_nomina.clicked.disconnect()
            self.btn_add_nomina.clicked.connect(self.open_create_employee)

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

    def apply_filter(self):
        selected_index = self.btn_search_nomina.currentIndex()
        if selected_index == 0:  # Restablecer la tabla
            self.proxy_model.setFilterRegExp(QRegExp())  # Quita cualquier filtro
            self.proxy_model.setFilterKeyColumn(-1)  # No filtrar por ninguna columna
            self.proxy_model.sort(-1)  # Quita la ordenación
        elif selected_index == 1:
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
            cedula, ok = QInputDialog.getText(self, "Buscar por Cédula", "Ingrese la cédula:")
            if ok and cedula:
                regex = QRegExp(cedula, Qt.CaseInsensitive) #Búsqueda insensible a mayúsculas
                self.proxy_model.setFilterKeyColumn(2)
                self.proxy_model.setFilterRegExp(regex)

        elif selected_index == 6:  # Búsqueda por Nombre
            nombre, ok = QInputDialog.getText(self, "Buscar por Nombre", "Ingrese el nombre:")
            if ok and nombre:
                regex = QRegExp(nombre, Qt.CaseInsensitive) #Búsqueda insensible a mayúsculas
                self.proxy_model.setFilterKeyColumn(0)
                self.proxy_model.setFilterRegExp(regex)

        elif selected_index == 7:  # Búsqueda por Apellido
            apellido, ok = QInputDialog.getText(self, "Buscar por Apellido", "Ingrese el apellido:")
            if ok and apellido:
                regex = QRegExp(apellido, Qt.CaseInsensitive) #Búsqueda insensible a mayúsculas
                self.proxy_model.setFilterKeyColumn(1)
                self.proxy_model.setFilterRegExp(regex)

            # Imprimir las cédulas ordenadas (esto se mantiene para depuración)
            for row in range(self.proxy_model.rowCount()):
                index = self.proxy_model.index(row, 2)  # Columna "Cédula"
                print("Cédula ordenada:", self.proxy_model.data(index))

    def open_create_nominas_semanal(self):
        self.preguntar_semana()

    def show_all_nominas(self):
        self.is_in_nomina = 1
        connection = pymysql.connect(
                host='localhost',
                user='root',
                password='root',
                database='sc_db',
                charset='utf8'
                )
        try:
            with connection.cursor() as cursor:
                query = """
                    SELECT cedula, asignaciones, deducciones_T, total_neto, fecha, fecha_fin, type FROM nominas_prev
                    UNION ALL
                    SELECT cedula, asignaciones, deducciones_T, total_neto, fecha, fecha_fin, type FROM nomina_semanal
                """
                cursor.execute(query)
                rows = cursor.fetchall()
                self.model.clear()
                headers = ["Cedula", "Asignaciones", "Deducciones", "Total", "Fecha_Inicio", "Fecha_Fin", "Tipo"]
                self.model.setHorizontalHeaderLabels(headers)

                for row_idx, row in enumerate(rows):
                    for col_idx, value in enumerate(row):    
                        item = QStandardItem(str(value))
                        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                        self.model.setItem(row_idx, col_idx, item)

        except pymysql.MySQLError as e:
            print(f"Error de conexión a la base de datos: {e}")

        #self.btn_add_nomina.setText("Crear Nomina")
        #self.btn_add_nomina.setObjectName("btn_all_create_nomina")
        #self.btn_add_nomina.clicked.disconnect()
        #self.btn_add_nomina.clicked.connect(self.open_create_nomina)

    def show_nominas_semanal(self):
        self.is_cesta = False
        self.is_in_nomina = 1
        connection = pymysql.connect(
                host='localhost',
                user='root',
                password='root',
                database='sc_db',
                charset='utf8'
                )
        try:
            with connection.cursor() as cursor:
                query = "SELECT cedula,asignaciones,deducciones_T,total_neto,fecha,fecha_fin,type FROM nomina_semanal"
                cursor.execute(query)
                rows = cursor.fetchall()
                self.model.clear()
                headers = ["Cedula", "Asignaciones", "Deducciones", "Total", "Fecha_Inicio", "Fecha_Fin", "Tipo"]
                self.model.setHorizontalHeaderLabels(headers)

                for row_idx, row in enumerate(rows):
                    for col_idx, value in enumerate(row):    
                        item = QStandardItem(str(value))
                        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # No editable
                        self.model.setItem(row_idx, col_idx, item)

        except pymysql.MySQLError as e:
            print(f"Error de conexión a la base de datos: {e}")

        self.btn_add_nomina.setText("Crear Nominas Semanal")
        self.btn_add_nomina.setObjectName("Create_nomina_btn_2")
        try:
            self.btn_add_nomina.clicked.disconnect()
            self.btn_add_nomina.clicked.connect(self.open_create_nominas_semanal)

        except TypeError:
            print("No existen conexiones previas para la señal 'clicked'.")

    def show_nominas_quincena(self):
        self.is_cesta = False
        self.is_in_nomina = 1
        connection = pymysql.connect(
                host='localhost',
                user='root',
                password='root',
                database='sc_db',
                charset='utf8'
                )
        try:
            with connection.cursor() as cursor:
                query = "SELECT cedula,asignaciones,deducciones_T,total_neto,fecha,fecha_fin,type FROM nominas_prev where type='Quincenal'"
                cursor.execute(query)
                rows = cursor.fetchall()
                self.model.clear()
                headers = ["Cedula", "Asignaciones", "Deducciones", "Total", "Fecha_Inicio", "Fecha_Fin", "Tipo"]
                self.model.setHorizontalHeaderLabels(headers)

                for row_idx, row in enumerate(rows):
                    for col_idx, value in enumerate(row):    
                        item = QStandardItem(str(value))
                        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # No editable
                        self.model.setItem(row_idx, col_idx, item)

        except pymysql.MySQLError as e:
            print(f"Error de conexión a la base de datos: {e}")

        self.btn_add_nomina.setText("Crear Nominas Quincenales")
        self.btn_add_nomina.setObjectName("Create_nomina_btn")
        try:
            self.btn_add_nomina.clicked.disconnect()
        except TypeError:
            print("No existen conexiones previas para la señal 'clicked'.")
        self.btn_add_nomina.clicked.connect(self.open_create_nominas_quincenal)

    def show_cesta(self):
        self.is_in_nomina = 1
        connection = pymysql.connect(
                host='localhost',
                user='root',
                password='root',
                database='sc_db',
                charset='utf8'
                )
        try:
            with connection.cursor() as cursor:
                query = "SELECT nombre,cedula,total_neto,descuentos, fecha from nomina_cestaticket"
                cursor.execute(query)
                rows = cursor.fetchall()
                self.model.clear()
                headers = ["Nombre", "Cedula", "Total", "Descuento", "Fecha"]
                self.model.setHorizontalHeaderLabels(headers)

                for row_idx, row in enumerate(rows):
                    for col_idx, value in enumerate(row):    
                        item = QStandardItem(str(value))
                        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # No editable
                        self.model.setItem(row_idx, col_idx, item)


        except pymysql.MySQLError as e:
            print(f"Error de conexión a la base de datos: {e}")

        self.is_cesta = True
        self.btn_add_nomina.setText("Crear Nominas Cestaticket")
        self.btn_add_nomina.setObjectName("create_cesta_btn")
        self.btn_add_nomina.clicked.disconnect()
        self.cesta_window = show_cesta_window()
        self.btn_add_nomina.clicked.connect(self.cesta_window.open_cesta)

    def open_create_nominas_quincenal(self):
        self.preguntar_quincena()

    def preguntar_semana(self):
        while True:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Seleccionar Semana")
            msg_box.setText("Seleccione de que semana desea crear las nominas")
            
            msg_box.setWindowFlag(Qt.WindowCloseButtonHint, False)
            msg_box.setWindowFlag(Qt.WindowContextHelpButtonHint, False)  

            btn_cancelar = msg_box.addButton("Cancelar", QMessageBox.DestructiveRole)
            btn_cuarta = msg_box.addButton("Cuarta", QMessageBox.RejectRole)
            btn_tercera = msg_box.addButton("Tercera", QMessageBox.RejectRole)
            btn_segunda = msg_box.addButton("Segunda", QMessageBox.RejectRole)
            btn_primera = msg_box.addButton("Primera", QMessageBox.AcceptRole)
            
            msg_box.exec_()

            clicked_button = msg_box.clickedButton()
            if clicked_button is None or clicked_button == btn_cancelar:
                print("Operación cancelada")
                break
            
            # Respuesta del usuario
            elif msg_box.clickedButton() == btn_primera:
                print("Seleccionaste: Primera semana")
                self.nominas_semanal = createNominasSemanal()
                self.nominas_semanal.week_1()
                break

            elif msg_box.clickedButton() == btn_segunda:
                self.nominas_semanal = createNominasSemanal()
                self.nominas_semanal.week_2()
                print("Seleccionaste: Segunda semana")
                break

            elif msg_box.clickedButton() == btn_tercera:
                print("Seleccionaste: Tercera Semana")
                self.nominas_semanal = createNominasSemanal()
                self.nominas_semanal.week_3()
                break

            elif msg_box.clickedButton() == btn_cuarta:
                self.nominas_semanal = createNominasSemanal()
                self.nominas_semanal.week_4()
                print("Seleccionaste: cuarta semana")
                break

    def preguntar_quincena(self):
        while True:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Seleccionar Quincena")
            msg_box.setText("¿Es la primera quincena o la segunda?")
            
            msg_box.setWindowFlag(Qt.WindowCloseButtonHint, False)
            msg_box.setWindowFlag(Qt.WindowContextHelpButtonHint, False)  

            btn_primera = msg_box.addButton("Primera", QMessageBox.AcceptRole)
            btn_segunda = msg_box.addButton("Segunda", QMessageBox.RejectRole)
            btn_cancelar = msg_box.addButton("Cancelar", QMessageBox.DestructiveRole)
            
            msg_box.exec_()

            clicked_button = msg_box.clickedButton()
            if clicked_button is None or clicked_button == btn_cancelar:
                print("Operación cancelada")
                break
            
            # Respuesta del usuario
            elif msg_box.clickedButton() == btn_primera:
                print("Seleccionaste: Primera quincena")
                self.nominas_quincenal = createNominasQuincenal()
                self.nominas_quincenal.showMaximized()
                break

            elif msg_box.clickedButton() == btn_segunda:
                self.nominas_quincenal = createNominasQuincenal()
                self.nominas_quincenal.second_half()
                print("Seleccionaste: Segunda quincena")
                break

    def open_create_nominas_mensual(self):
        self.nominas_mensual = createNominasMensual()
        self.nominas_mensual.showMaximized()

    def show_nominas_mensual(self):
        self.is_cesta = False
        self.is_in_nomina = 1
        connection = pymysql.connect(
                host='localhost',
                user='root',
                password='root',
                database='sc_db',
                charset='utf8'
                )
        try:
            with connection.cursor() as cursor:
                query = "SELECT cedula,asignaciones,deducciones_T,total_neto,fecha,fecha_fin,type FROM nominas_prev where type='Mensual'"
                cursor.execute(query)
                rows = cursor.fetchall()
                self.model.clear()
                headers = ["Cedula", "Asignaciones", "Deducciones", "Total", "Fecha_Inicio", "Fecha_Fin", "Tipo"]
                self.model.setHorizontalHeaderLabels(headers)

                for row_idx, row in enumerate(rows):
                    for col_idx, value in enumerate(row):    
                        item = QStandardItem(str(value))
                        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # No editable
                        self.model.setItem(row_idx, col_idx, item)

        except pymysql.MySQLError as e:
            print(f"Error de conexión a la base de datos: {e}")
        
        self.btn_add_nomina.setText("Crear Nominas Mensuales")
        self.btn_add_nomina.setObjectName("btn_create_nomina_mensual")
        self.btn_add_nomina.clicked.disconnect()
        self.btn_add_nomina.clicked.connect(self.open_create_nominas_mensual)

    def startType(self, cedula):
        connection = pymysql.connect(
                host='localhost',
                user='root',
                password='root',
                database='sc_db',
                charset='utf8'
                )
        try:
            with connection.cursor() as cursor:
                query = "SELECT type FROM user where cedula = %s"
                cursor.execute(query, cedula)
                theType = cursor.fetchone()
                if theType:
                    if str(theType[0]).strip() == "Normal":
                        print('normal: ',str(theType[0]).strip())
                        self.eliminar_empleado_gestion.hide()
                        self.crear_empleado_gestion.hide()
                        self.editar_empleado_gestion.hide()
                    elif str(theType[0]).strip() == "Privilegiado":
                        print('privi: ',str(theType[0]).strip())
                        self.eliminar_empleado_gestion.show()
                        self.crear_empleado_gestion.show()
                        self.editar_empleado_gestion.show()
                    else:
                        print('paso algo raro', str(theType[0]).strip())
                    
                else:
                    print("El tipo no es reconocido.")

        except pymysql.MySQLError as e:
            print(f"Error de conexión a la base de datos: {e}")

    def load_type(self, cedula):
        self.cedula = cedula
        print('cedula = ', self.cedula)
        self.startType(cedula)
        self.showMaximized()

        
