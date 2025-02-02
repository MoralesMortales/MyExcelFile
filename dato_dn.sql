CREATE TABLE `employee` (
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
  PRIMARY KEY (`cedula`)
);

INSERT INTO `employee` VALUES
('Asa','Mama',1111111,'Bachiller','Sara','Rarsd','BI','2024-12-12',3,'Clinica del Niño - Juan de Urpin',345,'Mensual',1,3,NULL,NULL,NULL),
('Pepe','Per',1231231,'Bachiller','Portero','Porterobic','BI','2024-12-09',0,'Clinica del Niño - Juan de Urpin',50,'Quincenal',1,12,NULL,NULL,NULL),
('Carlos','Moras',31034826,'TSU','Gerente','Ing sistemas','BI','2024-12-02',0,'Clinica del Niño - Juan de Urpin',100,'Mensual',1,0,'333333333333333333','00',''),
('Carlos','Augusto',50000000,'TSU','Revisador de docmentos','Ingeniero de sistemas','TII','2024-12-01',2,'Clinica del Niño - Juan de Urpin',400,'Mensual',1,0,NULL,NULL,NULL),
('Pdro','Morta',123123122,'Especialista','Qeqweqeq','Qweqwe','BI','2024-01-01',12,'Clinica del Niño - Juan de Urpin',1234,'Quincenal',1,2,NULL,NULL,NULL),
('Qwqe','Qweqwe',123123123,'Bachiller','Qeweqweqw','Wqeqwewq','BI','2024-12-10',23,'Clinica del Niño - Juan de Urpin',232,'Quincenal',1,2,'33333333333333333333','00','None'),
('Asas adsdasd asdadsa','Asdads adasdad',233423423,'Especialista','Werwerwer','Werwerwerwerwr','BII','2024-01-01',45,'Clinica Movil - Barcelona',400,'Quincenal',1,4,'55555555555555555555','00','04128816267'),
('Aerawerr','Sefsdfsafds',333333333,'Bachiller','Jbxkjfbsd','Daisdhaiduh','BI','2025-10-15',4,'Clinica del Niño - Juan de Urpin',345,'Quincenal',1,3,'12312312312312312313','00',NULL),
('Wqeweqew','Qweqewqe',342332342,'Bachiller','Qweqweqwe','Weqeqwe','BI','2024-12-10',3,'Clinica del Niño - Juan de Urpin',3232,'Quincenal',1,2,'44444444444444444444','00','None');

CREATE TABLE `employee_prev` (
  `cedula` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `nomina_type` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`cedula`)
);

INSERT INTO `employee_prev` VALUES
(1111111,'Asa Mama','Clinica del Niño - Juan de Urpin','Mensual'),
(31034826,'Carlos Moras','Clinica del Niño - Juan de Urpin','Mensual'),
(50000000,'Carlos Augusto','Clinica del Niño - Juan de Urpin','Mensual');

CREATE TABLE `historial` (
  `admin` int(11) DEFAULT NULL,
  `empleado` int(11) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  `action` varchar(255) DEFAULT NULL
);

INSERT INTO `historial` VALUES
(1231231,31034826,'2024-12-12','21:58:03','Crear Nomina'),
(123123123,31034826,'2024-12-12','21:58:03','Crear Nomina'),
(323232323,31034826,'2024-12-12','21:58:03','Crear Nomina'),
(342332342,31034826,'2024-12-12','21:58:03','Crear Nomina'),
(1231231,31034826,'2024-12-12','21:59:10','Crear Nomina'),
(123123123,31034826,'2024-12-12','21:59:10','Crear Nomina'),
(323232323,31034826,'2024-12-12','21:59:10','Crear Nomina'),
(342332342,31034826,'2024-12-12','21:59:10','Crear Nomina');

CREATE TABLE `lista_nominas` (
  `nro` int(11) NOT NULL AUTO_INCREMENT,
  `cuenta` varchar(255) DEFAULT NULL,
  `total_neto` double DEFAULT NULL,
  `total_deducciones` double DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  PRIMARY KEY (`nro`)
);

CREATE TABLE `nominas` (
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
  PRIMARY KEY (`n`),
  KEY `cedula` (`cedula`),
  KEY `fk_nomina_cedula` (`made_by`)
);

INSERT INTO `nominas` VALUES
(1111111,345,160,160,160,37.5,10.35,0,872.85,23.06,1.59,12.74,8.73,0,849.79,'2024-12-01','Mensual','2024-12-31',31034826,0,1),
(31034826,100,160,160,160,0,0,20,600,10.15,0.46,3.69,6,0,589.85,'2024-12-01','Mensual','2024-12-31',31034826,0,2),
(50000000,400,160,160,160,0,8,80,968,26.3,1.85,14.77,9.68,0,941.7,'2024-12-01','Mensual','2024-12-31',31034826,0,3);

CREATE TABLE `nominas_prev` (
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
  PRIMARY KEY (`id`)
);
CREATE TABLE `user` (
  `cedula` int(11) DEFAULT NULL,
  `clave` varchar(255) DEFAULT NULL,
  `correo` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  KEY `cedula` (`cedula`),
  CONSTRAINT `user_ibfk_1` FOREIGN KEY (`cedula`) REFERENCES `employee` (`cedula`)
);

INSERT INTO `user` VALUES
(50000000,'1234','micorreo@dad','Privilegiado'),
(31034826,'1234',',oasdas@','Privilegiado');
