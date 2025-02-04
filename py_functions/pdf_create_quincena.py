from PyQt5.QtWidgets import QFileDialog, QMessageBox
from reportlab.pdfgen import canvas
import pymysql
import os


def generate_pdf(type_nomina):
    print('Generando PDF...')
    connection = pymysql.connect(
        host='localhost',
        user='user_nomina',
        password='12345678',
        database='sc_db',
        charset='utf8'
    )

    if type_nomina == 'S':
        print('en S')
        # Consulta para obtener todas las nóminas
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM nomina_semanal_prev")
            nominas = cursor.fetchall()
    
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
            # Configuración inicial
            cuadro_x = 50
            margen_superior = 130
            cuadro_y = 720 - margen_superior  # Añadir margen superior de 50 puntos
            cuadro_ancho = 500
            cuadro_alto = 140  # Incluye espacio adicional para la celda superior
            line_spacing = 15
            items_por_pagina = 4  # Número de cuadros por página
            contador = 0
    
            base_dir = os.path.dirname(os.path.abspath(__file__))
            img_path_alcaldia = os.path.join(base_dir, "../images/alcaldia_logo5.png")
            img_path_salud = os.path.join(base_dir, "../images/salud_logo.jpg")
    
            img_width = 80
            img_height = 80
    
            alcaldia_width = 250

            c.drawImage(img_path_salud, 50, 750, img_width, img_height)
            c.drawImage(img_path_alcaldia, 300, 750, alcaldia_width, img_height)
    
            for nomina in nominas:
                cursor = connection.cursor()
                query = "select concat(name, ' ', lastname) as fullname from employee where cedula = %s;"
                cursor.execute(query, nomina[0])
                nombre = cursor.fetchone()
                nombre = nombre[0]
                # Si se excede el número de cuadros permitidos por página, crear nueva página
                if contador > 0 and contador % items_por_pagina == 0:
                    c.showPage()
                    cuadro_y = 720 - margen_superior  # Reiniciar la posición del cuadro                
                    c.drawImage(img_path_salud, 50, 750, img_width, img_height)
                    c.drawImage(img_path_alcaldia, 300, 750, alcaldia_width, img_height)
    
                if contador == 1 :
                    c.drawImage(img_path_salud, 50, 750, img_width, img_height)
                    c.drawImage(img_path_alcaldia, 300, 750, alcaldia_width, img_height)
    
    
                # Dibujar el cuadro principal
                c.rect(cuadro_x, cuadro_y, cuadro_ancho, cuadro_alto, stroke=1, fill=0)
    
                # Celda superior dividida en 4 columnas
                celda_alto = 30
                c.rect(cuadro_x, cuadro_y + cuadro_alto - celda_alto, cuadro_ancho, celda_alto, stroke=1, fill=0)
                columna_ancho = cuadro_ancho / 4
                c.setFont("Helvetica-Bold", 9)
    
                # Encabezados de la celda
                c.drawString(cuadro_x + 10, cuadro_y + cuadro_alto - 15, "Nro Documento")
                c.drawString(cuadro_x + columna_ancho + 10, cuadro_y + cuadro_alto - 15, "Tipo de Nómina")
                c.drawString(cuadro_x + 2 * columna_ancho + 10, cuadro_y + cuadro_alto - 15, "Nombre Empleado")
                c.drawString(cuadro_x + 3 * columna_ancho + 10, cuadro_y + cuadro_alto - 15, "Cédula Empleado")
    
                # Valores de la celda superior (convertidos a cadena)
                c.setFont("Helvetica", 9)
                c.drawString(cuadro_x + 10, cuadro_y + cuadro_alto - 25, str(nomina[20]))  # Nro Documento
                c.drawString(cuadro_x + columna_ancho + 10, cuadro_y + cuadro_alto - 25, str(nomina[16]))  # Tipo de Nómina
                # Limitar el nombre a 21 caracteres y agregar "..." si es más largo
    
                if len(nombre) > 24:
                    nombre = nombre[:21] + "..."
                c.drawString(cuadro_x + 2 * columna_ancho + 10, cuadro_y + cuadro_alto - 25, nombre)  # Nombre Usuario
    
                c.drawString(cuadro_x + 3 * columna_ancho + 10, cuadro_y + cuadro_alto - 25, str(nomina[0]))  # Cédula Usuario
    
                # Contenido de las columnas
                columna_ancho = cuadro_ancho / 3
                contenido_y = cuadro_y + cuadro_alto - celda_alto - 20
    
                # Primera columna
                c.drawString(cuadro_x + 10, contenido_y, f"Prima Alimentación: {str(nomina[4])} Bs")
                c.drawString(cuadro_x + 10, contenido_y - line_spacing, f"Prima Transporte: {str(nomina[2])} Bs")
                c.drawString(cuadro_x + 10, contenido_y - 2 * line_spacing, f"Prima Antigüedad: {str(nomina[6])} Bs")
                c.drawString(cuadro_x + 10, contenido_y - 3 * line_spacing, f"P.F: {str(nomina[10])} Bs")
                c.drawString(cuadro_x + 10, contenido_y - 4 * line_spacing, f"Cuota Sindical: {str(nomina[13])} Bs")
                c.drawString(cuadro_x + 10, contenido_y - 5 * line_spacing, f"Retribuciones: {str(nomina[19])} Bs")
    
                # Segunda columna
                c.drawString(cuadro_x + columna_ancho + 10, contenido_y, f"Prima Hogar: {str(nomina[3])} Bs")
                c.drawString(cuadro_x + columna_ancho + 10, contenido_y - line_spacing, f"Prima Hijo: {str(nomina[5])} Bs")
                c.drawString(cuadro_x + columna_ancho + 10, contenido_y - 2 * line_spacing, f"Prima Profesión: {str(nomina[7])} Bs")
                c.drawString(cuadro_x + columna_ancho + 10, contenido_y - 3 * line_spacing, f"FAOV: {str(nomina[12])} Bs")
                c.drawString(cuadro_x + columna_ancho + 10, contenido_y - 4 * line_spacing, f"Fecha Inicio: {str(nomina[15])}")
    
                # Tercera columna
                c.drawString(cuadro_x + 2 * columna_ancho + 10, contenido_y, f"Asignaciones: {str(nomina[8])} Bs")
                c.drawString(cuadro_x + 2 * columna_ancho + 10, contenido_y - line_spacing, f"Deducciones: {str(nomina[9])} Bs")
                c.drawString(cuadro_x + 2 * columna_ancho + 10, contenido_y - 2 * line_spacing, f"Total Neto: {str(nomina[14])} Bs")
                c.drawString(cuadro_x + 2 * columna_ancho + 10, contenido_y - 3 * line_spacing, f"IVSS: {str(nomina[10])} Bs")
                c.drawString(cuadro_x + 2 * columna_ancho + 10, contenido_y - 4 * line_spacing, f"Fecha Fin: {str(nomina[17])}")
    
                # Actualizar posición para el siguiente cuadro
                cuadro_y -= cuadro_alto + 20  # Espaciado entre cuadros
                contador += 1
    
            c.save()
            QMessageBox.information(None, "Éxito", f"PDF guardado en: {file_path}")
        else:
            QMessageBox.warning(None, "Cancelado", "No se seleccionó ubicación para guardar el archivo.")

    else:
        # Consulta para obtener todas las nóminas
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM nominas")
            nominas = cursor.fetchall()
    
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
    
            # Configuración inicial
            cuadro_x = 50
            margen_superior = 130
            cuadro_y = 720 - margen_superior  # Añadir margen superior de 50 puntos
            cuadro_ancho = 500
            cuadro_alto = 140  # Incluye espacio adicional para la celda superior
            line_spacing = 15
            items_por_pagina = 4  # Número de cuadros por página
            contador = 0
    
            base_dir = os.path.dirname(os.path.abspath(__file__))
            img_path_alcaldia = os.path.join(base_dir, "../images/alcaldia_logo5.png")
            img_path_salud = os.path.join(base_dir, "../images/salud_logo.jpg")
    
            img_width = 80
            img_height = 80
    
            alcaldia_width = 250
            c.drawImage(img_path_salud, 50, 750, img_width, img_height)
            c.drawImage(img_path_alcaldia, 300, 750, alcaldia_width, img_height)
            for nomina in nominas:
                cursor = connection.cursor()
                query = "select concat(name, ' ', lastname) as fullname from employee where cedula = %s;"
                cursor.execute(query, nomina[0])
                nombre = cursor.fetchone()
                nombre = nombre[0]
                # Si se excede el número de cuadros permitidos por página, crear nueva página
                if contador > 0 and contador % items_por_pagina == 0:
                    c.showPage()
                    cuadro_y = 720 - margen_superior  # Reiniciar la posición del cuadro                
                    c.drawImage(img_path_salud, 50, 750, img_width, img_height)
                    c.drawImage(img_path_alcaldia, 300, 750, alcaldia_width, img_height)
    
                if contador == 1:
                    c.drawImage(img_path_salud, 50, 750, img_width, img_height)
                    c.drawImage(img_path_alcaldia, 300, 750, alcaldia_width, img_height)
    
    
                # Dibujar el cuadro principal
                c.rect(cuadro_x, cuadro_y, cuadro_ancho, cuadro_alto, stroke=1, fill=0)
    
                # Celda superior dividida en 4 columnas
                celda_alto = 30
                c.rect(cuadro_x, cuadro_y + cuadro_alto - celda_alto, cuadro_ancho, celda_alto, stroke=1, fill=0)
                columna_ancho = cuadro_ancho / 4
                c.setFont("Helvetica-Bold", 9)
    
                # Encabezados de la celda
                c.drawString(cuadro_x + 10, cuadro_y + cuadro_alto - 15, "Nro Documento")
                c.drawString(cuadro_x + columna_ancho + 10, cuadro_y + cuadro_alto - 15, "Tipo de Nómina")
                c.drawString(cuadro_x + 2 * columna_ancho + 10, cuadro_y + cuadro_alto - 15, "Nombre Empleado")
                c.drawString(cuadro_x + 3 * columna_ancho + 10, cuadro_y + cuadro_alto - 15, "Cédula Empleado")
    
                # Valores de la celda superior (convertidos a cadena)
                c.setFont("Helvetica", 9)
                c.drawString(cuadro_x + 10, cuadro_y + cuadro_alto - 25, str(nomina[20]))  # Nro Documento
                c.drawString(cuadro_x + columna_ancho + 10, cuadro_y + cuadro_alto - 25, str(nomina[16]))  # Tipo de Nómina
                # Limitar el nombre a 21 caracteres y agregar "..." si es más largo
    
                if len(nombre) > 24:
                    nombre = nombre[:21] + "..."
                c.drawString(cuadro_x + 2 * columna_ancho + 10, cuadro_y + cuadro_alto - 25, nombre)  # Nombre Usuario
    
                c.drawString(cuadro_x + 3 * columna_ancho + 10, cuadro_y + cuadro_alto - 25, str(nomina[0]))  # Cédula Usuario
    
                # Contenido de las columnas
                columna_ancho = cuadro_ancho / 3
                contenido_y = cuadro_y + cuadro_alto - celda_alto - 20
    
                # Primera columna
                c.drawString(cuadro_x + 10, contenido_y, f"Prima Alimentación: {str(nomina[4])} Bs")
                c.drawString(cuadro_x + 10, contenido_y - line_spacing, f"Prima Transporte: {str(nomina[2])} Bs")
                c.drawString(cuadro_x + 10, contenido_y - 2 * line_spacing, f"Prima Antigüedad: {str(nomina[6])} Bs")
                c.drawString(cuadro_x + 10, contenido_y - 3 * line_spacing, f"P.F: {str(nomina[10])} Bs")
                c.drawString(cuadro_x + 10, contenido_y - 4 * line_spacing, f"Cuota Sindical: {str(nomina[13])} Bs")
                c.drawString(cuadro_x + 10, contenido_y - 5 * line_spacing, f"Retribuciones: {str(nomina[19])} Bs")
    
                # Segunda columna
                c.drawString(cuadro_x + columna_ancho + 10, contenido_y, f"Prima Hogar: {str(nomina[3])} Bs")
                c.drawString(cuadro_x + columna_ancho + 10, contenido_y - line_spacing, f"Prima Hijo: {str(nomina[5])} Bs")
                c.drawString(cuadro_x + columna_ancho + 10, contenido_y - 2 * line_spacing, f"Prima Profesión: {str(nomina[7])} Bs")
                c.drawString(cuadro_x + columna_ancho + 10, contenido_y - 3 * line_spacing, f"FAOV: {str(nomina[12])} Bs")
                c.drawString(cuadro_x + columna_ancho + 10, contenido_y - 4 * line_spacing, f"Fecha Inicio: {str(nomina[15])}")
    
                # Tercera columna
                c.drawString(cuadro_x + 2 * columna_ancho + 10, contenido_y, f"Asignaciones: {str(nomina[8])} Bs")
                c.drawString(cuadro_x + 2 * columna_ancho + 10, contenido_y - line_spacing, f"Deducciones: {str(nomina[9])} Bs")
                c.drawString(cuadro_x + 2 * columna_ancho + 10, contenido_y - 2 * line_spacing, f"Total Neto: {str(nomina[14])} Bs")
                c.drawString(cuadro_x + 2 * columna_ancho + 10, contenido_y - 3 * line_spacing, f"IVSS: {str(nomina[10])} Bs")
                c.drawString(cuadro_x + 2 * columna_ancho + 10, contenido_y - 4 * line_spacing, f"Fecha Fin: {str(nomina[17])}")
    
                # Actualizar posición para el siguiente cuadro
                cuadro_y -= cuadro_alto + 20  # Espaciado entre cuadros
                contador += 1
    
            c.save()
            QMessageBox.information(None, "Éxito", f"PDF guardado en: {file_path}")
        else:
            QMessageBox.warning(None, "Cancelado", "No se seleccionó ubicación para guardar el archivo.")


