from PyQt5.QtCore import Qt
import pymysql
from ui_py.edit_info_nomina import Ui_Form
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QDoubleValidator, QIntValidator 

class edit_info_nomina(QWidget, Ui_Form):
    def __init__(self):   
       super().__init__()
       self.setupUi(self)
       self.cedula = 0
       self.c_type = ''
       self.filter.stateChanged.connect(self.handle_filter_change)
       intRange = QDoubleValidator(0.0,99.9,0,self)
       self.lineEdit_2.setValidator(intRange)
       self.lineEdit_2.setMaxLength(6)
       days_validator = QIntValidator(0,15,self)
       self.lineEdit.setValidator(days_validator)
       self.lineEdit.setMaxLength(2)
       self.lineEdit_2.textChanged.connect(self.update_retributions)
       self.lineEdit.textChanged.connect(self.validate_days)
       self.confirm.clicked.connect(self.close)
       self.analizer = False


    def load_data(self):
         connection = pymysql.connect(
             host='localhost',
             user='user_nomina',
              password='12345678',
              database='sc_db',
              charset='utf8'
              )
         try:
             with connection.cursor() as cursor:

                   if self.c_type == 'S':
                       query = "select concat(name,' ',lastname) as fullname from employee where cedula = %s "
                       cursor.execute(query, self.cedula)
                       fullname = cursor.fetchone()
                       self.nombre.setText(f'{fullname[0]} (Nómina)')
                       self.trabajo.setText(self.cedula)
                   
                       query = "select prima_transporte from nomina_semanal_prev where cedula = %s "
                       cursor.execute(query, self.cedula)
                       academic = cursor.fetchone()
                       self.academico.setText(str(academic[0]))
                   
                       query = "select prima_alimentacion from nomina_semanal_prev where cedula = %s "
                       cursor.execute(query, self.cedula)
                       profesion = cursor.fetchone()
                       self.porfesion.setText(str(profesion[0]))
                   
                       query = "select prima_antiguedad from nomina_semanal_prev where cedula = %s "
                       cursor.execute(query, self.cedula)
                       onapre = cursor.fetchone()
                       self.onapre.setText(str(onapre[0]))
                   
                       query = "select asignaciones from nomina_semanal_prev where cedula = %s "
                       cursor.execute(query, self.cedula)
                       inicio = cursor.fetchone()
                       self.inicio.setText(str(inicio[0]))
                   
                       query = "select pf from nomina_semanal_prev where cedula = %s "
                       cursor.execute(query, self.cedula)
                       servicio = cursor.fetchone()
                       self.servicio.setText(str(servicio[0]))
                   
                       query = "select faov from nomina_semanal_prev where cedula = %s "
                       cursor.execute(query, self.cedula)
                       location = cursor.fetchone()
                       self.ubicacion.setText(str(location[0]))
                   
                       query = "select total_neto from nomina_semanal_prev where cedula = %s "
                       cursor.execute(query, self.cedula)
                       salario = cursor.fetchone()
                       self.salario.setText(str(salario[0]))

                       cursor.execute('select deducciones_T, sueldo_base, ivss,faov,pf,cuota_sindical from nomina_semanal_prev where cedula = %s', self.cedula)

                       vals = cursor.fetchall()
                       print('los vals', vals[0])
                       deducciones, pago,ivss,faov,pf,cuota_sindical = vals[0] 


                       nro_dias_desc = deducciones - (ivss + faov + pf + cuota_sindical)
                       pago_d = pago/7

                       n_dias = int(nro_dias_desc/pago_d)
                       
                       self.lineEdit.textChanged.disconnect(self.validate_days)
                       self.lineEdit.setText(str(n_dias))
                       self.lineEdit.textChanged.connect(self.validate_days)
                   
                       query = "select fecha from nomina_semanal_prev where cedula = %s "
                       cursor.execute(query, self.cedula)
                       nomina = cursor.fetchone()
                       self.nomina.setText(str(nomina[0]))
                   
                       query = "select made_by from nomina_semanal_prev where cedula = %s "
                       cursor.execute(query, self.cedula)
                       made_by = cursor.fetchone()
                   
                       query = "select concat(name,' ',lastname) as fullname from employee where cedula = %s "
                       cursor.execute(query, made_by)
                       created_by = cursor.fetchone()
                       self.estatus.setText(str(created_by[0]))
                   
                       query = "select sueldo_base from nomina_semanal_prev where cedula = %s "
                       cursor.execute(query, self.cedula)
                       nomina = cursor.fetchone()
                       self.trabajo_2.setText(str(nomina[0]))
                   
                       query = "select prima_hogar from nomina_semanal_prev where cedula = %s "
                       cursor.execute(query, self.cedula)
                       academic = cursor.fetchone()
                       self.academico_2.setText(str(academic[0]))
                   
                       query = "select prima_hijo from nomina_semanal_prev where cedula = %s "
                       cursor.execute(query, self.cedula)
                       profesion_2 = cursor.fetchone()
                       self.porfesion_2.setText(str(profesion_2[0]))
                   
                       query = "select prima_profesion from nomina_semanal_prev where cedula = %s "
                       cursor.execute(query, self.cedula)
                       onapre_2 = cursor.fetchone()
                       self.onapre_2.setText(str(onapre_2[0]))
                   
                       query = "select deducciones_T from nomina_semanal_prev where cedula = %s "
                       cursor.execute(query, self.cedula)
                       inicio_2 = cursor.fetchone()
                       self.inicio_2.setText(str(inicio_2[0]))
                   
                       query = "select ivss from nomina_semanal_prev where cedula = %s "
                       cursor.execute(query, self.cedula)
                       servicio_2 = cursor.fetchone()
                       self.servicio_2.setText(str(servicio_2[0]))
                   
                       query = "select cuota_sindical from nomina_semanal_prev where cedula = %s "
                       cursor.execute(query, self.cedula)
                       location = cursor.fetchone()
                       self.ubicacion_2.setText(str(location[0]))
                   
                       query = "select fecha_fin from nomina_semanal_prev where cedula = %s "
                       cursor.execute(query, self.cedula)
                       nomina = cursor.fetchone()
                       self.nomina_2.setText(str(nomina[0]))
                   
                       query = "select retributions from nomina_semanal_prev where cedula = %s "
                       cursor.execute(query, self.cedula)
                       retributions = cursor.fetchone()
                       self.lineEdit_2.setText(str(retributions[0]))
                   
                   else:
                       query = "select concat(name,' ',lastname) as fullname from employee where cedula = %s "
                       cursor.execute(query, self.cedula)
                       fullname = cursor.fetchone()
                       self.nombre.setText(f'{fullname[0]} (Nómina)')
                       self.trabajo.setText(self.cedula)
                   
                       query = "select prima_transporte from nominas where cedula = %s "
                       cursor.execute(query, self.cedula)
                       academic = cursor.fetchone()
                       self.academico.setText(str(academic[0]))
                   
                       query = "select prima_alimentacion from nominas where cedula = %s "
                       cursor.execute(query, self.cedula)
                       profesion = cursor.fetchone()
                       self.porfesion.setText(str(profesion[0]))
                   
                       query = "select prima_antiguedad from nominas where cedula = %s "
                       cursor.execute(query, self.cedula)
                       onapre = cursor.fetchone()
                       self.onapre.setText(str(onapre[0]))
                   
                       query = "select asignaciones from nominas where cedula = %s "
                       cursor.execute(query, self.cedula)
                       inicio = cursor.fetchone()
                       self.inicio.setText(str(inicio[0]))
                   
                       query = "select pf from nominas where cedula = %s "
                       cursor.execute(query, self.cedula)
                       servicio = cursor.fetchone()
                       self.servicio.setText(str(servicio[0]))
                   
                       query = "select faov from nominas where cedula = %s "
                       cursor.execute(query, self.cedula)
                       location = cursor.fetchone()
                       self.ubicacion.setText(str(location[0]))
                   
                       query = "select total_neto from nominas where cedula = %s "
                       cursor.execute(query, self.cedula)
                       salario = cursor.fetchone()
                       self.salario.setText(str(salario[0]))
                   
                       query = "select fecha from nominas where cedula = %s "
                       cursor.execute(query, self.cedula)
                       nomina = cursor.fetchone()
                       self.nomina.setText(str(nomina[0]))
                   
                       query = "select made_by from nominas where cedula = %s "
                       cursor.execute(query, self.cedula)
                       made_by = cursor.fetchone()
                   
                       query = "select concat(name,' ',lastname) as fullname from employee where cedula = %s "
                       cursor.execute(query, made_by)
                       created_by = cursor.fetchone()
                       self.estatus.setText(str(created_by[0]))
                   
                       query = "select sueldo_base from nominas where cedula = %s "
                       cursor.execute(query, self.cedula)
                       nomina = cursor.fetchone()
                       self.trabajo_2.setText(str(nomina[0]))
                   
                       query = "select prima_hogar from nominas where cedula = %s "
                       cursor.execute(query, self.cedula)
                       academic = cursor.fetchone()
                       self.academico_2.setText(str(academic[0]))
                   
                       query = "select prima_hijo from nominas where cedula = %s "
                       cursor.execute(query, self.cedula)
                       profesion_2 = cursor.fetchone()
                       self.porfesion_2.setText(str(profesion_2[0]))
                   
                       query = "select prima_profesion from nominas where cedula = %s "
                       cursor.execute(query, self.cedula)
                       onapre_2 = cursor.fetchone()
                       self.onapre_2.setText(str(onapre_2[0]))
                   
                       query = "select deducciones_T from nominas where cedula = %s "
                       cursor.execute(query, self.cedula)
                       inicio_2 = cursor.fetchone()
                       self.inicio_2.setText(str(inicio_2[0]))
                   
                       query = "select ivss from nominas where cedula = %s "
                       cursor.execute(query, self.cedula)
                       servicio_2 = cursor.fetchone()
                       self.servicio_2.setText(str(servicio_2[0]))
                   
                       query = "select cuota_sindical from nominas where cedula = %s "
                       cursor.execute(query, self.cedula)
                       location = cursor.fetchone()
                       self.ubicacion_2.setText(str(location[0]))

                       cursor.execute('select deducciones_T, sueldo_base, ivss,faov,pf,cuota_sindical from nominas where cedula = %s', self.cedula)

                       vals = cursor.fetchall()
                       deducciones, pago,ivss,faov,pf,cuota_sindical = vals[0] 

                       nro_dias_desc = deducciones - (ivss + faov + pf + cuota_sindical)

                       if self.c_type == 'M':
                           pago_d = pago/30
                       else:
                           pago_d = pago/15

                       n_dias = int(nro_dias_desc/pago_d)
                       print(nro_dias_desc,' ', pago_d,' ',n_dias)

                       self.lineEdit.textChanged.disconnect(self.validate_days)
                       
                       self.lineEdit.setText(str(n_dias))
                   
                       self.lineEdit.textChanged.connect(self.validate_days)

                       query = "select fecha_fin from nominas where cedula = %s "
                       cursor.execute(query, self.cedula)
                       nomina = cursor.fetchone()
                       self.nomina_2.setText(str(nomina[0]))
                   
                       query = "select retributions from nominas where cedula = %s "
                       cursor.execute(query, self.cedula)
                       retributions = cursor.fetchone()
                       self.lineEdit_2.setText(str(retributions[0]))

         except pymysql.MySQLError as e:
             print(e)

       

    def handle_filter_change(self):
        connection = pymysql.connect(
            host='localhost',
            user='user_nomina',
            password='12345678',
            database='sc_db',
            charset='utf8'
        )
        cursor = connection.cursor()

        # Si el botón está marcado
        if self.filter.isChecked():

            # Obtener payment
            query = "SELECT payment FROM employee WHERE cedula = %s"
            cursor.execute(query, (self.cedula,))
            payment = cursor.fetchone()[0]
            cuota_sindical = round(payment * 0.01, 2)

            if self.c_type == 'S':
                query = "UPDATE nomina_semanal_prev SET cuota_sindical = %s WHERE cedula = %s"

                cursor.execute(query, (cuota_sindical, self.cedula))
                connection.commit()

                query = "SELECT ivss, faov, pf, asignaciones, retributions, sueldo_base, prima_transporte, prima_hogar, prima_alimentacion, prima_hijo, prima_antiguedad, prima_profesion FROM nomina_semanal_prev WHERE cedula = %s"

                cursor.execute(query, (self.cedula,))

                ivss, faov, p_f, asignaciones, retribuciones, sueldo_base, prima_transporte, prima_hogar, prima_alimentacion, prima_hijo, prima_antiguedad, prima_profesion = cursor.fetchone()

                asignaciones = prima_alimentacion + prima_antiguedad + prima_hijo + prima_hogar + prima_profesion + sueldo_base + prima_transporte + retribuciones

                asignaciones = round(asignaciones, 2)
        
                sueldo_diario = sueldo_base/7

                sueldo_diario = round(sueldo_diario, 2)

                dias_descontados_input = 0 if self.lineEdit.text() == '' else int(self.lineEdit.text())
    
                dias_descontados = round(float(dias_descontados_input) * sueldo_diario , 2)
    
                faov = round((asignaciones) * 0.01, 2)
                deducciones = round(ivss + faov + p_f + cuota_sindical + dias_descontados, 2)
                neto = round(asignaciones - deducciones, 2)
            
                # Actualizar los valores calculados
    
                query = "UPDATE nomina_semanal_prev SET deducciones_T = %s, total_neto = %s, asignaciones = %s, faov = %s WHERE cedula = %s"
                cursor.execute(query, (deducciones, neto, prima_alimentacion + prima_antiguedad + prima_hijo + prima_hogar + prima_profesion + sueldo_base + prima_transporte + retribuciones, faov,self.cedula))

                connection.commit()
                connection.close()
    
            else:
                query = "UPDATE nominas SET cuota_sindical = %s WHERE cedula = %s"
                cursor.execute(query, (cuota_sindical, self.cedula))
                connection.commit()

                query = "SELECT ivss, faov, pf, asignaciones, retributions, cuota_sindical, sueldo_base, prima_transporte, prima_hogar, prima_alimentacion, prima_hijo, prima_antiguedad, prima_profesion FROM nominas WHERE cedula = %s"

                cursor.execute(query, (self.cedula,))

                ivss, faov, p_f, asignaciones, retribuciones, cuota_sindical, sueldo_base, prima_transporte, prima_hogar, prima_alimentacion, prima_hijo, prima_antiguedad, prima_profesion = cursor.fetchone()

                # Recalcular asignaciones, deducciones, y total_neto

                asignaciones = prima_alimentacion + prima_antiguedad + prima_hijo + prima_hogar + prima_profesion + sueldo_base + prima_transporte + retribuciones

                asignaciones = round(asignaciones, 2)

                if self.c_type == "Q":
                    sueldo_diario = sueldo_base/15

                else:
                    sueldo_diario = sueldo_base/30

                sueldo_diario = round(sueldo_diario, 2)

                dias_descontados_input = 0 if self.lineEdit.text() == '' else int(self.lineEdit.text())

                dias_descontados = round(float(dias_descontados_input) * sueldo_diario , 2)

                faov = round((asignaciones) * 0.01, 2)
                deducciones = round(ivss + faov + p_f + cuota_sindical + dias_descontados, 2)

                neto = round(asignaciones - deducciones, 2)
        
                # Actualizar los valores calculados

                query = "UPDATE nominas SET deducciones_T = %s, total_neto = %s, asignaciones = %s, faov = %s WHERE cedula = %s"
                cursor.execute(query, (deducciones, neto, prima_alimentacion + prima_antiguedad + prima_hijo + prima_hogar + prima_profesion + sueldo_base + prima_transporte + retribuciones, faov,self.cedula))
 
                connection.commit()
                connection.close()

        else:
            cuota_sindical = 0

            if self.c_type == 'S':
                query = "UPDATE nomina_semanal_prev SET cuota_sindical = %s WHERE cedula = %s"

                cursor.execute(query, (cuota_sindical, self.cedula))
                connection.commit()

                query = "SELECT ivss, faov, pf, asignaciones, retributions, cuota_sindical, sueldo_base, prima_transporte, prima_hogar, prima_alimentacion, prima_hijo, prima_antiguedad, prima_profesion FROM nomina_semanal_prev WHERE cedula = %s"

                cursor.execute(query, (self.cedula,))

                ivss, faov, p_f, asignaciones, retribuciones, cuota_sindical, sueldo_base, prima_transporte, prima_hogar, prima_alimentacion, prima_hijo, prima_antiguedad, prima_profesion = cursor.fetchone()

                asignaciones = prima_alimentacion + prima_antiguedad + prima_hijo + prima_hogar + prima_profesion + sueldo_base + prima_transporte + retribuciones

                asignaciones = round(asignaciones,2)
        
                sueldo_diario = sueldo_base/7

                sueldo_diario = round(sueldo_diario, 2)

                dias_descontados_input = 0 if self.lineEdit.text() == '' else int(self.lineEdit.text())
    
                dias_descontados = round(float(dias_descontados_input) * sueldo_diario , 2)
    
                faov = round((asignaciones) * 0.01, 2)
                deducciones = round(ivss + faov + p_f + cuota_sindical + dias_descontados, 2)

                neto = round(asignaciones - deducciones, 2)
            
                # Actualizar los valores calculados
    
                query = "UPDATE nomina_semanal_prev SET deducciones_T = %s, total_neto = %s, asignaciones = %s, faov = %s WHERE cedula = %s"
                cursor.execute(query, (deducciones, neto, prima_alimentacion + prima_antiguedad + prima_hijo + prima_hogar + prima_profesion + sueldo_base + prima_transporte + retribuciones, faov,self.cedula))

                connection.commit()
                connection.close()
    
            else:
                query = "UPDATE nominas SET cuota_sindical = %s WHERE cedula = %s"
                cursor.execute(query, (cuota_sindical, self.cedula))
                connection.commit()

                query = "SELECT ivss, faov, pf, asignaciones, retributions, cuota_sindical, sueldo_base, prima_transporte, prima_hogar, prima_alimentacion, prima_hijo, prima_antiguedad, prima_profesion FROM nominas WHERE cedula = %s"

                cursor.execute(query, (self.cedula,))

                ivss, faov, p_f, asignaciones, retribuciones, cuota_sindical, sueldo_base, prima_transporte, prima_hogar, prima_alimentacion, prima_hijo, prima_antiguedad, prima_profesion = cursor.fetchone()

                asignaciones = prima_alimentacion + prima_antiguedad + prima_hijo + prima_hogar + prima_profesion + sueldo_base + prima_transporte + retribuciones
        
                if self.c_type == "Q":
                    sueldo_diario = sueldo_base/15

                else:
                    sueldo_diario = sueldo_base/30

                sueldo_diario = round(sueldo_diario, 2)

                asignaciones = round(asignaciones, 2)

                dias_descontados_input = 0 if self.lineEdit.text() == '' else int(self.lineEdit.text())

                dias_descontados = round(float(dias_descontados_input) * sueldo_diario , 2)

                faov = round((asignaciones) * 0.01, 2)
                deducciones = round(ivss + faov + p_f + cuota_sindical + dias_descontados, 2)



                neto = round(asignaciones - deducciones, 2)
        
                # Actualizar los valores calculados

                query = "UPDATE nominas SET deducciones_T = %s, total_neto = %s, asignaciones = %s, faov = %s WHERE cedula = %s"
                cursor.execute(query, (deducciones, neto, prima_alimentacion + prima_antiguedad + prima_hijo + prima_hogar + prima_profesion + sueldo_base + prima_transporte + retribuciones, faov,self.cedula))
 
                connection.commit()
                connection.close()


        self.load_data()

    def open_window(self, cedula, c_type):
        self.showMaximized()
        self.c_type = c_type
        self.cedula = cedula
        self.load_data()

    def update_retributions(self, text):
        connection = pymysql.connect(
            host='localhost',
            user='user_nomina',
            password='12345678',
            database='sc_db',
            charset='utf8',
            )

        cursor = connection.cursor()
        val = str(text)
        if val == '':
            val = 0
        else:
            val = int(text)
            if self.c_type == 'S':
                query = "update nomina_semanal_prev set retributions = %s where cedula = %s";
                cursor.execute (query,(val,self.cedula))
                connection.commit()

            else:
                query = "update nominas set retributions = %s where cedula = %s";
                cursor.execute (query,(val,self.cedula))
                connection.commit()


        self.handle_filter_change()

    def validate_days(self):

            text = self.lineEdit.text()
        
            if not self.lineEdit.text().strip():  # Verificar si está vacío o solo tiene espacios
                self.lineEdit.setText("0")
                
                if text == "0":
                    value = 0  # Establecer el valor como 0
                elif text == "00":  # Evitar múltiples ceros al inicio
                    self.lineEdit.setText("0")                        
                    value = 0
                return
            
            elif text.startswith("0") and len(text) > 1:
                # Si comienza con "0" pero tiene más dígitos, elimina el "0" inicial
                self.lineEdit.setText(text[1:])
                return

            else:
             # Validar rango y corregir si es necesario
                 try:
                     value = int(text)
                     if value > 15 and self.c_type == 'Q':
                         self.lineEdit.setText('15')  # Limitar al máximo permitido
                     elif value > 30 and self.c_type == 'M':
                         self.lineEdit.setText('30')  # Limitar al máximo permitido
                     elif value > 7 and self.c_type == 'S':
                         self.lineEdit.setText('7')  # Limitar al máximo permitido

                 except ValueError:
                     self.lineEdit.setText('0')  # Reemplazar valores inválidos con '0'
                 self.handle_filter_change()


