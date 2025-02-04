
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from reportlab.pdfgen import canvas
import pymysql
import conf
import os
from datetime import datetime


def generate_pdf_lista(self):
    try:
        print('Generando PDF con imágenes y encabezados...')
        connection = pymysql.connect(
            host='localhost',
            user='user_nomina',
            password='12345678',
            database='sc_db',
            charset='utf8'
        )

        # Consulta para obtener nóminas y unir datos con la tabla employee
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    nomina_cestaticket.cedula,  employee.tipo_cuenta ,employee.nro_cuenta, employee.name, employee.lastname, nomina_cestaticket.descuentos, nomina_cestaticket.total_neto, employee.nomina_type
                
                FROM 
                    nomina_cestaticket
                JOIN 
                    employee ON nomina_cestaticket.cedula = employee.cedula
            """)
            nominas = cursor.fetchall()

        # Cálculo de totales
        nomina_type = "Cestaticket"
        total_deducciones = sum([nomina[5] for nomina in nominas])
        total_nomina = sum([nomina[6] for nomina in nominas])

        # Configuración del archivo PDF
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(
            None,
            "Guardar PDF",
            "",
            "Archivos PDF (*.pdf);;Todos los archivos (*)",
            options=options
        )

        if file_path:
            if not file_path.endswith('.pdf'):
                file_path += '.pdf'

            # Crear el PDF
            c = canvas.Canvas(file_path)
            c.setFont("Helvetica", 10)

            # Rutas de las imágenes
            base_dir = os.path.dirname(os.path.abspath(__file__))
            img_path_alcaldia = os.path.join(base_dir, "../images/alcaldia_logo5.png")
            img_path_salud = os.path.join(base_dir, "../images/salud_logo.jpg")

            img_width = 80
            img_height = 80
            alcaldia_width = 250

            cuadro_y = 670
            contador = 0
            fecha_actual_2 = datetime.now().strftime("%d/%m/%Y")

            hora_24 = datetime.now()
            hora_actual = hora_24.strftime("%I:%M").lstrip("0")  # Remover el 0 inicial si existe
            periodo = "a.m." if hora_24.hour < 12 else "p.m."  # Determinar a.m. o p.m.
            hora_actual += f" {periodo}"  # Concatenar hora y periodo
            fecha_actual = datetime.now().strftime("%d-%b-%Y").lower()  # Formato de fecha

            # Encabezado de "hoy" y "hora"
            c.setFont("Helvetica-Bold", 10)
            c.drawString(50, 730, "Hoy:")
            c.drawString(190, 730, "Hora:")
            c.drawString(330, 730, "Listado de Nominas:")
            c.setFont("Helvetica", 10)
            c.drawString(80, 730, fecha_actual)  # Fecha formateada
            c.drawString(230, 730, hora_actual)  # Hora formateada
            c.drawString(445, 730, nomina_type)  # Hora formateada
 
            # Encabezado debajo de las imágenes
            c.setFont("Helvetica-Bold", 10)
            c.drawString(50, 700, "Nombre de la Empresa:")
            c.drawString(230, 700, "Cuenta Ordenante:")
            c.drawString(370, 700, "Monto Total Nómina:")
            c.drawString(490, 700, "Fecha Valor:")
            
            c.setFont("Helvetica", 10)
            c.drawString(50, 685, conf.institucion)
            c.drawString(230, 685, conf.cuenta_institucion)
            c.drawString(370, 685, f"${total_nomina:.2f}")
            c.drawString(490, 685, fecha_actual_2)
         
        
            for index, nomina in enumerate(nominas):
            # Si es la primera nómina o una nueva página
               if index == 0 or contador % 25 == 0:
                   if contador > 0:  # Para evitar crear una nueva página al inicio
                       c.showPage()
                       cuadro_y = 730  # Reiniciar la posición para la nueva página
           
                   # Añadir imágenes
                   c.drawImage(img_path_salud, 50, 750, img_width, img_height)
                   c.drawImage(img_path_alcaldia, 300, 750, alcaldia_width, img_height)
           
                   # Encabezados de las celdas
                   cuadro_y = 660 if index == 0 else 730  # Cambiar posición dependiendo de la página
                   c.setFont("Helvetica-Bold", 9)
                   c.drawString(50, cuadro_y, "Tipo")
                   c.drawString(100, cuadro_y, "Nro. Cuenta")
                   c.drawString(220, cuadro_y, "Monto")
                   c.drawString(300, cuadro_y, "Nombre Empleado")
                   c.drawString(490, cuadro_y, "Cédula Identidad")
                   cuadro_y -= 20
           
               # Datos de la nómina
               c.setFont("Helvetica", 9)
               tipo_cuenta = str(nomina[1])
               nro_cuenta = str(nomina[2])
               total_neto = f"${float(nomina[6]):.2f}"
               nombre_completo = f"{nomina[3]} {nomina[4]}"
               if len(nombre_completo) > 40:
                   nombre_completo = nombre_completo[:37] + "..."
               cedula = str(nomina[0])
           
               c.drawString(50, cuadro_y, tipo_cuenta)
               c.drawString(100, cuadro_y, nro_cuenta)
               c.drawString(220, cuadro_y, total_neto)
               c.drawString(300, cuadro_y, nombre_completo)
               c.drawString(490, cuadro_y, cedula)
           
               cuadro_y -= 20
               contador += 1
           
               # Salto de página si el contenido supera el margen
               if cuadro_y < 50:
                   c.showPage()
                   cuadro_y = 750
                   contador = 0
            c.save()
            QMessageBox.information(None, "Éxito", f"PDF guardado en: {file_path}")
        else:
            QMessageBox.warning(None, "Cancelado", "No se seleccionó ubicación para guardar el archivo.")
    except pymysql.MySQLError as e:
        QMessageBox.critical(None, "Error", f"Error al conectarse a la base de datos: {str(e)}")
    except Exception as e:
        QMessageBox.critical(None, "Error", f"Error al generar el PDF: {str(e)}")

