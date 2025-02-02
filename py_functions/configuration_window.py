from PyQt5.QtWidgets import QWidget, QMessageBox
from ui_py.config import Ui_Form
import conf_function  
import conf

class configurationWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.institucion.setMaxLength(20)
        self.rif.setMaxLength(9)
        self.ffgf.setText(str(conf.cesta_ticket))
        self.institucion_2.setText(str(conf.institucion))
        self.institucion.setText(str(conf.cuenta_institucion))
        self.nombre_licenciada.setText(str(conf.nombre_licenciada))
        self.cargo_licenciada.setText(str(conf.cargo_licenciada))

        self.deducciones_data = {
            "P.F": conf.p_f,
            "I.V.S.S": conf.i_v_s_s,
            "F.A.O.V": conf.f_a_o_v,
            "Cuota Sindical": conf.cuota_sindical
        }

        self.contratacion_data = {
            "Prima por Transporte": conf.prima_transporte,
            "Prima por Hogar": conf.prima_hogar,
            "Prima por Alimentacion": conf.prima_alimentacion,
            "Prima por Hijo": conf.prima_hijo
        }

        self.rif.setText(conf.rif)

        self.profesion_data = conf.prima_profesion.copy()
        self.antiguedad_data = conf.prima_anti.copy()

        self.actualizar_lineedit_deducciones()
        self.actualizar_lineedit_contratacion()
        self.actualizar_lineedit_profesion()
        self.actualizar_lineedit_antiguedad()

        self.deducciones.currentIndexChanged.connect(self.actualizar_lineedit_deducciones)
        self.contratacion.currentIndexChanged.connect(self.actualizar_lineedit_contratacion)
        self.profesion.currentIndexChanged.connect(self.actualizar_lineedit_profesion)
        self.antiguedad.currentIndexChanged.connect(self.actualizar_lineedit_antiguedad)

        # Conectar los botones a sus métodos correspondientes
        self.update_deducciones.clicked.connect(self.guardar_y_actualizar_deducciones)
        self.update_contratacion.clicked.connect(self.guardar_y_actualizar_contratacion)
        self.update_antiguedad.clicked.connect(self.guardar_y_actualizar_antiguedad)
        self.update_profesion.clicked.connect(self.guardar_y_actualizar_profesion)
        self.update_iupdate_institucion_3.clicked.connect(self.guardar_y_actualizar_institucion_name)
        self.cestactiket_input.clicked.connect(self.guardar_y_actualizar_cesta_ticket)
        self.cuenta_ordenante.clicked.connect(self.guardar_y_actualizar_institucion_ordenante)
        self.update_contratacion_5.clicked.connect(self.guardar_licenciada)
        self.rif_btn.clicked.connect(self.riffing)

    def actualizar_lineedit_antiguedad(self):
        item = self.antiguedad.currentText()
        valor = str(self.antiguedad_data.get(item, ""))
        self.antiguedad_input.setText(valor)

    def actualizar_lineedit_deducciones(self):
        item = self.deducciones.currentText()
        valor = str(self.deducciones_data.get(item, ""))
        self.deducciones_input.setText(valor)

    def actualizar_lineedit_profesion(self):
        item = self.profesion.currentText()
        valor = str(self.profesion_data.get(item, ""))
        self.profesion_input.setText(valor)

    def actualizar_lineedit_contratacion(self):
        item = self.contratacion.currentText()
        valor = str(self.contratacion_data.get(item, ""))
        self.contratacion_input.setText(valor)

    def guardar_y_actualizar_antiguedad(self):
        antiguedad_seleccionada = self.antiguedad.currentText()
        nuevo_valor = self.antiguedad_input.text()

        try:
            nuevo_valor = float(nuevo_valor)  # Asegurarse de que el valor ingresado sea float

            if antiguedad_seleccionada in self.antiguedad_data:
                # Actualizar el valor correspondiente en conf
                conf.prima_anti[antiguedad_seleccionada] = nuevo_valor

                # Guardar los cambios en el archivo conf.py
                conf_function.guardar_conf(conf, 'conf.py')

                # Actualizar archivos auxiliares
                conf_function.python_a_txt("conf.py", "converter.txt")
                conf_function.txt_a_python("converter.txt", "conf.py")

                # Mensaje de confirmación
                QMessageBox.information(self, "Guardado", f"Se actualizó la antigüedad '{antiguedad_seleccionada}' correctamente.")
            else:
                QMessageBox.warning(self, "Error", f"La antigüedad seleccionada '{antiguedad_seleccionada}' no es válida.")
        except ValueError:
            QMessageBox.warning(self, "Error", "El valor ingresado no es válido. Por favor, ingrese un número.")

    def guardar_y_actualizar_institucion_name(self):
        nuevo_nombre_institucion = self.institucion_2.text()  # Obtener el nuevo nombre de la caja de texto

        if nuevo_nombre_institucion:
            # Actualizar el valor en la configuración de conf
            conf.institucion = nuevo_nombre_institucion

            try:
                # Guardar todo en el archivo conf.py
                conf_function.guardar_conf(conf, 'conf.py')
                
                # Actualizar archivos auxiliares
                conf_function.python_a_txt("conf.py", "converter.txt")
                conf_function.txt_a_python("converter.txt", "conf.py")

                # Confirmar que todo se actualizó correctamente
                QMessageBox.information(self, "Guardado", "Se actualizó el nombre de la institución correctamente.")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Hubo un error al guardar: {str(e)}")
        else:
            QMessageBox.warning(self, "Error", "Por favor, ingrese el nombre de la institución.")

    def riffing(self):
        rif = self.rif.text()  # Obtener el nuevo nombre de la caja de texto

        if rif:
            # Actualizar el valor en la configuración de conf
            conf.rif = rif

            try:
                # Guardar todo en el archivo conf.py
                conf_function.guardar_conf(conf, 'conf.py')
                
                # Actualizar archivos auxiliares
                conf_function.python_a_txt("conf.py", "converter.txt")
                conf_function.txt_a_python("converter.txt", "conf.py")

                # Confirmar que todo se actualizó correctamente
                QMessageBox.information(self, "Guardado", "Se actualizó el Rif correctamente.")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Hubo un error al guardar: {str(e)}")
        else:
            QMessageBox.warning(self, "Error", "Por favor, ingrese el valor requerido.")
    def guardar_licenciada(self):
        print('boop')
        nombre_licenciada = self.nombre_licenciada.text().title()  # Obtener el nuevo nombre de la caja de texto
        cargo_licenciada = self.cargo_licenciada.text()

        if nombre_licenciada and cargo_licenciada: 
            # Actualizar el valor en la configuración de conf
            conf.nombre_licenciada = nombre_licenciada
            conf.cargo_licenciada = cargo_licenciada

            try:
                # Guardar todo en el archivo conf.py
                conf_function.guardar_conf(conf, 'conf.py')
                
                # Actualizar archivos auxiliares
                conf_function.python_a_txt("conf.py", "converter.txt")
                conf_function.txt_a_python("converter.txt", "conf.py")

                # Confirmar que todo se actualizó correctamente
                QMessageBox.information(self, "Guardado", "Se actualizó correctamente.")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Hubo un error al guardar: {str(e)}")
        elif nombre_licenciada: 
            # Actualizar el valor en la configuración de conf
            conf.nombre_licenciada = nombre_licenciada

            try:
                # Guardar todo en el archivo conf.py
                conf_function.guardar_conf(conf, 'conf.py')
                
                # Actualizar archivos auxiliares
                conf_function.python_a_txt("conf.py", "converter.txt")
                conf_function.txt_a_python("converter.txt", "conf.py")

                # Confirmar que todo se actualizó correctamente
                QMessageBox.information(self, "Guardado", "Se actualizó correctamente.")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Hubo un error al guardar: {str(e)}")
        elif cargo_licenciada: 
            # Actualizar el valor en la configuración de conf
            conf.cargo_licenciada = cargo_licenciada

            try:
                # Guardar todo en el archivo conf.py
                conf_function.guardar_conf(conf, 'conf.py')
                
                # Actualizar archivos auxiliares
                conf_function.python_a_txt("conf.py", "converter.txt")
                conf_function.txt_a_python("converter.txt", "conf.py")

                # Confirmar que todo se actualizó correctamente
                QMessageBox.information(self, "Guardado", "Se actualizó correctamente.")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Hubo un error al guardar: {str(e)}")
        else:
            QMessageBox.warning(self, "Error", "Por favor, ingrese algun dato")

    def guardar_y_actualizar_institucion_ordenante(self):
        cuenta_texto = self.institucion.text()  # Obtener el valor ingresado como texto

        try:
            # Intentar convertir el texto a un número float
            cuenta = str(cuenta_texto)

            # Asignar el valor al archivo de configuración
            conf.cuenta_institucion = cuenta

            # Guardar todo en el archivo conf.py
            conf_function.guardar_conf(conf, 'conf.py')
            
            # Actualizar archivos auxiliares
            conf_function.python_a_txt("conf.py", "converter.txt")
            conf_function.txt_a_python("converter.txt", "conf.py")

            # Confirmar que todo se actualizó correctamente
            QMessageBox.information(self, "Guardado", "Se actualizó la cuenta ordenante de la institución correctamente.")

        except ValueError:
            QMessageBox.warning(self, "Error", "La cuenta ordenante debe ser un número válido.")

        except Exception as e:
            QMessageBox.warning(self, "Error", f"Hubo un error al guardar: {str(e)}")

    def guardar_y_actualizar_cesta_ticket(self):
        cestaticket = self.ffgf.text()  # Obtener el nuevo nombre de la caja de texto
        if cestaticket:
            conf.cesta_ticket = cestaticket

            try:
                conf_function.guardar_conf(conf, 'conf.py')
                conf_function.python_a_txt("conf.py", "converter.txt")
                conf_function.txt_a_python("converter.txt", "conf.py")

                QMessageBox.information(self, "Guardado", "Se actualizó el monto de Cestaticket correctamente.")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Hubo un error al guardar: {str(e)}")
        else:
            QMessageBox.warning(self, "Error", "Por favor, Coloque el valor requerido.")

    def guardar_y_actualizar_deducciones(self):
        deduccion_seleccionada = self.deducciones.currentText()
        nuevo_valor = self.deducciones_input.text()
        
        try:
            nuevo_valor = float(nuevo_valor)
            
            if deduccion_seleccionada in self.deducciones_data:
                if deduccion_seleccionada == "P.F":
                    conf.p_f = nuevo_valor
                    print(conf.p_f)
                elif deduccion_seleccionada == "I.V.S.S":
                    conf.i_v_s_s = nuevo_valor
                elif deduccion_seleccionada == "F.A.O.V":
                    conf.f_a_o_v = nuevo_valor
                elif deduccion_seleccionada == "Cuota Sindical":
                    conf.cuota_sindical = nuevo_valor
                
                # Guardar los cambios
                conf_function.guardar_conf(conf, 'conf.py')
                conf_function.python_a_txt("conf.py", "converter.txt")
                conf_function.txt_a_python("converter.txt", "conf.py")
                
                # Mostrar mensaje de éxito
                QMessageBox.information(self, "Guardado", f"Se actualizó la deducción '{deduccion_seleccionada}' con éxito.")
            else:
                QMessageBox.warning(self, "Error", "No se pudo actualizar la deducción seleccionada.")
        except ValueError:
            # Mostrar advertencia si el valor ingresado no es numérico
            QMessageBox.warning(self, "Error", "Por favor, ingrese un valor numérico válido.")

    def guardar_y_actualizar_contratacion(self):
        contratacion_seleccionada = self.contratacion.currentText()
        nuevo_valor = self.contratacion_input.text()
        try:
            nuevo_valor = float(nuevo_valor)  # Convertir el nuevo valor a float
            if contratacion_seleccionada in self.contratacion_data:
                # Actualizar el valor en la configuración correspondiente
                if contratacion_seleccionada == "Prima por Transporte":
                    conf.prima_transporte = nuevo_valor
                elif contratacion_seleccionada == "Prima por Hogar":
                    conf.prima_hogar = nuevo_valor
                elif contratacion_seleccionada == "Prima por Alimentacion":
                    conf.prima_alimentacion = nuevo_valor
                elif contratacion_seleccionada == "Prima por Hijo":
                    conf.prima_hijo = nuevo_valor

                conf_function.guardar_conf(conf, 'conf.py')
                conf_function.python_a_txt("conf.py", "converter.txt")
                conf_function.txt_a_python("converter.txt", "conf.py")

                QMessageBox.information(self, "Guardado", f"Se actualizó la prima de contratación '{contratacion_seleccionada}' con éxito.")
            else:
                QMessageBox.warning(self, "Error", f"La contratación seleccionada '{contratacion_seleccionada}' no es válida.")
        except ValueError:
            QMessageBox.warning(self, "Error", "El valor ingresado no es válido. Por favor, ingrese un número.")


    def guardar_y_actualizar_profesion(self):
        profesion_seleccionada = self.profesion.currentText()
        nuevo_valor = self.profesion_input.text()
        try:
            nuevo_valor = float(nuevo_valor)  # Convertir el nuevo valor a float
            if profesion_seleccionada in self.profesion_data:
                conf.prima_profesion[profesion_seleccionada] = nuevo_valor
                conf_function.guardar_conf(conf, 'conf.py')

                # Actualizar los archivos auxiliares
                conf_function.python_a_txt("conf.py", "converter.txt")
                conf_function.txt_a_python("converter.txt", "conf.py")

                # Mostrar mensaje de éxito
                QMessageBox.information(self, "Guardado", f"Se actualizó la prima de profesión '{profesion_seleccionada}' con éxito.")
            else:
                QMessageBox.warning(self, "Error", f"La profesión seleccionada '{profesion_seleccionada}' no es válida.")
        except ValueError:
            QMessageBox.warning(self, "Error", "El valor ingresado no es válido. Por favor, ingrese un número.")

    def guardar_y_actualizar(self):
        sender = self.sender()  # Obtiene el nombre del botón que fue presionado
        print(f"Botón {sender.text()} presionado.")

        # Ejecutar las funciones de guardado
        conf_function.python_a_txt("conf.py", "converter.txt")
        conf_function.txt_a_python("converter.txt", "conf.py")

        # Mostrar mensaje de confirmación
        QMessageBox.information(self, "Confirmación", "¡Guardado correctamente!")
