from PyQt5.QtWidgets import QWidget, QCalendarWidget
from PyQt5.QtGui import QBrush, QColor
from ui_py.create_nomina import Ui_Form
from PyQt5.QtCore import QDate
import conf
from py_functions.successful_change_notification import successfulWidget
import pymysql

class createNominaWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Crear Nomina")
        self.calculate_btn.clicked.connect(self.calculatenomina)
        self.calendarWidget_2.clicked.connect(self.on_calendar_clicked)
        self.create_nomina_btn.clicked.connect(self.creatingNomina)

    def calculatenomina(self):
        cedula_user = self.cedula_input.text()
        asignaciones_user = self.retribuciones_input.text()
        asignaciones_user = asignaciones_user.strip()
        asignaciones_user = 0 if asignaciones_user == '' else float(asignaciones_user)
        print(asignaciones_user)
        connection = pymysql.connect(
                host='localhost',
                user='user_nomina',
                password='12345678',   
                database='sc_db',
                charset='utf8'
                )
        try:
            with connection.cursor() as cursor:
                query = "SELECT payment from employee where cedula = %s "
                cursor.execute(query, cedula_user)
                payment = cursor.fetchone()

                if payment is not None:
                    payment = payment[0]

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

                    #radio es quince 
                    if self.radioButton.isChecked():
                        payment = payment / 2
                        asignaciones = asignaciones_user + payment + conf.prima_hogar/2 + conf.prima_transporte/2 + conf.prima_alimentacion/2 + conf.prima_hijo*float(hijos[0]) + (conf.prima_profesion[profession]/100)*(payment) + (conf.prima_anti[service_years]/100)*(payment)

                        ivss = ((payment)*12)/52*0.04*4
                        ivss = round(ivss,2)
                        faov = 0.01*asignaciones
                        faov = round(faov,2)
                        p_f = ((payment)*12)/52*0.005*4
                        p_f = round(p_f,2)
                        cuota_sindical = (payment)*0.01

                        selected_date_start = self.calendarWidget_2.selectedDate()  # Obtiene la fecha seleccionada
                        selected_date_end = self.calendarWidget.selectedDate()  # Obtiene la fecha seleccionada

                        if self.checkBox.isChecked():
                            deducciones = ivss + faov + p_f + cuota_sindical
                            deducciones = round(deducciones,2)
                            neto = asignaciones - deducciones
                            neto = round(neto,2)

                            self.prima_transporte.setText(f'{conf.prima_transporte/2}')
                            self.prima_hogar.setText(f'{conf.prima_hogar/2}')
                            self.prima_alimentacion.setText(f'{conf.prima_alimentacion/2}')
                            self.sueldo_base.setText(f'Sueldo base: {payment/2}')

                            self.prima_hijo.setText(f'{conf.prima_hijo*float(hijos[0]) }')
                            self.prima_antiguedad.setText(f'{(conf.prima_anti[service_years]/100)*(payment/2)}')
                            self.prima_profesion.setText(f'{(conf.prima_profesion[profession]/100)*(payment/2)}')
                            self.asignaciones.setText(f'Asignaciones: {asignaciones}')

                            self.pf_d.setText(f'{p_f}')
                            self.ivss_d.setText(f'{ivss}')
                            self.label_13.setText(f'{faov}')
                            self.cuota_sindical_d.setText(f'{cuota_sindical}')
                            self.deducciones_total.setText(f'Total deducciones: {deducciones}')
                            self.pago_neto.setText(f'Neto a Pagar: {neto}')
                            
                                             
                        else:
                            deducciones = ivss + faov + p_f
                            deducciones = round(deducciones,2)

                            neto = asignaciones - deducciones
                            neto = round(neto,2)

                            self.prima_transporte.setText(f'{conf.prima_transporte/2}')
                            self.prima_hogar.setText(f'{conf.prima_hogar/2}')
                            self.prima_alimentacion.setText(f'{conf.prima_alimentacion/2}')
                            self.sueldo_base.setText(f'Sueldo base: {payment/2}')

                            self.prima_hijo.setText(f'{conf.prima_hijo*float(hijos[0]) }')
                            self.prima_antiguedad.setText(f'{(conf.prima_anti[service_years]/100)*(payment/2)}')
                            self.prima_profesion.setText(f'{(conf.prima_profesion[profession]/100)*(payment/2)}')
                            self.asignaciones.setText(f'Asignaciones: {asignaciones}')

                            self.pf_d.setText(f'{p_f}')
                            self.ivss_d.setText(f'{ivss}')
                            self.label_13.setText(f'{faov}')
                            self.cuota_sindical_d.setText(f'0')
                            self.deducciones_total.setText(f'Total deducciones: {deducciones}')
                            self.pago_neto.setText(f'Neto a Pagar: {neto}')
                
                    elif self.radioButton_2.isChecked():
                         asignaciones = asignaciones_user + payment + conf.prima_hogar + conf.prima_transporte + conf.prima_alimentacion + conf.prima_hijo*float(hijos[0]) + (conf.prima_profesion[profession]/100)*payment + (conf.prima_anti[service_years]/100)*payment
                         ivss = (payment*12)/52*0.04*4
                         ivss = round(ivss,2)
                         faov = 0.01*asignaciones
                         faov = round(faov,2)
                         p_f = (payment*12)/52*0.005*4
                         p_f = round(p_f,2)
                         cuota_sindical = payment*0.01

                         self.calendarWidget_2.clicked.connect(self.on_calendar_clicked)
                         selected_date = self.calendarWidget_2.selectedDate()  # Obtiene la fecha seleccionada
                         
                         first_day_of_month = QDate(selected_date.year(), selected_date.month(), 1) 
                         last_day_of_month = first_day_of_month.addMonths(1).addDays(-1)
                        
                         print(first_day_of_month, last_day_of_month)

                         if self.checkBox.isChecked():
                             deducciones = ivss + faov + p_f + cuota_sindical
                             deducciones = round(deducciones,2)
                             neto = asignaciones - deducciones
                             neto = round(neto,2)

                             self.prima_transporte.setText(f'{conf.prima_transporte}')
                             self.prima_hogar.setText(f'{conf.prima_hogar}')
                             self.prima_alimentacion.setText(f'{conf.prima_alimentacion}')
                             self.sueldo_base.setText(f'Sueldo base: {payment}')

                             self.prima_hijo.setText(f'{conf.prima_hijo*float(hijos[0]) }')
                             self.prima_antiguedad.setText(f'{(conf.prima_anti[service_years]/100)*payment}')
                             self.prima_profesion.setText(f'{(conf.prima_profesion[profession]/100)*payment}')
                             self.asignaciones.setText(f'Asignaciones: {asignaciones}')

                             self.pf_d.setText(f'{p_f}')
                             self.ivss_d.setText(f'{ivss}')
                             self.label_13.setText(f'{faov}')
                             self.cuota_sindical_d.setText(f'{cuota_sindical}')
                             self.deducciones_total.setText(f'Total deducciones: {deducciones}')
                             self.pago_neto.setText(f'Neto a Pagar: {neto}')
                         else:
                             deducciones = ivss + faov + p_f
                             deducciones = round(deducciones,2)

                             neto = asignaciones - deducciones
                             neto = round(neto,2)

                             self.prima_transporte.setText(f'{conf.prima_transporte}')
                             self.prima_hogar.setText(f'{conf.prima_hogar}')
                             self.prima_alimentacion.setText(f'{conf.prima_alimentacion}')
                             self.sueldo_base.setText(f'Sueldo base: {payment}')

                             self.prima_hijo.setText(f'{conf.prima_hijo*float(hijos[0]) }')
                             self.prima_antiguedad.setText(f'{(conf.prima_anti[service_years]/100)*payment}')
                             self.prima_profesion.setText(f'{(conf.prima_profesion[profession]/100)*payment}')
                             self.asignaciones.setText(f'Asignaciones: {asignaciones}')
 
                             self.pf_d.setText(f'{p_f}')
                             self.ivss_d.setText(f'{ivss}')
                             self.label_13.setText(f'{faov}')
                             self.cuota_sindical_d.setText(f'0')
                             self.deducciones_total.setText(f'Total deducciones: {deducciones}')
                             self.pago_neto.setText(f'Neto a Pagar: {neto}')

        except pymysql.MySQLError as e:
            print(f"Error de conexión a la base de datos: {e}")

    def creatingNomina(self):
        cedula_user = self.cedula_input.text()
        asignaciones_user = self.retribuciones_input.text()
        asignaciones_user = asignaciones_user.strip()
        asignaciones_user = 0 if asignaciones_user == '' else float(asignaciones_user)
        cedula_user = int(cedula_user)
        self.cedula = cedula_user
        print(cedula_user,'miraaa')
        connection = pymysql.connect(
                host='localhost',
                user='user_nomina',
                password='12345678',
                database='sc_db',
                charset='utf8'
                )
        try:
            with connection.cursor() as cursor:
                query = "SELECT payment from employee where cedula = %s "
                cursor.execute(query, cedula_user)
                payment = cursor.fetchone()

                if payment is not None:
                    payment = payment[0]

                    self.create_nomina_btn.clicked.connect(self.create_nomina_fnt)

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
                
                    #radio es quince 
                    if self.radioButton.isChecked():
                        payment = payment/2
                        asignaciones = asignaciones_user + payment + conf.prima_hogar/2 + conf.prima_transporte/2 + conf.prima_alimentacion/2 + conf.prima_hijo*float(hijos[0]) + (conf.prima_profesion[profession]/100)*(payment) + (conf.prima_anti[service_years]/100)*(payment)

                        ivss = ((payment)*12)/52*0.04*4
                        ivss = round(ivss,2)
                        faov = 0.01*asignaciones
                        faov = round(faov,2)
                        p_f = ((payment)*12)/52*0.005*4
                        p_f = round(p_f,2)
                        cuota_sindical = 0 

                        selected_date_start = self.calendarWidget_2.selectedDate()  # Obtiene la fecha seleccionada
                        selected_date_end = self.calendarWidget.selectedDate()  # Obtiene la fecha seleccionada

                        selected_date_start = selected_date_start.toString("yyyy-MM-dd")
                        selected_date_end = selected_date_end.toString("yyyy-MM-dd")

                        if self.checkBox.isChecked():
                            cuota_sindical = (payment)*0.01
                            deducciones = ivss + faov + p_f + cuota_sindical
                            deducciones = round(deducciones,2)
                            neto = asignaciones - deducciones
                            neto = round(neto,2)

                            self.prima_transporte.setText(f'{conf.prima_transporte/2}')
                            self.prima_hogar.setText(f'{conf.prima_hogar/2}')
                            self.prima_alimentacion.setText(f'{conf.prima_alimentacion/2}')
                            self.sueldo_base.setText(f'Sueldo base: {payment}')

                            self.prima_hijo.setText(f'{conf.prima_hijo*float(hijos[0]) }')
                            self.prima_antiguedad.setText(f'{(conf.prima_anti[service_years]/100)*(payment)}')
                            self.prima_profesion.setText(f'{(conf.prima_profesion[profession]/100)*(payment)}')
                            self.asignaciones.setText(f'Asignaciones: {asignaciones}')

                            self.pf_d.setText(f'{p_f}')
                            self.ivss_d.setText(f'{ivss}')
                            self.label_13.setText(f'{faov}')
                            self.cuota_sindical_d.setText(f'{cuota_sindical}')
                            self.deducciones_total.setText(f'Total deducciones: {deducciones}')
                            self.pago_neto.setText(f'Neto a Pagar: {neto}')
                            self.create_nomina_fnt(cedula_user, 
                                                   payment,
                                                   conf.prima_transporte/2,
                                                   conf.prima_hogar/2,
                                                   conf.prima_alimentacion/2,
                                                   conf.prima_hijo*float(hijos[0]),
                                                   (conf.prima_anti[service_years]/100)*payment,
                                                   (conf.prima_profesion[profession]/100)*payment,
                                                   asignaciones,deducciones
                                                   ,p_f
                                                   ,ivss,
                                                   faov,
                                                   cuota_sindical,
                                                   neto,selected_date_start,
                                                   'Quincenal',
                                                   selected_date_end)

                        else:
                            deducciones = ivss + faov + p_f
                            deducciones = round(deducciones,2)

                            neto = asignaciones - deducciones
                            neto = round(neto,2)

                            self.prima_transporte.setText(f'{conf.prima_transporte/2}')
                            self.prima_hogar.setText(f'{conf.prima_hogar/2}')
                            self.prima_alimentacion.setText(f'{conf.prima_alimentacion/2}')
                            self.sueldo_base.setText(f'Sueldo base: {payment}')

                            self.prima_hijo.setText(f'{conf.prima_hijo*float(hijos[0]) }')
                            self.prima_antiguedad.setText(f'{(conf.prima_anti[service_years]/100)*(payment)}')
                            self.prima_profesion.setText(f'{(conf.prima_profesion[profession]/100)*(payment)}')
                            self.asignaciones.setText(f'Asignaciones: {asignaciones}')

                            self.pf_d.setText(f'{p_f}')
                            self.ivss_d.setText(f'{ivss}')
                            self.label_13.setText(f'{faov}')
                            self.cuota_sindical_d.setText(f'0')
                            self.deducciones_total.setText(f'Total deducciones: {deducciones}')
                            self.pago_neto.setText(f'Neto a Pagar: {neto}')

                            self.create_nomina_fnt(cedula_user, 
                            payment,
                            conf.prima_transporte/2,
                            conf.prima_hogar/2,
                            conf.prima_alimentacion/2,
                            conf.prima_hijo*float(hijos[0]),
                            (conf.prima_anti[service_years]/100)*payment,
                            (conf.prima_profesion[profession]/100)*payment,
                            asignaciones,deducciones
                            ,p_f
                            ,ivss,
                            faov,
                            cuota_sindical,
                            neto,selected_date_start,
                            'Quincenal',
                            selected_date_end,
                            asignaciones_user)
                
                    elif self.radioButton_2.isChecked():
                         asignaciones = asignaciones_user + payment + conf.prima_hogar + conf.prima_transporte + conf.prima_alimentacion + conf.prima_hijo*float(hijos[0]) + (conf.prima_profesion[profession]/100)*payment + (conf.prima_anti[service_years]/100)*payment
                         ivss = (payment*12)/52*0.04*4
                         ivss = round(ivss,2)
                         faov = 0.01*asignaciones
                         faov = round(faov,2)
                         p_f = (payment*12)/52*0.005*4
                         p_f = round(p_f,2)
                         cuota_sindical = payment*0.01

                         self.calendarWidget_2.clicked.connect(self.on_calendar_clicked)
                         selected_date = self.calendarWidget_2.selectedDate()  # Obtiene la fecha seleccionada
                         
                         first_day_of_month = QDate(selected_date.year(), selected_date.month(), 1) 
                         last_day_of_month = first_day_of_month.addMonths(1).addDays(-1)

                         first_day_of_month = first_day_of_month.toString("yyyy-MM-dd")
                         last_day_of_month = last_day_of_month.toString("yyyy-MM-dd")
                        
                         print(first_day_of_month, last_day_of_month)

                         if self.checkBox.isChecked():
                             deducciones = ivss + faov + p_f + cuota_sindical
                             deducciones = round(deducciones,2)
                             neto = asignaciones - deducciones
                             neto = round(neto,2)

                             self.prima_transporte.setText(f'{conf.prima_transporte}')
                             self.prima_hogar.setText(f'{conf.prima_hogar}')
                             self.prima_alimentacion.setText(f'{conf.prima_alimentacion}')
                             self.sueldo_base.setText(f'Sueldo base: {payment}')

                             self.prima_hijo.setText(f'{conf.prima_hijo*float(hijos[0]) }')
                             self.prima_antiguedad.setText(f'{(conf.prima_anti[service_years]/100)*payment}')
                             self.prima_profesion.setText(f'{(conf.prima_profesion[profession]/100)*payment}')
                             self.asignaciones.setText(f'Asignaciones: {asignaciones}')

                             self.pf_d.setText(f'{p_f}')
                             self.ivss_d.setText(f'{ivss}')
                             self.label_13.setText(f'{faov}')
                             self.cuota_sindical_d.setText(f'{cuota_sindical}')
                             self.deducciones_total.setText(f'Total deducciones: {deducciones}')
                             self.pago_neto.setText(f'Neto a Pagar: {neto}')

                             self.create_nomina_fnt(cedula_user, 
                                                   payment,
                                                   conf.prima_transporte,
                                                   conf.prima_hogar,
                                                   conf.prima_alimentacion,
                                                   conf.prima_hijo*float(hijos[0]),
                                                   (conf.prima_anti[service_years]/100)*payment,
                                                   (conf.prima_profesion[profession]/100)*payment,
                                                   asignaciones,deducciones
                                                   ,p_f
                                                   ,ivss,
                                                   faov,
                                                   cuota_sindical,
                                                   neto,first_day_of_month,
                                                   'Mensual',
                                                   last_day_of_month,
                                                    asignaciones_user)

                         else:
                             deducciones = ivss + faov + p_f
                             deducciones = round(deducciones,2)

                             neto = asignaciones - deducciones
                             neto = round(neto,2)

                             self.prima_transporte.setText(f'{conf.prima_transporte}')
                             self.prima_hogar.setText(f'{conf.prima_hogar}')
                             self.prima_alimentacion.setText(f'{conf.prima_alimentacion}')
                             self.sueldo_base.setText(f'Sueldo base: {payment}')

                             self.prima_hijo.setText(f'{conf.prima_hijo*float(hijos[0]) }')
                             self.prima_antiguedad.setText(f'{(conf.prima_anti[service_years]/100)*payment}')
                             self.prima_profesion.setText(f'{(conf.prima_profesion[profession]/100)*payment}')
                             self.asignaciones.setText(f'Asignaciones: {asignaciones}')
 
                             self.pf_d.setText(f'{p_f}')
                             self.ivss_d.setText(f'{ivss}')
                             self.label_13.setText(f'{faov}')
                             self.cuota_sindical_d.setText(f'0')
                             self.deducciones_total.setText(f'Total deducciones: {deducciones}')
                             self.pago_neto.setText(f'Neto a Pagar: {neto}')
                             self.create_nomina_fnt(cedula_user, 
                                                   payment,
                                                   conf.prima_transporte,
                                                   conf.prima_hogar,
                                                   conf.prima_alimentacion,
                                                   conf.prima_hijo*float(hijos[0]),
                                                   (conf.prima_anti[service_years]/100)*payment,
                                                   (conf.prima_profesion[profession]/100)*payment,
                                                   asignaciones,deducciones
                                                   ,p_f
                                                   ,ivss,
                                                   faov,
                                                   cuota_sindical,
                                                   neto,first_day_of_month,
                                                   'Mensual',
                                                   last_day_of_month,
                                                    asignaciones_user)


        except pymysql.MySQLError as e:
            print(f"Error de conexión a la base de datos: {e}")

    def on_calendar_clicked(self, date):
        """Cuando se hace clic en una fecha del primer calendario, selecciona la fecha +15 días
        o la última fecha del mes si se pasa del mes actual."""
        # Sumar 15 días a la fecha seleccionada
        new_date = date.addDays(15)

        # Verificar si el mes ha cambiado
        if new_date.month() != date.month():
            # Obtener la última fecha del mes actual
            last_day_of_month = QDate(date.year(), date.month(), date.daysInMonth())
            self.calendarWidget.setSelectedDate(last_day_of_month)
        else:
            # Si no se pasa del mes, usar la fecha calculada
            self.calendarWidget.setSelectedDate(new_date)

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
""")

        connection = pymysql.connect(
                host='localhost',
                user='user_nomina',
                password='12345678',
                database='sc_db',
                charset='utf8'
                )
        try:
            with connection.cursor() as cursor:
                query = "insert into nominas(cedula, sueldo_base, prima_transporte, prima_hogar, prima_alimentacion, prima_hijo, prima_antiguedad, prima_profesion, asignaciones, deducciones_T,pf,ivss,faov,cuota_sindical,total_neto,fecha,type,fecha_fin,made_by, retributions) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(query, (cedula, sueldo_base, prima_transporte, prima_hogar, prima_alimentacion, prima_hijo, prima_antiguedad, prima_profesion, asignaciones, deducciones_T, pf, ivss, faov, cuota_sindical, total_neto, fecha, tipo, fecha_fin, conf.user, asignaciones_user))
                connection.commit()
                successfulWidget(self, message="Nomina creada exitosamente")


        except pymysql.MySQLError as e:
            print(f"Error de conexión a la base de datos: {e}")
