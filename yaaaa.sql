-- MariaDB dump 10.19  Distrib 10.11.6-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: sc_db
-- ------------------------------------------------------
-- Server version	10.11.6-MariaDB-0+deb12u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
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
  `nro_cuenta` varchar(255) DEFAULT NULL,
  `tipo_cuenta` varchar(255) DEFAULT NULL,
  `nro_telefono` varchar(255) DEFAULT NULL,
  `contrato` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`cedula`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES
('Sdsadad','W',1,'Bachiller','Ert','Er','BI','2024-01-01',1,'1',1,'Quincenal',1,1,'14555555555555555555','00','1',NULL),
('Ww','W',2,'Bachiller','W','We','BI','2024-01-01',33,'E',3333,'Quincenal',1,2,'22222222222222222222','00','222222222222','Empleado Fijo'),
('Asa','Mama',1111111,'Bachiller','Sara','Rarsd','BI','2024-12-12',3,'Clinica del niño - juan de urpin',345,'Mensual',1,3,'80000000000000000000','00','None',NULL),
('Pepe','Per',1231231,'Bachiller','Portero','Porterobic','BI','2024-12-09',0,'Clinica del Niño - Juan de Urpin',50,'Quincenal',1,12,NULL,NULL,NULL,NULL),
('Elizabeth Del Carmen','Bolivar Galvis',15050177,'Bachiller','X cargo','X profesion','BI','2024-01-01',14,'x lugar',88.5,'Quincenal',1,2,'10201020102010201020','00','041518181871',NULL),
('Carlos','Moras',31034826,'TSU','Gerente','Ing sistemas','BI','2024-12-02',0,'Clinica del Niño - Juan de Urpin',100,'Mensual',1,0,'333333333333333333','00','',NULL),
('Carlos','Augusto',50000000,'TSU','Revisador de docmentos','Ingeniero de sistemas','TII','2024-12-01',2,'Clinica del niño - juan de urpin',400,'Mensual',1,0,'56666666666666666666','00','None',NULL),
('R','R',89684444,'Bachiller','R','R','BI','2025-01-02',2,'r',2,'Quincenal',1,2,'33222222222222222222','00','2',NULL),
('W','W',111111111,'Bachiller','Sssssss','S','BI','2024-01-01',2,'s',222,'Quincenal',1,2,'11111111111111111111','00','222222222222',NULL),
('Pepito','Ik',111111113,'Bachiller','E','E','BI','2024-01-01',2,'e',222,'Semanal',1,2,'33333333333333333333','00','222222222222',NULL),
('X','X',121212222,'TSU','R','R','BI','2024-01-01',4,'r',4,'Quincenal',1,4,'33333333333333333333','00','4',NULL),
('Pdro','Morta',123123122,'Especialista','Qeqweqeq','Qweqwe','BI','2024-01-01',12,'Clinica del Niño - Juan de Urpin',1234,'Quincenal',1,2,NULL,NULL,NULL,NULL),
('Qwqe','Qweqwe',123123123,'Bachiller','Qeweqweqw','Wqeqwewq','BI','2024-12-10',23,'Clinica del Niño - Juan de Urpin',232,'Quincenal',1,2,'33333333333333333333','00','None',NULL),
('E','E',212111111,'Bachiller','E','E','BI','2025-01-02',3,'e',3,'Quincenal',1,3,'22222222222222222222','00','3',NULL),
('Sasa','Sasa',222222222,'Bachiller','E','E','BI','2024-01-01',33,'e',333,'Semanal',1,3,'22222222222222222222','00','232222222222',NULL),
('Pepita','W',232333333,'Bachiller','Eeeeeee','E','BI','2024-01-01',3,'e',3,'Quincenal',1,3,'33333333333333333333','00','333333333333',NULL),
('D','Dw',233333233,'Bachiller','E','E','BI','2025-01-02',98,'e',8787887,'Quincenal',1,9,'23333333323333333323','00','777777777777',NULL),
('Rqwe','Qwer',233333332,'Bachiller','D','D','BI','2025-01-02',3,'d',12,'Quincenal',1,32,'23333333323333333322','00','131222222222',NULL),
('Dd','D',233333333,'Bachiller','E','E','BI','2024-01-01',4,'e',343,'Quincenal',1,2,'23333333323333333323','00','244444444444',NULL),
('Asas adsdasd asdadsa','Asdads adasdad',233423423,'Especialista','Werwerwer','Werwerwerwerwr','BII','2024-01-01',45,'Clinica Movil - Barcelona',400,'Quincenal',1,4,'55555555555555555555','00','04128816267',NULL),
('R','R',234234444,'Bachiller','R','R','BI','2025-01-02',2,'r',2,'Quincenal',1,52,'44444444444444444444','00','535555555555',NULL),
('R','R',321111111,'Bachiller','E','E','BI','2025-01-29',2,'e',2,'Quincenal',1,2,'22222222222222222222','00','2',NULL),
('R','R',333333322,'Bachiller','E','E','BI','2025-01-02',2,'e',2,'Quincenal',1,2,'33333333333333333333','00','2',NULL),
('Aerawerr','Sefsdfsafds',333333333,'Bachiller','Jbxkjfbsd','Daisdhaiduh','BI','2025-10-15',4,'Clinica del Niño - Juan de Urpin',345,'Quincenal',1,3,'12312312312312312313','00',NULL,NULL),
('Eeee','Eeee',333333334,'Bachiller','S','S','BI','2024-01-01',3,'s',344,'Quincenal',1,3,'33333333333333333333','00','344334433443',NULL),
('R','R',333334234,'Bachiller','R','R','BI','2025-01-02',3,'r',3,'Quincenal',1,3,'22222222222222222222','00','3',NULL),
('T','T',341111111,'Bachiller','T','T','BI','2025-01-02',3,'t',3,'Quincenal',1,3,'34444444444444444444','00','3',NULL),
('Wqeweqew','Qweqewqe',342332342,'Bachiller','Qweqweqwe','Weqeqwe','BI','2024-12-10',3,'Clinica del niño - juan de urpin',3232,'Quincenal',0,2,'44444444444444444444','00','102454545454',NULL),
('R','R',343433333,'Bachiller','R','R','BI','2024-01-01',43,'r',3,'Quincenal',1,4,'33333333333333333333','00','333333333333',NULL),
('F','F',343434343,'Bachiller','R','R','BI','2024-01-01',3,'r',3,'Quincenal',1,3,'44444444444444444444','00','3',NULL),
('Dada','Sded',343434355,'Bachiller','Ew','Wer','BI','2024-01-01',234,'we',234,'Semanal',1,2,'23333333333333333333','00','233333333333',NULL),
('Rtr','R',344444444,'Bachiller','E','E','BI','2025-01-02',2,'d',23233232,'Quincenal',1,2,'22333333332333333332','00','222222222222',NULL),
('Deeeeedq','De',345222222,'Bachiller','R','R','BI','2024-01-01',4,'R',4,'Mensual',1,4,'33333333333333333333','00','444444444444',NULL),
('Y','Y',345444444,'Bachiller','T','T','BI','2025-01-02',4,'t',4,'Quincenal',1,4,'44444444444444444444','00','4',NULL),
('E','E',421333333,'Bachiller','E','E','BI','2025-01-02',1,'e',1,'Quincenal',1,1,'31233333333333333333','00','1',NULL),
('V','V',444444444,'Bachiller','W','W','BI','2025-01-02',8,'w',898989,'Quincenal',1,2,'23111111111111333333','00','898888888888',NULL),
('E','E',444444449,'Bachiller','E','E','BI','2025-01-02',1,'e',1,'Quincenal',1,1,'44444444444444444444','00','1',NULL),
('Ttttttttttttttttttttttt','T',453534533,'Bachiller','T','G','BI','2025-01-02',4,'g',4,'Quincenal',1,4,'44444444444444444444','00','4',NULL),
('Ggggggggggggggggggggg','Gg',454535345,'Bachiller','Tr','T','BI','2025-01-02',3,'t',3,'Quincenal',1,3,'44444444444444444444','00','333333333333',NULL),
('U','U',999999999,'Bachiller','U','U','BI','2024-01-01',9,'u',999,'Semanal',1,9,'99999999999999999999','00','999999999999',NULL);
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_prev`
--

LOCK TABLES `employee_prev` WRITE;
/*!40000 ALTER TABLE `employee_prev` DISABLE KEYS */;
INSERT INTO `employee_prev` VALUES
(111111113,'Pepito Ik','e','Semanal'),
(222222222,'Sasa Sasa','e','Semanal'),
(343434355,'Dada Sded','we','Semanal'),
(999999999,'U U','u','Semanal');
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historial`
--

