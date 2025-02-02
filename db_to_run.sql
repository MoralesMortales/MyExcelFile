-- MariaDB dump 10.19  Distrib 10.11.6-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: sc_db
-- ------------------------------------------------------
-- Server version	10.11.6-MariaDB-0+deb12u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
  PRIMARY KEY (`cedula`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES
('Asa','Mama',1111111,'Bachiller','Sara','Rarsd','BI','2024-12-12',3,'Clinica del Niño - Juan de Urpin',345,'Mensual',1,3),
('Pepe','Per',1231231,'Bachiller','Portero','Porterobic','BI','2024-12-09',0,'Clinica del Niño - Juan de Urpin',50,'Quincenal',1,12),
('Carlos','Moras',31034826,'TSU','Gerente','Ing sistemas','BI','2024-12-02',0,'Clinica del Niño - Juan de Urpin',100,'Mensual',1,0),
('Carlos','Augusto',50000000,'TSU','Revisador de docmentos','Ingeniero de sistemas','TII','2024-12-01',2,'Clinica del Niño - Juan de Urpin',400,'Mensual',1,0),
('Qwqe','Qweqwe',123123123,'Bachiller','Qeweqweqw','Wqeqwewq','BI','2024-12-10',23,'Clinica del Niño - Juan de Urpin',232,'Quincenal',1,2),
('Wqeqweq','Qweqewwq',323232323,'Bachiller','Sdadadsa','Dsdasdsadad','BI','2024-12-10',23,'Clinica del Niño - Juan de Urpin',2324,'Quincenal',0,44),
('Wqeweqew','Qweqewqe',342332342,'Bachiller','Qweqweqwe','Weqeqwe','BI','2024-12-10',3,'Clinica del Niño - Juan de Urpin',3232,'Quincenal',1,2);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_prev`
--

DROP TABLE IF EXISTS `employee_prev`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee_prev` (
  `cedula` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `nomina_type` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`cedula`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_prev`
--

LOCK TABLES `employee_prev` WRITE;
/*!40000 ALTER TABLE `employee_prev` DISABLE KEYS */;
INSERT INTO `employee_prev` VALUES
(1111111,'Asa Mama','Clinica del Niño - Juan de Urpin','Mensual'),
(31034826,'Carlos Moras','Clinica del Niño - Juan de Urpin','Mensual'),
(50000000,'Carlos Augusto','Clinica del Niño - Juan de Urpin','Mensual');
/*!40000 ALTER TABLE `employee_prev` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historial`
--

DROP TABLE IF EXISTS `historial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `historial` (
  `admin` int(11) DEFAULT NULL,
  `empleado` int(11) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  `action` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historial`
--

LOCK TABLES `historial` WRITE;
/*!40000 ALTER TABLE `historial` DISABLE KEYS */;
/*!40000 ALTER TABLE `historial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nominas`
--

DROP TABLE IF EXISTS `nominas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nominas`
--

LOCK TABLES `nominas` WRITE;
/*!40000 ALTER TABLE `nominas` DISABLE KEYS */;
INSERT INTO `nominas` VALUES
(1111111,345,160,160,160,37.5,10.35,0,872.85,23.06,1.59,12.74,8.73,0,849.79,'2024-12-01','Mensual','2024-12-31',31034826,0,1),
(31034826,100,160,160,160,0,0,20,600,10.15,0.46,3.69,6,0,589.85,'2024-12-01','Mensual','2024-12-31',31034826,0,2),
(50000000,400,160,160,160,0,8,80,5968,76.3,1.85,14.77,59.68,0,5891.7,'2024-12-01','Mensual','2024-12-31',31034826,5000,3);
/*!40000 ALTER TABLE `nominas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nominas_prev`
--

DROP TABLE IF EXISTS `nominas_prev`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nominas_prev`
--

LOCK TABLES `nominas_prev` WRITE;
/*!40000 ALTER TABLE `nominas_prev` DISABLE KEYS */;
/*!40000 ALTER TABLE `nominas_prev` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `cedula` int(11) DEFAULT NULL,
  `clave` varchar(255) DEFAULT NULL,
  `correo` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  KEY `cedula` (`cedula`),
  CONSTRAINT `user_ibfk_1` FOREIGN KEY (`cedula`) REFERENCES `employee` (`cedula`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES
(50000000,'1234','micorreo@dad','Privilegiado'),
(31034826,'1234',',oasdas@','Privilegiado');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-12  3:24:34
