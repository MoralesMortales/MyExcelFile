from PyQt5.QtWidgets import QFileDialog, QMessageBox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
import pymysql
import conf
import os
from datetime import datetime
import num2words
from datetime import datetime

def crear_consta(cedula):
    try:
        connection = pymysql.connect(
            host='localhost',
            user='user_nomina',
            password='12345678',
            database='sc_db',
            charset='utf8'
        )

        with connection.cursor() as cursor:
            cursor.execute('SELECT nomina_type FROM employee WHERE cedula = %s', (cedula,))
            data_base = cursor.fetchall()
            val = data_base[0]
            print(val[0])
            if val[0] == 'Semanal':

                cursor.execute('SELECT nomina_type, CONCAT(name, " ", lastname) AS fullname, contrato, payment, start_date, job FROM employee WHERE cedula = %s', (cedula,))

                data_base = cursor.fetchall()

                nomina_type, name, contrato, sueldo_base, fecha_ini, cargo = data_base[0]
                
                cursor.execute('SELECT prima_transporte, prima_hogar, prima_alimentacion, prima_hijo, prima_antiguedad, prima_profesion FROM nomina_semanal WHERE cedula = %s ORDER BY ABS(DATEDIFF(created, CURDATE())) LIMIT 1;', (cedula,))
                data = cursor.fetchall()
                print('a ',data[0])

                prima_transporte, prima_hogar, prima_alimentacion, prima_hijo, prima_antiguedad, prima_profesion = data[0]
    
                # Calcular el total
                total = sueldo_base + prima_transporte + prima_hogar + prima_alimentacion + prima_hijo + prima_antiguedad + prima_profesion
    
                # Convertir el total a texto
                total_en_letras = num2words.num2words(total, lang='es', to='currency', currency='VES').upper()
                total_en_cesta = num2words.num2words(conf.cesta_ticket, lang='es', to='currency', currency='VES').upper()
    
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
                    c = canvas.Canvas(file_path, pagesize=letter)
                    c.setFont("Helvetica", 10)
    
                    # Rutas de las imágenes
                    base_dir = os.path.dirname(os.path.abspath(__file__))
                    img_path_alcaldia = os.path.join(base_dir, "../images/alcaldia_logo5.png")
                    img_path_salud = os.path.join(base_dir, "../images/salud_logo.jpg")
    
                    img_width = 80
                    img_height = 80
    
                    alcaldia_width = 250
                    # Añadir imagen
                    c.drawImage(img_path_salud, 50, 700, img_width, img_height)
                    c.drawImage(img_path_alcaldia, 300, 700, alcaldia_width, img_height)
    
                    # Agregar el texto "RIF"
                    c.setFont("Helvetica-Bold", 10)
                    
                    c.drawString(50, 670, f"RIF: G-{conf.rif[:8]}-{conf.rif[-1]}")
    
                    # Palabra "CONSTANCIA"
                    c.setFont("Helvetica-Bold", 14)
                    c.drawCentredString(300, 650, "CONSTANCIA")
    
                    # Párrafo inicial
                    c.setFont("Helvetica", 10)
                    print(cedula, 'si')
                    cedula_str = str(cedula)
                    cedula_formateada = ".".join([cedula_str[max(i - 3, 0):i] for i in range(len(cedula_str), 0, -3)][::-1])


                    if len(name) > 20:
                        # Divide el texto en 18 caracteres para la primera línea y el resto para la segunda
                        primera_parte = name[:20]
                        if name[20] != ' ':
                            raya = '-'
                        else:
                            raya = ' '
                        segunda_parte = name[20:]

                        name_formateado = f" "
                        
                        texto_formateado = (
                        f"La Suscrita Directora de Talento Humano Del Instituto Salud Barcelona del Municipio Simón Bolívar del\n\n"
                        f"Estado Anzoátegui, hace constar por medio de la presente que el ciudadano: {primera_parte.upper()}{raya},\n\n"
                        f"{segunda_parte.upper()}, titular de la Cédula de Identidad Nro {cedula_formateada}, presta servicios en este INSTITUTO\n\n")

                        if len(cargo) > 9:
                            texto_formateado += f"desde el {fecha_ini.strftime('%d/%m/%Y')}, ocupando el cargo de {cargo.upper()} como {contrato.upper()}.\n\n"

                        else:
                            texto_formateado += f"desde el {fecha_ini.strftime('%d/%m/%Y')}, ocupando el cargo de {cargo.upper()} como {contrato.upper()}. Devengando lo siguiente."


                    else:
                        name_formateado = name
                        # Texto formateado con el nombre ajustado

                        texto_formateado = (
                        f"La Suscrita Directora de Talento Humano Del Instituto Salud Barcelona del Municipio Simón Bolívar del\n\n"
                        f"Estado Anzoátegui, hace constar por medio de la presente que el ciudadano: {name.upper()},\n\n"
                        f"titular de la Cédula de Identidad Nro {cedula_formateada}, presta servicios en este INSTITUTO\n\n"
                        )

                        # Condicional para agregar una parte del texto dependiendo del largo de 'cargo'
                        if len(cargo) > 9:
                            texto_formateado += f"desde el {fecha_ini.strftime('%d/%m/%Y')}, ocupando el cargo de {cargo.upper()} como {contrato.upper()}\n\n"
                        else:
                            texto_formateado += f"desde el {fecha_ini.strftime('%d/%m/%Y')}, ocupando el cargo de {cargo.upper()} como {contrato.upper()}. Devengando lo siguiente."

                    c.setFont("Helvetica-Bold", 10)

                    # Divide el texto en líneas reales usando saltos de línea (\n)
                    lineas = texto_formateado.splitlines()  

                    # Coordenadas iniciales
                    x, y = 50, 615

                    # Dibuja cada línea ajustando la posición vertical
                    for linea in lineas:
                        c.drawString(x, y, linea.strip())  # Usa .strip() por si hay espacios adicionales
                        y -= 10  # Ajusta la altura (puedes cambiar el valor según el tamaño de fuente)

                    # Dibujar el cuadro de 7 filas y 2 columnas
                    cuadro_x = 165
                    cuadro_y = 520
                    fila_altura = 20
                    columna_ancho = 200
                    c.setFont("Helvetica-Bold", 10)
    
                    nombres = ["SUELDO BÁSICO", "PRIMA POR HOGAR", "PRIMA POR TRANSPORTE", "PRIMA POR ALIMENTACIÓN",
                               "PRIMA POR HIJO", "PROFESIONALIZACIÓN", "TOTAL"]
                    valores = [sueldo_base, prima_hogar, prima_transporte, prima_alimentacion, 
                               prima_hijo, prima_profesion, total]
    
                    for i, nombre in enumerate(nombres):
                        c.drawString(cuadro_x, cuadro_y, nombre)
                        c.drawString(cuadro_x + columna_ancho, cuadro_y, f"{valores[i]:,.2f}")
                        cuadro_y -= fila_altura
    
                    # Párrafo inferior
                    c.setFont("Helvetica", 10)
                    texto_formateado = (
                            f"Generando un sueldo {nomina_type} de {total_en_letras}\n\n"
                            f"Es cancelado un bono de alimento por un monto de {total_en_cesta}\n\n"
                            f"INDEXADO AL VALOR DEL DÓLAR (bs {conf.cesta_ticket}) MENSUAL. El mismo no reviste carácter salarial y presentará\n\n"
                            f"variación mensual según artículo 8 por decreto oficial en Gaceta Nro 6.746 de fecha 01 de Mayo de 2023\n\n")

                    lineas = texto_formateado.splitlines()  

                    # Coordenadas iniciales
                    x, y = 50,cuadro_y - 50 

                    # Dibuja cada línea ajustando la posición vertical
                    for linea in lineas:
                        c.drawString(x, y, linea.strip())  # Usa .strip() por si hay espacios adicionales
                        y -= 10  # Ajusta la altura (puedes cambiar el valor según el tamaño de fuente)

                    fecha_actual = datetime.now()

                    # Extraer día, mes y año
                    dia = fecha_actual.day
                    mes = fecha_actual.strftime("%B")  # Nombre completo del mes en español (requiere configuración de idioma)
                    year = fecha_actual.year

                    c.setFont("Helvetica", 10)
                    texto_formateado = (
                            f"Constancia que se expide a solicitud de parte interesada en la Ciudad de Barcelona a los {dia} del mes \n\n"
                            f"de {mes} del {year}\n\n")

                    lineas = texto_formateado.splitlines()  

                    # Coordenadas iniciales
                    x, y = 50,cuadro_y - 150 

                    # Dibuja cada línea ajustando la posición vertical
                    for linea in lineas:
                        c.drawString(x, y, linea.strip())  # Usa .strip() por si hay espacios adicionales
                        y -= 10  # Ajusta la altura (puedes cambiar el valor según el tamaño de fuente)
                    
                    ancho_pagina = c._pagesize[0]
                    longitud_linea = 150  # Puedes x_inicio = (ancho_pagina - longitud_linea) / 2
                    x_inicio = (ancho_pagina - longitud_linea) / 2
                    x_fin = x_inicio + longitud_linea
                    y_pos = 90  # Altura de la línea (pie de página)ajustar esta longitud según lo necesites

                    # Línea horizontal al pie de página
                    c.line(x_inicio, y_pos, x_fin, y_pos)

                    c.setFont("Helvetica-Bold", 10)
                    c.drawCentredString(300, 70, conf.nombre_licenciada.upper())
                    c.drawCentredString(300, 55, conf.cargo_licenciada.upper())
                    c.drawCentredString(300, 45, 'DEL INSTITUTO SALUD BARCELONA')
                    c.drawCentredString(300, 35, 'SEGÚN RESOLUCIÓN 041-2024')

    
                    # Guardar el PDF
                    c.save()
                    QMessageBox.information(None, "Éxito", "El PDF se ha generado correctamente.")
                
            else:

                print("Entrando al bloque 'else'")

                cursor.execute('SELECT nomina_type, CONCAT(name, " ", lastname) AS fullname, contrato, payment, start_date, job FROM employee WHERE cedula = %s', (cedula,))
                data_base = cursor.fetchall()
                nomina_type, name, contrato, sueldo_base, fecha_ini, cargo = data_base[0]
                
                cursor.execute('SELECT prima_transporte, prima_hogar, prima_alimentacion, prima_hijo, prima_antiguedad, prima_profesion FROM nominas_prev WHERE cedula = %s ORDER BY ABS(DATEDIFF(created, CURDATE())) LIMIT 1;', (cedula,))
                data = cursor.fetchall()
                print('a ',data[0])

                prima_transporte, prima_hogar, prima_alimentacion, prima_hijo, prima_antiguedad, prima_profesion = data[0]
    
                # Calcular el total
                total = sueldo_base + prima_transporte + prima_hogar + prima_alimentacion + prima_hijo + prima_antiguedad + prima_profesion
    
                # Convertir el total a texto
                total_en_letras = num2words.num2words(total, lang='es', to='currency', currency='VES').upper()
                total_en_cesta = num2words.num2words(conf.cesta_ticket, lang='es', to='currency', currency='VES').upper()
    
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
                    c = canvas.Canvas(file_path, pagesize=letter)
                    c.setFont("Helvetica", 10)
    
                    # Rutas de las imágenes
                    base_dir = os.path.dirname(os.path.abspath(__file__))
                    img_path_alcaldia = os.path.join(base_dir, "../images/alcaldia_logo5.png")
                    img_path_salud = os.path.join(base_dir, "../images/salud_logo.jpg")
    
                    img_width = 80
                    img_height = 80
    
                    alcaldia_width = 250
                    # Añadir imagen
                    c.drawImage(img_path_salud, 50, 700, img_width, img_height)
                    c.drawImage(img_path_alcaldia, 300, 700, alcaldia_width, img_height)
    
                    # Agregar el texto "RIF"
                    c.setFont("Helvetica-Bold", 10)
                    
                    c.drawString(50, 670, f"RIF: G-{conf.rif[:8]}-{conf.rif[-1]}")
    
                    # Palabra "CONSTANCIA"
                    c.setFont("Helvetica-Bold", 14)
                    c.drawCentredString(300, 650, "CONSTANCIA")
    
                    # Párrafo inicial
                    c.setFont("Helvetica", 10)
                    print(cedula, 'si')
                    cedula_str = str(cedula)
                    cedula_formateada = ".".join([cedula_str[max(i - 3, 0):i] for i in range(len(cedula_str), 0, -3)][::-1])


                    if len(name) > 20:
                        # Divide el texto en 18 caracteres para la primera línea y el resto para la segunda
                        primera_parte = name[:20]
                        if name[20] != ' ':
                            raya = '-'
                        else:
                            raya = ' '
                        segunda_parte = name[20:]

                        name_formateado = f" "
                        
                        texto_formateado = (
                        f"La Suscrita Directora de Talento Humano Del Instituto Salud Barcelona del Municipio Simón Bolívar del\n\n"
                        f"Estado Anzoátegui, hace constar por medio de la presente que el ciudadano: {primera_parte.upper()}{raya},\n\n"
                        f"{segunda_parte.upper()}, titular de la Cédula de Identidad Nro {cedula_formateada}, presta servicios en este INSTITUTO\n\n")

                        if len(cargo) > 9:
                            texto_formateado += f"desde el {fecha_ini.strftime('%d/%m/%Y')}, ocupando el cargo de {cargo.upper()} como {contrato.upper()}.\n\n"

                        else:
                            texto_formateado += f"desde el {fecha_ini.strftime('%d/%m/%Y')}, ocupando el cargo de {cargo.upper()} como {contrato.upper()}. Devengando lo siguiente."


                    else:
                        name_formateado = name
                        # Texto formateado con el nombre ajustado

                        texto_formateado = (
                        f"La Suscrita Directora de Talento Humano Del Instituto Salud Barcelona del Municipio Simón Bolívar del\n\n"
                        f"Estado Anzoátegui, hace constar por medio de la presente que el ciudadano: {name.upper()},\n\n"
                        f"titular de la Cédula de Identidad Nro {cedula_formateada}, presta servicios en este INSTITUTO\n\n"
                        )

                        # Condicional para agregar una parte del texto dependiendo del largo de 'cargo'
                        if len(cargo) > 9:
                            texto_formateado += f"desde el {fecha_ini.strftime('%d/%m/%Y')}, ocupando el cargo de {cargo.upper()} como {contrato.upper()}\n\n"
                        else:
                            texto_formateado += f"desde el {fecha_ini.strftime('%d/%m/%Y')}, ocupando el cargo de {cargo.upper()} como {contrato.upper()}. Devengando lo siguiente."

                    c.setFont("Helvetica-Bold", 10)

                    # Divide el texto en líneas reales usando saltos de línea (\n)
                    lineas = texto_formateado.splitlines()  

                    # Coordenadas iniciales
                    x, y = 50, 615

                    # Dibuja cada línea ajustando la posición vertical
                    for linea in lineas:
                        c.drawString(x, y, linea.strip())  # Usa .strip() por si hay espacios adicionales
                        y -= 10  # Ajusta la altura (puedes cambiar el valor según el tamaño de fuente)

                    # Dibujar el cuadro de 7 filas y 2 columnas
                    cuadro_x = 165
                    cuadro_y = 520
                    fila_altura = 20
                    columna_ancho = 200
                    c.setFont("Helvetica-Bold", 10)
    
                    nombres = ["SUELDO BÁSICO", "PRIMA POR HOGAR", "PRIMA POR TRANSPORTE", "PRIMA POR ALIMENTACIÓN",
                               "PRIMA POR HIJO", "PROFESIONALIZACIÓN", "TOTAL"]
                    valores = [sueldo_base, prima_hogar, prima_transporte, prima_alimentacion, 
                               prima_hijo, prima_profesion, total]
    
                    for i, nombre in enumerate(nombres):
                        c.drawString(cuadro_x, cuadro_y, nombre)
                        c.drawString(cuadro_x + columna_ancho, cuadro_y, f"{valores[i]:,.2f} Bs")
                        cuadro_y -= fila_altura
    
                    # Párrafo inferior
                    c.setFont("Helvetica", 10)
                    texto_formateado = (
                            f"Generando un sueldo {nomina_type} de {total_en_letras}\n\n"
                            f"Es cancelado un bono de alimento por un monto de {total_en_cesta}\n\n"
                            f"INDEXADO AL VALOR DEL DÓLAR (bs {conf.cesta_ticket}) MENSUAL. El mismo no reviste carácter salarial y presentará\n\n"
                            f"variación mensual según artículo 8 por decreto oficial en Gaceta Nro 6.746 de fecha 01 de Mayo de 2023\n\n")

                    lineas = texto_formateado.splitlines()  

                    # Coordenadas iniciales
                    x, y = 50,cuadro_y - 50 

                    # Dibuja cada línea ajustando la posición vertical
                    for linea in lineas:
                        c.drawString(x, y, linea.strip())  # Usa .strip() por si hay espacios adicionales
                        y -= 10  # Ajusta la altura (puedes cambiar el valor según el tamaño de fuente)

                    fecha_actual = datetime.now()

                    # Extraer día, mes y año
                    dia = fecha_actual.day
                    mes = fecha_actual.strftime("%B")  # Nombre completo del mes en español (requiere configuración de idioma)
                    year = fecha_actual.year

                    c.setFont("Helvetica", 10)
                    texto_formateado = (
                            f"Constancia que se expide a solicitud de parte interesada en la Ciudad de Barcelona a los {dia} del mes \n\n"
                            f"de {mes} del {year}\n\n")

                    lineas = texto_formateado.splitlines()  

                    # Coordenadas iniciales
                    x, y = 50,cuadro_y - 150 

                    # Dibuja cada línea ajustando la posición vertical
                    for linea in lineas:
                        c.drawString(x, y, linea.strip())  # Usa .strip() por si hay espacios adicionales
                        y -= 10  # Ajusta la altura (puedes cambiar el valor según el tamaño de fuente)
                    
                    ancho_pagina = c._pagesize[0]
                    longitud_linea = 150  # Puedes x_inicio = (ancho_pagina - longitud_linea) / 2
                    x_inicio = (ancho_pagina - longitud_linea) / 2
                    x_fin = x_inicio + longitud_linea
                    y_pos = 90  # Altura de la línea (pie de página)ajustar esta longitud según lo necesites

                    # Línea horizontal al pie de página
                    c.line(x_inicio, y_pos, x_fin, y_pos)

                    c.setFont("Helvetica-Bold", 10)
                    c.drawCentredString(300, 70, conf.nombre_licenciada.upper())
                    c.drawCentredString(300, 55, conf.cargo_licenciada.upper())
                    c.drawCentredString(300, 45, 'DEL INSTITUTO SALUD BARCELONA')
                    c.drawCentredString(300, 35, 'SEGÚN RESOLUCIÓN 041-2024')

    
                    # Guardar el PDF
                    c.save()
                    QMessageBox.information(None, "Éxito", "El PDF se ha generado correctamente.")
                
        
    except pymysql.MySQLError as e:
        QMessageBox.critical(None, "Error", f"No tienes ninguna nomina creada con este empleado!")

    except Exception as e:
        QMessageBox.critical(None, "Error", f"No tienes ninguna nomina creada con este empleado!")