LOCK TABLES `historial` WRITE;
/*!40000 ALTER TABLE `historial` DISABLE KEYS */;
INSERT INTO `historial` VALUES
(31034826,333333334,'2024-12-30','12:10:30','Crear Nomina Cestaticket'),
(31034826,1,'2024-12-30','12:49:05','Crear Nomina Cestaticket'),
(31034826,2,'2024-12-30','12:49:05','Crear Nomina Cestaticket'),
(31034826,1111111,'2024-12-30','12:49:05','Crear Nomina Cestaticket'),
(31034826,1231231,'2024-12-30','12:49:05','Crear Nomina Cestaticket'),
(31034826,31034826,'2024-12-30','12:49:05','Crear Nomina Cestaticket'),
(31034826,50000000,'2024-12-30','12:49:05','Crear Nomina Cestaticket'),
(31034826,111111111,'2024-12-30','12:49:05','Crear Nomina Cestaticket'),
(31034826,123123122,'2024-12-30','12:49:05','Crear Nomina Cestaticket'),
(31034826,123123123,'2024-12-30','12:49:05','Crear Nomina Cestaticket'),
(31034826,233423423,'2024-12-30','12:49:05','Crear Nomina Cestaticket'),
(31034826,333333333,'2024-12-30','12:49:05','Crear Nomina Cestaticket'),
(31034826,333333334,'2024-12-30','12:49:05','Crear Nomina Cestaticket'),
(31034826,1,'2024-12-31','17:58:02','Crear Nomina Cestaticket'),
(31034826,2,'2024-12-31','17:58:02','Crear Nomina Cestaticket'),
(31034826,1111111,'2024-12-31','17:58:02','Crear Nomina Cestaticket'),
(31034826,1231231,'2024-12-31','17:58:02','Crear Nomina Cestaticket'),
(31034826,31034826,'2024-12-31','17:58:02','Crear Nomina Cestaticket'),
(31034826,50000000,'2024-12-31','17:58:02','Crear Nomina Cestaticket'),
(31034826,111111111,'2024-12-31','17:58:02','Crear Nomina Cestaticket'),
(31034826,123123122,'2024-12-31','17:58:02','Crear Nomina Cestaticket'),
(31034826,123123123,'2024-12-31','17:58:02','Crear Nomina Cestaticket'),
(31034826,233423423,'2024-12-31','17:58:02','Crear Nomina Cestaticket'),
(31034826,333333333,'2024-12-31','17:58:02','Crear Nomina Cestaticket'),
(31034826,333333334,'2024-12-31','17:58:03','Crear Nomina Cestaticket'),
(31034826,1,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,2,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,1111111,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,1231231,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,31034826,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,50000000,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,111111111,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,123123122,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,123123123,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,233423423,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,333333333,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,333333334,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,1,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,2,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,1111111,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,1231231,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,31034826,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,50000000,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,111111111,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,123123122,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,123123123,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,233423423,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,333333333,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,333333334,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,1,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,2,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,1111111,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,1231231,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,31034826,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,50000000,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,111111111,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,123123122,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,123123123,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,233423423,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,333333333,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,333333334,'2024-12-31','17:58:04','Crear Nomina Cestaticket'),
(31034826,1,'2024-12-31','18:33:06','Crear Nomina Cestaticket'),
(31034826,2,'2024-12-31','18:33:06','Crear Nomina Cestaticket'),
(31034826,1111111,'2024-12-31','18:33:06','Crear Nomina Cestaticket'),
(31034826,1231231,'2024-12-31','18:33:06','Crear Nomina Cestaticket'),
(31034826,31034826,'2024-12-31','18:33:06','Crear Nomina Cestaticket'),
(31034826,50000000,'2024-12-31','18:33:06','Crear Nomina Cestaticket'),
(31034826,111111111,'2024-12-31','18:33:06','Crear Nomina Cestaticket'),
(31034826,123123122,'2024-12-31','18:33:06','Crear Nomina Cestaticket'),
(31034826,123123123,'2024-12-31','18:33:06','Crear Nomina Cestaticket'),
(31034826,233423423,'2024-12-31','18:33:06','Crear Nomina Cestaticket'),
(31034826,333333333,'2024-12-31','18:33:07','Crear Nomina Cestaticket'),
(31034826,333333334,'2024-12-31','18:33:07','Crear Nomina Cestaticket'),
(31034826,1,'2024-12-31','18:34:47','Crear Nomina Cestaticket'),
(31034826,2,'2024-12-31','18:34:47','Crear Nomina Cestaticket'),
(31034826,1111111,'2024-12-31','18:34:47','Crear Nomina Cestaticket'),
(31034826,1231231,'2024-12-31','18:34:47','Crear Nomina Cestaticket'),
(31034826,31034826,'2024-12-31','18:34:47','Crear Nomina Cestaticket'),
(31034826,50000000,'2024-12-31','18:34:47','Crear Nomina Cestaticket'),
(31034826,111111111,'2024-12-31','18:34:47','Crear Nomina Cestaticket'),
(31034826,123123122,'2024-12-31','18:34:47','Crear Nomina Cestaticket'),
(31034826,123123123,'2024-12-31','18:34:47','Crear Nomina Cestaticket'),
(31034826,233423423,'2024-12-31','18:34:47','Crear Nomina Cestaticket'),
(31034826,333333333,'2024-12-31','18:34:47','Crear Nomina Cestaticket'),
(31034826,333333334,'2024-12-31','18:34:47','Crear Nomina Cestaticket'),
(31034826,1,'2024-12-31','18:41:46','Crear Nomina Cestaticket'),
(31034826,2,'2024-12-31','18:41:46','Crear Nomina Cestaticket'),
(31034826,1111111,'2024-12-31','18:41:46','Crear Nomina Cestaticket'),
(31034826,1231231,'2024-12-31','18:41:46','Crear Nomina Cestaticket'),
(31034826,31034826,'2024-12-31','18:41:46','Crear Nomina Cestaticket'),
(31034826,50000000,'2024-12-31','18:41:46','Crear Nomina Cestaticket'),
(31034826,111111111,'2024-12-31','18:41:46','Crear Nomina Cestaticket'),
(31034826,123123122,'2024-12-31','18:41:46','Crear Nomina Cestaticket'),
(31034826,123123123,'2024-12-31','18:41:46','Crear Nomina Cestaticket'),
(31034826,233423423,'2024-12-31','18:41:46','Crear Nomina Cestaticket'),
(31034826,333333333,'2024-12-31','18:41:46','Crear Nomina Cestaticket'),
(31034826,333333334,'2024-12-31','18:41:46','Crear Nomina Cestaticket'),
(233333333,31034826,'2025-01-02','02:12:58','Crear Usuario'),
(233333332,31034826,'2025-01-02','02:13:28','Crear Usuario'),
(344444444,31034826,'2025-01-02','02:13:49','Crear Usuario'),
(233333233,31034826,'2025-01-02','02:14:22','Crear Usuario'),
(444444444,31034826,'2025-01-02','02:14:51','Crear Usuario'),
(343433333,31034826,'2025-01-02','02:18:25','Crear Usuario'),
(345444444,31034826,'2025-01-02','02:18:43','Crear Usuario'),
(453534533,31034826,'2025-01-02','02:19:01','Crear Usuario'),
(454535345,31034826,'2025-01-02','02:19:16','Crear Usuario'),
(341111111,31034826,'2025-01-02','02:19:35','Crear Usuario'),
(89684444,31034826,'2025-01-02','02:19:52','Crear Usuario'),
(333334234,31034826,'2025-01-02','02:20:04','Crear Usuario'),
(121212222,31034826,'2025-01-02','02:20:35','Crear Usuario'),
(234234444,31034826,'2025-01-02','02:20:49','Crear Usuario'),
(343434343,31034826,'2025-01-02','02:22:18','Crear Usuario'),
(444444449,31034826,'2025-01-02','02:22:36','Crear Usuario'),
(321111111,31034826,'2025-01-02','02:22:53','Crear Usuario'),
(333333322,31034826,'2025-01-02','02:23:07','Crear Usuario'),
(212111111,31034826,'2025-01-02','02:23:18','Crear Usuario'),
(421333333,31034826,'2025-01-02','02:23:29','Crear Usuario'),
(15050177,31034826,'2025-01-02','14:17:50','Crear Usuario'),
(1,31034826,'2025-01-03','13:23:48','Crear Nomina'),
(2,31034826,'2025-01-03','13:23:48','Crear Nomina'),
(1231231,31034826,'2025-01-03','13:23:48','Crear Nomina'),
(15050177,31034826,'2025-01-03','13:23:48','Crear Nomina'),
(89684444,31034826,'2025-01-03','13:23:48','Crear Nomina'),
(111111111,31034826,'2025-01-03','13:23:48','Crear Nomina'),
(121212222,31034826,'2025-01-03','13:23:48','Crear Nomina'),
(123123122,31034826,'2025-01-03','13:23:48','Crear Nomina'),
(123123123,31034826,'2025-01-03','13:23:48','Crear Nomina'),
(212111111,31034826,'2025-01-03','13:23:48','Crear Nomina'),
(233333233,31034826,'2025-01-03','13:23:48','Crear Nomina'),
(233333332,31034826,'2025-01-03','13:23:48','Crear Nomina'),
(233333333,31034826,'2025-01-03','13:23:48','Crear Nomina'),
(233423423,31034826,'2025-01-03','13:23:48','Crear Nomina'),
(234234444,31034826,'2025-01-03','13:23:48','Crear Nomina'),
(321111111,31034826,'2025-01-03','13:23:48','Crear Nomina'),
(333333322,31034826,'2025-01-03','13:23:48','Crear Nomina'),
(333333333,31034826,'2025-01-03','13:23:48','Crear Nomina'),
(333333334,31034826,'2025-01-03','13:23:48','Crear Nomina'),
(333334234,31034826,'2025-01-03','13:23:48','Crear Nomina'),
(341111111,31034826,'2025-01-03','13:23:49','Crear Nomina'),
(343433333,31034826,'2025-01-03','13:23:49','Crear Nomina'),
(343434343,31034826,'2025-01-03','13:23:49','Crear Nomina'),
(344444444,31034826,'2025-01-03','13:23:49','Crear Nomina'),
(345444444,31034826,'2025-01-03','13:23:49','Crear Nomina'),
(421333333,31034826,'2025-01-03','13:23:49','Crear Nomina'),
(444444444,31034826,'2025-01-03','13:23:49','Crear Nomina'),
(444444449,31034826,'2025-01-03','13:23:49','Crear Nomina'),
(453534533,31034826,'2025-01-03','13:23:49','Crear Nomina'),
(454535345,31034826,'2025-01-03','13:23:49','Crear Nomina'),
(1,31034826,'2025-01-03','15:44:53','Crear Nomina'),
(2,31034826,'2025-01-03','15:44:53','Crear Nomina'),
(1231231,31034826,'2025-01-03','15:44:53','Crear Nomina'),
(15050177,31034826,'2025-01-03','15:44:53','Crear Nomina'),
(89684444,31034826,'2025-01-03','15:44:53','Crear Nomina'),
(111111111,31034826,'2025-01-03','15:44:53','Crear Nomina'),
(121212222,31034826,'2025-01-03','15:44:53','Crear Nomina'),
(123123122,31034826,'2025-01-03','15:44:53','Crear Nomina'),
(123123123,31034826,'2025-01-03','15:44:53','Crear Nomina'),
(212111111,31034826,'2025-01-03','15:44:53','Crear Nomina'),
(233333233,31034826,'2025-01-03','15:44:53','Crear Nomina'),
(233333332,31034826,'2025-01-03','15:44:53','Crear Nomina'),
(233333333,31034826,'2025-01-03','15:44:53','Crear Nomina'),
(233423423,31034826,'2025-01-03','15:44:53','Crear Nomina'),
(234234444,31034826,'2025-01-03','15:44:53','Crear Nomina'),
(321111111,31034826,'2025-01-03','15:44:53','Crear Nomina'),
(333333322,31034826,'2025-01-03','15:44:53','Crear Nomina'),
(333333333,31034826,'2025-01-03','15:44:53','Crear Nomina'),
(333333334,31034826,'2025-01-03','15:44:53','Crear Nomina'),
(333334234,31034826,'2025-01-03','15:44:54','Crear Nomina'),
(341111111,31034826,'2025-01-03','15:44:54','Crear Nomina'),
(343433333,31034826,'2025-01-03','15:44:54','Crear Nomina'),
(343434343,31034826,'2025-01-03','15:44:54','Crear Nomina'),
(344444444,31034826,'2025-01-03','15:44:54','Crear Nomina'),
(345444444,31034826,'2025-01-03','15:44:54','Crear Nomina'),
(421333333,31034826,'2025-01-03','15:44:54','Crear Nomina'),
(444444444,31034826,'2025-01-03','15:44:54','Crear Nomina'),
(444444449,31034826,'2025-01-03','15:44:54','Crear Nomina'),
(453534533,31034826,'2025-01-03','15:44:54','Crear Nomina'),
(454535345,31034826,'2025-01-03','15:44:54','Crear Nomina'),
(1111111,31034826,'2025-01-03','23:11:29','Crear Nomina'),
(31034826,31034826,'2025-01-03','23:11:29','Crear Nomina'),
(50000000,31034826,'2025-01-03','23:11:29','Crear Nomina'),
(31034826,1,'2025-01-03','23:11:49','Crear Nomina Cestaticket'),
(31034826,2,'2025-01-03','23:11:49','Crear Nomina Cestaticket'),
(31034826,1111111,'2025-01-03','23:11:49','Crear Nomina Cestaticket'),
(31034826,1231231,'2025-01-03','23:11:49','Crear Nomina Cestaticket'),
(31034826,15050177,'2025-01-03','23:11:49','Crear Nomina Cestaticket'),
(31034826,31034826,'2025-01-03','23:11:49','Crear Nomina Cestaticket'),
(31034826,50000000,'2025-01-03','23:11:49','Crear Nomina Cestaticket'),
(31034826,89684444,'2025-01-03','23:11:49','Crear Nomina Cestaticket'),
(31034826,111111111,'2025-01-03','23:11:49','Crear Nomina Cestaticket'),
(31034826,121212222,'2025-01-03','23:11:49','Crear Nomina Cestaticket'),
(31034826,123123122,'2025-01-03','23:11:49','Crear Nomina Cestaticket'),
(31034826,123123123,'2025-01-03','23:11:49','Crear Nomina Cestaticket'),
(31034826,212111111,'2025-01-03','23:11:49','Crear Nomina Cestaticket'),
(31034826,233333233,'2025-01-03','23:11:49','Crear Nomina Cestaticket'),
(31034826,233333332,'2025-01-03','23:11:49','Crear Nomina Cestaticket'),
(31034826,233333333,'2025-01-03','23:11:50','Crear Nomina Cestaticket'),
(31034826,233423423,'2025-01-03','23:11:50','Crear Nomina Cestaticket'),
(31034826,234234444,'2025-01-03','23:11:50','Crear Nomina Cestaticket'),
(31034826,321111111,'2025-01-03','23:11:50','Crear Nomina Cestaticket'),
(31034826,333333322,'2025-01-03','23:11:50','Crear Nomina Cestaticket'),
(31034826,333333333,'2025-01-03','23:11:50','Crear Nomina Cestaticket'),
(31034826,333333334,'2025-01-03','23:11:50','Crear Nomina Cestaticket'),
(31034826,333334234,'2025-01-03','23:11:50','Crear Nomina Cestaticket'),
(31034826,341111111,'2025-01-03','23:11:50','Crear Nomina Cestaticket'),
(31034826,343433333,'2025-01-03','23:11:50','Crear Nomina Cestaticket'),
(31034826,343434343,'2025-01-03','23:11:50','Crear Nomina Cestaticket'),
(31034826,344444444,'2025-01-03','23:11:50','Crear Nomina Cestaticket'),
(31034826,345444444,'2025-01-03','23:11:50','Crear Nomina Cestaticket'),
(31034826,421333333,'2025-01-03','23:11:50','Crear Nomina Cestaticket'),
(31034826,444444444,'2025-01-03','23:11:50','Crear Nomina Cestaticket'),
(31034826,444444449,'2025-01-03','23:11:50','Crear Nomina Cestaticket'),
(31034826,453534533,'2025-01-03','23:11:50','Crear Nomina Cestaticket'),
(31034826,454535345,'2025-01-03','23:11:50','Crear Nomina Cestaticket'),
(343434355,31034826,'2025-01-04','00:11:59','Crear Usuario'),
(343434355,31034826,'2025-01-05','11:21:38','Crear Nomina'),
(343434355,31034826,'2025-01-05','12:27:37','Crear Nomina'),
(343434355,31034826,'2025-01-05','12:28:28','Crear Nomina'),
(343434355,31034826,'2025-01-05','12:48:09','Crear Nomina'),
(343434355,31034826,'2025-01-05','12:52:01','Crear Nomina'),
(343434355,31034826,'2025-01-05','12:52:12','Crear Nomina'),
(1111111,31034826,'2025-01-07','00:12:12','Crear Nomina'),
(31034826,31034826,'2025-01-07','00:12:12','Crear Nomina'),
(50000000,31034826,'2025-01-07','00:12:12','Crear Nomina'),
(1,31034826,'2025-01-07','01:28:44','Crear Nomina'),
(2,31034826,'2025-01-07','01:28:44','Crear Nomina'),
(1231231,31034826,'2025-01-07','01:28:44','Crear Nomina'),
(15050177,31034826,'2025-01-07','01:28:44','Crear Nomina'),
(89684444,31034826,'2025-01-07','01:28:44','Crear Nomina'),
(111111111,31034826,'2025-01-07','01:28:44','Crear Nomina'),
(121212222,31034826,'2025-01-07','01:28:44','Crear Nomina'),
(123123122,31034826,'2025-01-07','01:28:44','Crear Nomina'),
(123123123,31034826,'2025-01-07','01:28:44','Crear Nomina'),
(212111111,31034826,'2025-01-07','01:28:45','Crear Nomina'),
(233333233,31034826,'2025-01-07','01:28:45','Crear Nomina'),
(233333332,31034826,'2025-01-07','01:28:45','Crear Nomina'),
(233333333,31034826,'2025-01-07','01:28:45','Crear Nomina'),
(233423423,31034826,'2025-01-07','01:28:45','Crear Nomina'),
(234234444,31034826,'2025-01-07','01:28:45','Crear Nomina'),
(321111111,31034826,'2025-01-07','01:28:45','Crear Nomina'),
(333333322,31034826,'2025-01-07','01:28:45','Crear Nomina'),
(333333333,31034826,'2025-01-07','01:28:45','Crear Nomina'),
(333333334,31034826,'2025-01-07','01:28:45','Crear Nomina'),
(333334234,31034826,'2025-01-07','01:28:45','Crear Nomina'),
(341111111,31034826,'2025-01-07','01:28:45','Crear Nomina'),
(343433333,31034826,'2025-01-07','01:28:45','Crear Nomina'),
(343434343,31034826,'2025-01-07','01:28:45','Crear Nomina'),
(344444444,31034826,'2025-01-07','01:28:45','Crear Nomina'),
(345444444,31034826,'2025-01-07','01:28:45','Crear Nomina'),
(421333333,31034826,'2025-01-07','01:28:45','Crear Nomina'),
(444444444,31034826,'2025-01-07','01:28:45','Crear Nomina'),
(444444449,31034826,'2025-01-07','01:28:45','Crear Nomina'),
(453534533,31034826,'2025-01-07','01:28:45','Crear Nomina'),
(454535345,31034826,'2025-01-07','01:28:45','Crear Nomina'),
(222222222,31034826,'2025-01-07','01:29:12','Crear Usuario'),
(999999999,31034826,'2025-01-07','01:30:49','Crear Usuario'),
(111111113,31034826,'2025-01-07','01:35:26','Crear Usuario'),
(232333333,31034826,'2025-01-07','01:37:31','Crear Usuario'),
(345222222,31034826,'2025-01-07','01:38:29','Crear Usuario'),
(111111113,31034826,'2025-01-07','04:03:05','Crear Nomina'),
(222222222,31034826,'2025-01-07','04:03:05','Crear Nomina'),
(343434355,31034826,'2025-01-07','04:03:05','Crear Nomina'),
(999999999,31034826,'2025-01-07','04:03:05','Crear Nomina'),
(1,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(2,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(1231231,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(15050177,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(89684444,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(111111111,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(121212222,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(123123122,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(123123123,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(212111111,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(232333333,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(233333233,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(233333332,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(233333333,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(233423423,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(234234444,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(321111111,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(333333322,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(333333333,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(333333334,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(333334234,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(341111111,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(343433333,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(343434343,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(344444444,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(345444444,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(421333333,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(444444444,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(444444449,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(453534533,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(454535345,31034826,'2025-01-07','04:03:22','Crear Nomina'),
(1111111,31034826,'2025-01-07','04:03:33','Crear Nomina'),
(31034826,31034826,'2025-01-07','04:03:33','Crear Nomina'),
(50000000,31034826,'2025-01-07','04:03:33','Crear Nomina'),
(345222222,31034826,'2025-01-07','04:03:33','Crear Nomina'),
(1111111,31034826,'2025-01-07','04:14:43','Crear Nomina'),
(31034826,31034826,'2025-01-07','04:14:43','Crear Nomina'),
(50000000,31034826,'2025-01-07','04:14:43','Crear Nomina'),
(345222222,31034826,'2025-01-07','04:14:43','Crear Nomina'),
(111111113,31034826,'2025-01-07','04:18:51','Crear Nomina'),
(222222222,31034826,'2025-01-07','04:18:51','Crear Nomina'),
(343434355,31034826,'2025-01-07','04:18:51','Crear Nomina'),
(999999999,31034826,'2025-01-07','04:18:51','Crear Nomina');
/*!40000 ALTER TABLE `historial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lista_nominas`
--

DROP TABLE IF EXISTS `lista_nominas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lista_nominas` (
  `nro` int(11) NOT NULL AUTO_INCREMENT,
  `cuenta` varchar(255) DEFAULT NULL,
  `total_neto` double DEFAULT NULL,
  `total_deducciones` double DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `tipo` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`nro`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lista_nominas`
--

LOCK TABLES `lista_nominas` WRITE;
/*!40000 ALTER TABLE `lista_nominas` DISABLE KEYS */;
INSERT INTO `lista_nominas` VALUES
(1,'01201234123412341234',2381.34,3.9000000000000004,'2024-12-13',NULL,'Resumen Consolidado'),
(2,'01201234123412341234',2381.34,3.9000000000000004,'2024-12-13',NULL,'Resumen Consolidado'),
(3,'01201234123412341234',2381.34,3.9000000000000004,'2024-12-13',NULL,'Resumen Consolidado'),
(4,'01201234123412341234',2381.34,3.9000000000000004,'2024-12-13',NULL,'Resumen Consolidado'),
(5,'01201234123412341234',2381.34,59.510000000000005,'2024-12-13',NULL,'Resumen Consolidado');
/*!40000 ALTER TABLE `lista_nominas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nomina_cestaticket`
--

DROP TABLE IF EXISTS `nomina_cestaticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nomina_cestaticket` (
  `nombre` varchar(255) DEFAULT NULL,
  `cedula` int(11) DEFAULT NULL,
  `total_neto` double DEFAULT NULL,
  `descuentos` double DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nomina_cestaticket`
--

LOCK TABLES `nomina_cestaticket` WRITE;
/*!40000 ALTER TABLE `nomina_cestaticket` DISABLE KEYS */;
INSERT INTO `nomina_cestaticket` VALUES
('Sds W',1,1500,0,'2024-12-31',NULL),
('Ww W',2,1500,0,'2024-12-31',NULL),
('Asa Mama',1111111,1500,0,'2024-12-31',NULL),
('Pepe Per',1231231,1500,0,'2024-12-31',NULL),
('Carlos Moras',31034826,1500,0,'2024-12-31',NULL),
('Carlos Augusto',50000000,1500,0,'2024-12-31',NULL),
('W W',111111111,1500,0,'2024-12-31',NULL),
('Pdro Morta',123123122,1500,0,'2024-12-31',NULL),
('Qwqe Qweqwe',123123123,1500,0,'2024-12-31',NULL),
('Asas adsdasd asdadsa Asdads adasdad',233423423,1500,0,'2024-12-31',NULL),
('Aerawerr Sefsdfsafds',333333333,1500,0,'2024-12-31',NULL),
('Eeee Eeee',333333334,1500,0,'2024-12-31',NULL),
('Sdsadad W',1,1500,0,'2025-01-03',NULL),
('Ww W',2,1500,0,'2025-01-03',NULL),
('Asa Mama',1111111,1500,0,'2025-01-03',NULL),
('Pepe Per',1231231,1500,0,'2025-01-03',NULL),
('Elizabeth Del Carmen Bolivar Galvis',15050177,1500,0,'2025-01-03',NULL),
('Carlos Moras',31034826,1500,0,'2025-01-03',NULL),
('Carlos Augusto',50000000,1500,0,'2025-01-03',NULL),
('R R',89684444,1500,0,'2025-01-03',NULL),
('W W',111111111,1500,0,'2025-01-03',NULL),
('X X',121212222,1500,0,'2025-01-03',NULL),
('Pdro Morta',123123122,1500,0,'2025-01-03',NULL),
('Qwqe Qweqwe',123123123,1500,0,'2025-01-03',NULL),
('E E',212111111,1500,0,'2025-01-03',NULL),
('D Dw',233333233,1500,0,'2025-01-03',NULL),
('Rqwe Qwer',233333332,1500,0,'2025-01-03',NULL),
('Dd D',233333333,1500,0,'2025-01-03',NULL),
('Asas adsdasd asdadsa Asdads adasdad',233423423,1500,0,'2025-01-03',NULL),
('R R',234234444,1500,0,'2025-01-03',NULL),
('R R',321111111,1500,0,'2025-01-03',NULL),
('R R',333333322,1500,0,'2025-01-03',NULL),
('Aerawerr Sefsdfsafds',333333333,1500,0,'2025-01-03',NULL),
('Eeee Eeee',333333334,1500,0,'2025-01-03',NULL),
('R R',333334234,1500,0,'2025-01-03',NULL),
('T T',341111111,1500,0,'2025-01-03',NULL),
('R R',343433333,1500,0,'2025-01-03',NULL),
('F F',343434343,1500,0,'2025-01-03',NULL),
('Rtr R',344444444,1500,0,'2025-01-03',NULL),
('Y Y',345444444,1500,0,'2025-01-03',NULL),
('E E',421333333,1500,0,'2025-01-03',NULL),
('V V',444444444,1500,0,'2025-01-03',NULL),
('E E',444444449,1500,0,'2025-01-03',NULL),
('Ttttttttttttttttttttttt T',453534533,1500,0,'2025-01-03',NULL),
('Ggggggggggggggggggggg Gg',454535345,1500,0,'2025-01-03',NULL);
/*!40000 ALTER TABLE `nomina_cestaticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nomina_cestaticket_prev`
--

DROP TABLE IF EXISTS `nomina_cestaticket_prev`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nomina_cestaticket_prev` (
  `nombre` varchar(255) DEFAULT NULL,
  `cedula` int(11) DEFAULT NULL,
  `total_neto` double DEFAULT NULL,
  `descuentos` double DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nomina_cestaticket_prev`
--

LOCK TABLES `nomina_cestaticket_prev` WRITE;
/*!40000 ALTER TABLE `nomina_cestaticket_prev` DISABLE KEYS */;
INSERT INTO `nomina_cestaticket_prev` VALUES
('Dada Sded',343434355,1150,350,'2025-01-07','Cestaticet');
/*!40000 ALTER TABLE `nomina_cestaticket_prev` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nomina_semanal`
--

DROP TABLE IF EXISTS `nomina_semanal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nomina_semanal` (
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
  PRIMARY KEY (`n`),
  KEY `cedula` (`cedula`),
  KEY `fk_nomina_cedula` (`made_by`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nomina_semanal`
--

LOCK TABLES `nomina_semanal` WRITE;
/*!40000 ALTER TABLE `nomina_semanal` DISABLE KEYS */;
INSERT INTO `nomina_semanal` VALUES
(111111113,222,40,40,40,6.25,4.44,0,352.69,12.75,1.02,8.2,3.53,0,339.94,'2025-01-08','Semanal','2025-01-14',31034826,0,1,NULL,'2025-01-07'),
(222222222,333,40,40,40,9.38,99.9,0,562.275,19.46,1.54,12.3,5.62,0,542.81,'2025-01-08','Semanal','2025-01-14',31034826,0,2,NULL,'2025-01-07'),
(343434355,234,40,40,40,6.25,70.2,0,430.45,14.02,1.08,8.64,4.3,0,416.43,'2025-01-08','Semanal','2025-01-14',31034826,0,3,NULL,'2025-01-07'),
(999999999,999,40,40,40,28.12,299.7,0,1446.825,55.97,4.61,36.89,14.47,0,1390.86,'2025-01-08','Semanal','2025-01-14',31034826,0,4,NULL,'2025-01-07');
/*!40000 ALTER TABLE `nomina_semanal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nomina_semanal_prev`
--

DROP TABLE IF EXISTS `nomina_semanal_prev`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nomina_semanal_prev` (
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
  PRIMARY KEY (`n`),
  KEY `cedula` (`cedula`),
  KEY `fk_nomina_cedula` (`made_by`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nomina_semanal_prev`
--

LOCK TABLES `nomina_semanal_prev` WRITE;
/*!40000 ALTER TABLE `nomina_semanal_prev` DISABLE KEYS */;
INSERT INTO `nomina_semanal_prev` VALUES
(111111113,222,40,40,40,6.25,4.44,0,352.69,12.75,1.02,8.2,3.53,0,339.94,'2025-01-22','Semanal','2025-01-28',31034826,0,1,4),
(222222222,333,40,40,40,9.38,99.9,0,562.275,19.46,1.54,12.3,5.62,0,542.81,'2025-01-22','Semanal','2025-01-28',31034826,0,2,4),
(343434355,234,40,40,40,6.25,70.2,0,430.45,14.02,1.08,8.64,4.3,0,416.43,'2025-01-22','Semanal','2025-01-28',31034826,0,3,4),
(999999999,999,40,40,40,28.12,299.7,0,1446.825,55.97,4.61,36.89,14.47,0,1390.86,'2025-01-22','Semanal','2025-01-28',31034826,0,4,4);
/*!40000 ALTER TABLE `nomina_semanal_prev` ENABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nominas`
--

LOCK TABLES `nominas` WRITE;
/*!40000 ALTER TABLE `nominas` DISABLE KEYS */;
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
  `created` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nominas_prev`
--

LOCK TABLES `nominas_prev` WRITE;
/*!40000 ALTER TABLE `nominas_prev` DISABLE KEYS */;
INSERT INTO `nominas_prev` VALUES
(1111111,345,160,160,160,37.5,103.5,0,966,23.99,1.59,12.74,9.66,0,942.01,'2025-01-01','Mensual','2025-01-31',31034826,0,1,'2025-01-07'),
(31034826,100,160,160,160,0,0,20,600,10.15,0.46,3.69,6,0,589.85,'2025-01-01','Mensual','2025-01-31',31034826,0,2,'2025-01-07'),
(50000000,400,160,160,160,0,8,80,968,26.3,1.85,14.77,9.68,0,941.7,'2025-01-01','Mensual','2025-01-31',31034826,0,3,'2025-01-07'),
(345222222,4,160,160,160,50,1.2,0,535.2,5.52,0.02,0.15,5.35,0,529.68,'2025-01-01','Mensual','2025-01-31',31034826,0,4,'2025-01-07');
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES
(50000000,'1234','micorreo@dad','Privilegiado'),
(31034826,'123456','moralesyaguilera@gmail.com','Privilegiado');
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

-- Dump completed on 2025-01-07  4:49:05
