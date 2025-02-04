import pymysql
from pymysql import MySQLError
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from py_functions.login_window import LoginWindow


def initialize_db():
    try:
        connection = pymysql.connect(
            host="localhost", user='user_nomina', password='12345678', charset="utf8"
        )
        connection_cursor = connection.cursor()

        # Verificar si la base de daos 'sc_db' existe
        connection_cursor.execute("SHOW DATABASES;")
        databases = [db[0] for db in connection_cursor.fetchall()]

        if "sc_db" not in databases:
            print("La base de datos 'sc_db' no existe. Creándola...")

            connection_cursor.execute("CREATE DATABASE sc_db;")
            print("La base de datos 'sc_db' ha sido creada.")

            connection_cursor.execute(
                "GRANT ALL PRIVILEGES ON sc_db.* TO 'root'@'localhost' IDENTIFIED BY 'root';"
            )
            connection_cursor.execute("FLUSH PRIVILEGES;")
            connection.commit()

        else:
            print("La base de datos 'sc_db' ya existe.")

        # Conectar a la base de datos para crear tablas
        connection.close()
        connection = pymysql.connect(
            host="localhost",
            user='user_nomina',
            password='12345678',
            database="sc_db",
            charset="utf8",
        )
        connection_cursor = connection.cursor()

        # Lista de sentencias SQL separadas
        sql_statements = [
            """CREATE TABLE `employee` (
  `name` varchar(255) DEFAULT NULL,
  `lastname` varchar(255) DEFAULT NULL,
  `cedula` int(11) NOT NULL,
  `academic_level` varchar(255) DEFAULT NULL,
  `job` varchar(255) DEFAULT NULL,
  `proffesion` varchar(255) DEFAULT NULL,
  `job_onapre` varchar(255) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `service_years` int(50) DEFAULT NULL,
  `job_location` text DEFAULT NULL,
  `payment` double DEFAULT NULL,
  `nomina_type` varchar(255) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `children` int(11) DEFAULT NULL,
  `nro_cuenta` varchar(255) DEFAULT NULL,
  `tipo_cuenta` varchar(255) DEFAULT NULL,
  `nro_telefono` varchar(255) DEFAULT NULL,
  `contrato` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`cedula`)
);""",
            """INSERT INTO `employee` VALUES
('Carlos','Moras',31034826,'TSU','Gerente','Ing sistemas','BI','2024-12-02',0,'Clinica del Niño - Juan de Urpin',100,'Mensual',1,0,'333333333333333333','00','04128816267','Obrero Fijo');""",
            """CREATE TABLE `employee_prev` (
  `cedula` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `nomina_type` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`cedula`)
);""",
            """CREATE TABLE `historial` (
  `admin` int(11) DEFAULT NULL,
  `empleado` int(11) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  `action` varchar(255) DEFAULT NULL
);""",
            """CREATE TABLE `lista_nominas` (
  `nro` int(11) NOT NULL AUTO_INCREMENT,
  `cuenta` varchar(255) DEFAULT NULL,
  `total_neto` double DEFAULT NULL,
  `total_deducciones` double DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `tipo` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`nro`)
);""",
            """CREATE TABLE `nomina_cestaticket` (
  `nombre` varchar(255) DEFAULT NULL,
  `cedula` int(11) DEFAULT NULL,
  `total_neto` double DEFAULT NULL,
  `descuentos` double DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL
);""",
            """CREATE TABLE `nomina_cestaticket_prev` (
  `nombre` varchar(255) DEFAULT NULL,
  `cedula` int(11) DEFAULT NULL,
  `total_neto` double DEFAULT NULL,
  `descuentos` double DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL
);""",
            """CREATE TABLE `nomina_semanal` (
  `cedula` int(11) DEFAULT NULL,
  `sueldo_base` double DEFAULT NULL,
  `prima_transporte` double DEFAULT NULL,
  `prima_hogar` double DEFAULT NULL,
  `prima_alimentacion` double DEFAULT NULL,
  `prima_hijo` double DEFAULT NULL,
  `prima_antiguedad` double DEFAULT NULL,
  `prima_profesion` double DEFAULT NULL,
  `asignaciones` double DEFAULT NULL,
  `deducciones_T` double DEFAULT NULL,
  `pf` double DEFAULT NULL,
  `ivss` double DEFAULT NULL,
  `faov` double DEFAULT NULL,
  `cuota_sindical` double DEFAULT NULL,
  `total_neto` double DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `type` varchar(40) DEFAULT NULL,
  `fecha_fin` date DEFAULT NULL,
  `made_by` int(11) DEFAULT NULL,
  `retributions` int(11) DEFAULT NULL,
  `n` int(11) NOT NULL AUTO_INCREMENT,
  `n_semana` int(11) DEFAULT NULL,
  `created` date DEFAULT NULL,
  PRIMARY KEY (`n`)
);""",
            """CREATE TABLE `nomina_semanal_prev` (
  `cedula` int(11) DEFAULT NULL,
  `sueldo_base` double DEFAULT NULL,
  `prima_transporte` double DEFAULT NULL,
  `prima_hogar` double DEFAULT NULL,
  `prima_alimentacion` double DEFAULT NULL,
  `prima_hijo` double DEFAULT NULL,
  `prima_antiguedad` double DEFAULT NULL,
  `prima_profesion` double DEFAULT NULL,
  `asignaciones` double DEFAULT NULL,
  `deducciones_T` double DEFAULT NULL,
  `pf` double DEFAULT NULL,
  `ivss` double DEFAULT NULL,
  `faov` double DEFAULT NULL,
  `cuota_sindical` double DEFAULT NULL,
  `total_neto` double DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `type` varchar(40) DEFAULT NULL,
  `fecha_fin` date DEFAULT NULL,
  `made_by` int(11) DEFAULT NULL,
  `retributions` int(11) DEFAULT NULL,
  `n` int(11) NOT NULL AUTO_INCREMENT,
  `n_semana` int(11) DEFAULT NULL,
  PRIMARY KEY (`n`)
);""",
            """CREATE TABLE `nominas` (
  `cedula` int(11) DEFAULT NULL,
  `sueldo_base` double DEFAULT NULL,
  `prima_transporte` double DEFAULT NULL,
  `prima_hogar` double DEFAULT NULL,
  `prima_alimentacion` double DEFAULT NULL,
  `prima_hijo` double DEFAULT NULL,
  `prima_antiguedad` double DEFAULT NULL,
  `prima_profesion` double DEFAULT NULL,
  `asignaciones` double DEFAULT NULL,
  `deducciones_T` double DEFAULT NULL,
  `pf` double DEFAULT NULL,
  `ivss` double DEFAULT NULL,
  `faov` double DEFAULT NULL,
  `cuota_sindical` double DEFAULT NULL,
  `total_neto` double DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `type` varchar(40) DEFAULT NULL,
  `fecha_fin` date DEFAULT NULL,
  `made_by` int(11) DEFAULT NULL,
  `retributions` int(11) DEFAULT NULL,
  `n` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`n`)
);""",
            """CREATE TABLE `nominas_prev` (
  `cedula` int(11) DEFAULT NULL,
  `sueldo_base` double DEFAULT NULL,
  `prima_transporte` double DEFAULT NULL,
  `prima_hogar` double DEFAULT NULL,
  `prima_alimentacion` double DEFAULT NULL,
  `prima_hijo` double DEFAULT NULL,
  `prima_antiguedad` double DEFAULT NULL,
  `prima_profesion` double DEFAULT NULL,
  `asignaciones` double DEFAULT NULL,
  `deducciones_T` double DEFAULT NULL,
  `pf` double DEFAULT NULL,
  `ivss` double DEFAULT NULL,
  `faov` double DEFAULT NULL,
  `cuota_sindical` double DEFAULT NULL,
  `total_neto` double DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `type` varchar(40) DEFAULT NULL,
  `fecha_fin` date DEFAULT NULL,
  `made_by` int(11) DEFAULT NULL,
  `retributions` int(11) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` date DEFAULT NULL,
  PRIMARY KEY (`id`)
);""",
            """CREATE TABLE `user` (
  `cedula` int(11) DEFAULT NULL,
  `clave` varchar(255) DEFAULT NULL,
  `correo` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  KEY `cedula` (`cedula`),
  CONSTRAINT `user_ibfk_1` FOREIGN KEY (`cedula`) REFERENCES `employee` (`cedula`)
);""",
            """INSERT INTO `user` VALUES
(31034826,'1234','moralesyaguilera@gmail.com','Privilegiado');""",
        ]

        for statement in sql_statements:
            connection_cursor.execute(statement)

        print("Las tablas y datos han sido creados correctamente.")
        connection.commit()

    except MySQLError as e:
        print(f"Error al configurar la base de datos: {e}")
    finally:
        if connection_cursor:
            connection_cursor.close()
        else:
            print("error dude")
        if connection:
            connection.close()
        else:
            print("error 2 dude")


initialize_db()

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("images/logo8.png"))
    window = LoginWindow()
    window.showMaximized()

    sys.exit(app.exec())
