from PyQt5.QtWidgets import QFileDialog, QMessageBox
from reportlab.pdfgen import canvas
import pymysql
import conf
import os

def generate_pdf(self):
    print('Generando PDF...')
    connection = pymysql.connect(
        host='localhost',
        user='user_nomina',
        password='12345678',
        database='sc_db',
        charset='utf8'
    )

    # Consulta para obtener todas las nóminas
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM nomina_cestaticket_prev")
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
        margen_superior = 50
        cuadro_y = 720 - margen_superior
        cuadro_ancho = 500
        cuadro_alto = 70
        line_spacing = 15
        items_por_pagina = 8
        contador = 0
        counter = 0

        # Rutas de las imágenes
        base_dir = os.path.dirname(os.path.abspath(__file__))
        img_path_alcaldia = os.path.join(base_dir, "../images/alcaldia_logo5.png")
        img_path_salud = os.path.join(base_dir, "../images/salud_logo.jpg")

        # Tamaño de las imágenes
        img_width = 80
        img_height = 80

        alcaldia_width = 250

        for nomina in nominas:
            counter += 1  # Incrementar el número de documento
            cursor = connection.cursor()
            query = "SELECT CONCAT(name, ' ', lastname) AS fullname FROM employee WHERE cedula = %s;"
            cursor.execute(query, nomina[1])
            nombre = cursor.fetchone()
            if nombre:
                nombre = nombre[0]
            else:
                nombre = "Desconocido"
            print('Nombre obtenido:', nombre)

            # Si se excede el número de cuadros permitidos por página, crear nueva página
            if contador > 0 and contador % items_por_pagina == 0:
                c.showPage()
                cuadro_y = 720 - margen_superior
                # Dibujar las imágenes en la nueva página
                c.drawImage(img_path_salud, 50, 750, img_width, img_height)
                c.drawImage(img_path_alcaldia, 300, 750, alcaldia_width, img_height)

            # Dibujar las imágenes al inicio de la primera página
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
            c.drawString(cuadro_x + 10, cuadro_y + cuadro_alto - 25, str(counter))
            c.drawString(cuadro_x + columna_ancho + 10, cuadro_y + cuadro_alto - 25, str(nomina[5]))
            if len(nombre) > 24:
                nombre = nombre[:21] + '...'

            c.drawString(cuadro_x + 2 * columna_ancho + 10, cuadro_y + cuadro_alto - 25, nombre)
            c.drawString(cuadro_x + 3 * columna_ancho + 10, cuadro_y + cuadro_alto - 25, str(nomina[1]))

            # Contenido de las columnas
            contenido_y = cuadro_y + cuadro_alto - celda_alto - 20
            columna_ancho = cuadro_ancho / 4
            c.drawString(cuadro_x + 10, contenido_y, f"Monto Cestaticket: {str(conf.cesta_ticket)} Bs")
            c.drawString(cuadro_x + columna_ancho + 10, contenido_y, f"Descuentos: {str(nomina[3])} Bs")
            c.drawString(cuadro_x + 2 * columna_ancho + 10, contenido_y, f"Total Neto: {str(nomina[2])} Bs")
            c.drawString(cuadro_x + 3 * columna_ancho + 10, contenido_y, f"Fecha Validez: {str(nomina[4])}")

            cuadro_y -= cuadro_alto + 20
            contador += 1

        c.save()
        QMessageBox.information(None, "Éxito", f"PDF guardado en: {file_path}")
    else:
        QMessageBox.warning(None, "Cancelado", "No se seleccionó ubicación para guardar el archivo.")
