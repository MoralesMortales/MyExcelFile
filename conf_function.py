def python_a_txt(archivo_py, archivo_txt):
    """Convierte un archivo Python a un archivo TXT"""
    print('runinng')
    try:
        with open(archivo_py, "r", encoding="utf-8") as py_file:
            contenido = py_file.read()
        with open(archivo_txt, "w", encoding="utf-8") as txt_file:
            txt_file.write("# Datos del archivo Python convertidos a TXT\n")
            txt_file.write(contenido)
        print(f"Datos del archivo Python guardados en {archivo_txt}")
    except FileNotFoundError:
        print(f"Error: El archivo {archivo_py} no se encuentra.")


def txt_a_python(archivo_txt, archivo_py_actualizado):
    """Convierte un archivo TXT actualizado a un archivo Python"""
    try:
        with open(archivo_txt, "r", encoding="utf-8") as txt_file:
            contenido_txt = txt_file.readlines()

        # Filtrar líneas válidas (sin comentarios ni líneas vacías)
        lineas_validas = [
            linea for linea in contenido_txt if linea.strip() and not linea.strip().startswith("#")
        ]

        with open(archivo_py_actualizado, "w", encoding="utf-8") as py_file:
            py_file.writelines(lineas_validas)

        print(f"Datos actualizados guardados en {archivo_py_actualizado}")
    except FileNotFoundError:
        print(f"Error: El archivo {archivo_txt} no se encuentra.")

#python_a_txt("conf.py","converter.txt")
txt_a_python("converter.txt","conf.py")

import os

def guardar_conf(conf_modificado, archivo_py="conf.py"):
    try:
        # Obtener la ruta completa al archivo en la raíz del proyecto
        ruta_archivo = os.path.join(os.getcwd(), archivo_py)

        with open(ruta_archivo, "w", encoding="utf-8") as py_file:
            # Escribir el encabezado del archivo
            py_file.write("# Archivo de configuración generado automáticamente\n\n")
            
            # Escribir cada clave y valor
            for key, value in vars(conf_modificado).items():
                if not key.startswith("__"):  # Ignorar atributos internos
                    if isinstance(value, str):  # Si es string, agregar comillas simples
                        py_file.write(f"{key} = '{value}'\n")
                    elif isinstance(value, dict):  # Si es diccionario, formatearlo
                        py_file.write(f"{key} = {value}\n")
                    else:  # Otros tipos (números, booleanos, etc.)
                        py_file.write(f"{key} = {value}\n")

        print(f"Archivo {archivo_py} actualizado correctamente en la raíz del proyecto.")
    except Exception as e:
        print(f"Error al guardar el archivo {archivo_py}: {e}")
