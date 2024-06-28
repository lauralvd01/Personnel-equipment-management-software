-- MySQL dump 10.13  Distrib 8.4.0, for Linux (x86_64)
--
-- Host: localhost    Database: inf236backenddb
-- ------------------------------------------------------
-- Server version	8.4.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add motor',7,'add_motor'),(26,'Can change motor',7,'change_motor'),(27,'Can delete motor',7,'delete_motor'),(28,'Can view motor',7,'view_motor'),(29,'Can add camion',8,'add_camion'),(30,'Can change camion',8,'change_camion'),(31,'Can delete camion',8,'delete_camion'),(32,'Can view camion',8,'view_camion'),(33,'Can add asignacion motor camion',9,'add_asignacionmotorcamion'),(34,'Can change asignacion motor camion',9,'change_asignacionmotorcamion'),(35,'Can delete asignacion motor camion',9,'delete_asignacionmotorcamion'),(36,'Can view asignacion motor camion',9,'view_asignacionmotorcamion'),(37,'Can add asign',10,'add_asign'),(38,'Can change asign',10,'change_asign'),(39,'Can delete asign',10,'delete_asign'),(40,'Can view asign',10,'view_asign'),(41,'Can add componente',11,'add_componente'),(42,'Can change componente',11,'change_componente'),(43,'Can delete componente',11,'delete_componente'),(44,'Can view componente',11,'view_componente'),(45,'Can add sistema',12,'add_sistema'),(46,'Can change sistema',12,'change_sistema'),(47,'Can delete sistema',12,'delete_sistema'),(48,'Can view sistema',12,'view_sistema'),(49,'Can add incidencia',13,'add_incidencia'),(50,'Can change incidencia',13,'change_incidencia'),(51,'Can delete incidencia',13,'delete_incidencia'),(52,'Can view incidencia',13,'view_incidencia'),(53,'Can add usuario',14,'add_usuario'),(54,'Can change usuario',14,'change_usuario'),(55,'Can delete usuario',14,'delete_usuario'),(56,'Can view usuario',14,'view_usuario');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(10,'inf236backend','asign'),(9,'inf236backend','asignacionmotorcamion'),(8,'inf236backend','camion'),(11,'inf236backend','componente'),(13,'inf236backend','incidencia'),(7,'inf236backend','motor'),(12,'inf236backend','sistema'),(14,'inf236backend','usuario'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-05-29 19:03:23.415282'),(2,'auth','0001_initial','2024-05-29 19:03:23.980422'),(3,'admin','0001_initial','2024-05-29 19:03:24.118907'),(4,'admin','0002_logentry_remove_auto_add','2024-05-29 19:03:24.130427'),(5,'admin','0003_logentry_add_action_flag_choices','2024-05-29 19:03:24.143373'),(6,'contenttypes','0002_remove_content_type_name','2024-05-29 19:03:24.226629'),(7,'auth','0002_alter_permission_name_max_length','2024-05-29 19:03:24.295244'),(8,'auth','0003_alter_user_email_max_length','2024-05-29 19:03:24.321298'),(9,'auth','0004_alter_user_username_opts','2024-05-29 19:03:24.333311'),(10,'auth','0005_alter_user_last_login_null','2024-05-29 19:03:24.392114'),(11,'auth','0006_require_contenttypes_0002','2024-05-29 19:03:24.397354'),(12,'auth','0007_alter_validators_add_error_messages','2024-05-29 19:03:24.408621'),(13,'auth','0008_alter_user_username_max_length','2024-05-29 19:03:24.476193'),(14,'auth','0009_alter_user_last_name_max_length','2024-05-29 19:03:24.555365'),(15,'auth','0010_alter_group_name_max_length','2024-05-29 19:03:24.577017'),(16,'auth','0011_update_proxy_permissions','2024-05-29 19:03:24.589506'),(17,'auth','0012_alter_user_first_name_max_length','2024-05-29 19:03:24.658434'),(18,'inf236backend','0001_initial','2024-05-29 19:03:24.685006'),(19,'inf236backend','0002_camion_motor_operativo_motor_tiempo_en_uso_and_more','2024-05-29 19:03:24.883161'),(20,'sessions','0001_initial','2024-05-29 19:03:24.928011'),(21,'inf236backend','0002_initial','2024-06-28 19:37:45.852366'),(22,'inf236backend','0003_delete_asign_and_more','2024-06-28 21:12:42.230815'),(23,'inf236backend','0004_componente_nombre','2024-06-28 21:43:56.218737'),(24,'inf236backend','0005_remove_incidencia_usuario_and_more','2024-06-28 22:13:29.686246'),(25,'inf236backend','0006_remove_incidencia_motor_incidencia_camion','2024-06-28 22:42:53.210477');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inf236backend_asignacionmotorcamion`
--

DROP TABLE IF EXISTS `inf236backend_asignacionmotorcamion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inf236backend_asignacionmotorcamion` (
  `id_asignacion` int NOT NULL AUTO_INCREMENT,
  `fecha_asignacion` datetime(6) NOT NULL,
  `fecha_desasignacion` datetime(6) DEFAULT NULL,
  `camion_id` int NOT NULL,
  `motor_id` int NOT NULL,
  PRIMARY KEY (`id_asignacion`),
  KEY `inf236backend_asigna_camion_id_308d8828_fk_inf236bac` (`camion_id`),
  KEY `inf236backend_asigna_motor_id_d2706abd_fk_inf236bac` (`motor_id`),
  CONSTRAINT `inf236backend_asigna_camion_id_308d8828_fk_inf236bac` FOREIGN KEY (`camion_id`) REFERENCES `inf236backend_camion` (`id_camion`),
  CONSTRAINT `inf236backend_asigna_motor_id_d2706abd_fk_inf236bac` FOREIGN KEY (`motor_id`) REFERENCES `inf236backend_motor` (`id_motor`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inf236backend_asignacionmotorcamion`
--

LOCK TABLES `inf236backend_asignacionmotorcamion` WRITE;
/*!40000 ALTER TABLE `inf236backend_asignacionmotorcamion` DISABLE KEYS */;
INSERT INTO `inf236backend_asignacionmotorcamion` VALUES (2,'2024-06-28 22:36:50.084846',NULL,1,3);
/*!40000 ALTER TABLE `inf236backend_asignacionmotorcamion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inf236backend_camion`
--

DROP TABLE IF EXISTS `inf236backend_camion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inf236backend_camion` (
  `id_camion` int NOT NULL AUTO_INCREMENT,
  `n_serie` varchar(256) NOT NULL,
  `placa` varchar(256) NOT NULL,
  `estado` varchar(256) NOT NULL,
  `fecha_inicio` datetime(6) DEFAULT NULL,
  `durabilidad` int NOT NULL,
  PRIMARY KEY (`id_camion`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inf236backend_camion`
--

LOCK TABLES `inf236backend_camion` WRITE;
/*!40000 ALTER TABLE `inf236backend_camion` DISABLE KEYS */;
INSERT INTO `inf236backend_camion` VALUES (1,'001','SDF-800-CL','En reparación','2024-06-28 22:36:50.084846',12),(2,'002','SER-456-CL','operativo',NULL,12),(3,'003','ANB-978-CL','operativo',NULL,12),(4,'004','ZRT-948-CL','operativo',NULL,12),(5,'005','DTG-482-CL','operativo',NULL,12);
/*!40000 ALTER TABLE `inf236backend_camion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inf236backend_componente`
--

DROP TABLE IF EXISTS `inf236backend_componente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inf236backend_componente` (
  `id_componente` int NOT NULL AUTO_INCREMENT,
  `n_serie` varchar(256) NOT NULL,
  `fecha_inicio` datetime(6) DEFAULT NULL,
  `durabilidad` int NOT NULL,
  `sistema_id` int NOT NULL,
  `nombre` varchar(256) NOT NULL,
  PRIMARY KEY (`id_componente`),
  KEY `inf236backend_compon_sistema_id_7b752a6d_fk_inf236bac` (`sistema_id`),
  CONSTRAINT `inf236backend_compon_sistema_id_7b752a6d_fk_inf236bac` FOREIGN KEY (`sistema_id`) REFERENCES `inf236backend_sistema` (`id_sistema`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inf236backend_componente`
--

LOCK TABLES `inf236backend_componente` WRITE;
/*!40000 ALTER TABLE `inf236backend_componente` DISABLE KEYS */;
INSERT INTO `inf236backend_componente` VALUES (1,'001','2024-06-28 22:36:50.084846',3,1,'Componente a'),(2,'002',NULL,3,2,'Componente a'),(3,'003',NULL,3,3,'Componente a'),(4,'004','2024-06-28 22:36:50.084846',3,5,'Componente a'),(5,'005',NULL,3,6,'Componente a'),(6,'006',NULL,3,7,'Componente a'),(7,'001','2024-06-28 22:36:50.084846',4,1,'Componente b'),(8,'002',NULL,4,2,'Componente b'),(9,'003',NULL,4,3,'Componente b'),(10,'001','2024-06-28 22:36:50.084846',2,5,'Componente c'),(11,'002',NULL,2,6,'Componente c'),(12,'003',NULL,2,7,'Componente c');
/*!40000 ALTER TABLE `inf236backend_componente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inf236backend_incidencia`
--

DROP TABLE IF EXISTS `inf236backend_incidencia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inf236backend_incidencia` (
  `id_incidencia` int NOT NULL AUTO_INCREMENT,
  `descripcion_problema` longtext,
  `descripcion_trabajo_necesario` longtext,
  `fecha_incidencia` datetime(6) NOT NULL,
  `fecha_inicio_trabajo` datetime(6) DEFAULT NULL,
  `fecha_fin_trabajo` datetime(6) DEFAULT NULL,
  `solucionado` tinyint(1) NOT NULL,
  `mecanicos_asociados` longtext,
  `descripcion_trabajo_hecho` longtext,
  `mecanico_asignado_id` int DEFAULT NULL,
  `camion_id` int NOT NULL,
  PRIMARY KEY (`id_incidencia`),
  KEY `inf236backend_incide_mecanico_asignado_id_5910efc5_fk_inf236bac` (`mecanico_asignado_id`),
  KEY `inf236backend_incide_camion_id_58900ed6_fk_inf236bac` (`camion_id`),
  CONSTRAINT `inf236backend_incide_camion_id_58900ed6_fk_inf236bac` FOREIGN KEY (`camion_id`) REFERENCES `inf236backend_camion` (`id_camion`),
  CONSTRAINT `inf236backend_incide_mecanico_asignado_id_5910efc5_fk_inf236bac` FOREIGN KEY (`mecanico_asignado_id`) REFERENCES `inf236backend_usuario` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inf236backend_incidencia`
--

LOCK TABLES `inf236backend_incidencia` WRITE;
/*!40000 ALTER TABLE `inf236backend_incidencia` DISABLE KEYS */;
INSERT INTO `inf236backend_incidencia` VALUES (1,'Cambio programado','Cambiar el componente c del sistema B del motor','2024-06-28 22:46:54.057329',NULL,NULL,0,'Ninguno','',NULL,1),(2,'Cambio programado','Cambiar el componente c del sistema B del motor','2024-06-28 22:50:38.568247',NULL,NULL,0,'Ninguno','',NULL,1),(3,'Cambio programado','Cambiar el componente c del sistema B del motor','2024-06-28 22:51:19.370434',NULL,NULL,0,'Ninguno','',NULL,1);
/*!40000 ALTER TABLE `inf236backend_incidencia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inf236backend_motor`
--

DROP TABLE IF EXISTS `inf236backend_motor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inf236backend_motor` (
  `id_motor` int NOT NULL AUTO_INCREMENT,
  `n_serie` varchar(256) NOT NULL,
  `operativo` tinyint(1) NOT NULL,
  `tiempo_en_uso` int NOT NULL,
  `fecha_inicio` datetime(6) DEFAULT NULL,
  `durabilidad` int NOT NULL,
  PRIMARY KEY (`id_motor`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inf236backend_motor`
--

LOCK TABLES `inf236backend_motor` WRITE;
/*!40000 ALTER TABLE `inf236backend_motor` DISABLE KEYS */;
INSERT INTO `inf236backend_motor` VALUES (3,'001',0,0,'2024-06-28 22:36:50.084846',6),(4,'002',1,0,NULL,6),(6,'003',1,0,NULL,6);
/*!40000 ALTER TABLE `inf236backend_motor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inf236backend_sistema`
--

DROP TABLE IF EXISTS `inf236backend_sistema`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inf236backend_sistema` (
  `id_sistema` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(256) NOT NULL,
  `n_serie` varchar(256) NOT NULL,
  `motor_id` int NOT NULL,
  PRIMARY KEY (`id_sistema`),
  KEY `inf236backend_sistem_motor_id_f2520f27_fk_inf236bac` (`motor_id`),
  CONSTRAINT `inf236backend_sistem_motor_id_f2520f27_fk_inf236bac` FOREIGN KEY (`motor_id`) REFERENCES `inf236backend_motor` (`id_motor`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inf236backend_sistema`
--

LOCK TABLES `inf236backend_sistema` WRITE;
/*!40000 ALTER TABLE `inf236backend_sistema` DISABLE KEYS */;
INSERT INTO `inf236backend_sistema` VALUES (1,'Sistema A','001',3),(2,'Sistema A','002',4),(3,'Sistema A','003',6),(5,'Sistema B','001',3),(6,'Sistema B','002',4),(7,'Sistema B','003',6);
/*!40000 ALTER TABLE `inf236backend_sistema` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inf236backend_usuario`
--

DROP TABLE IF EXISTS `inf236backend_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inf236backend_usuario` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `rut` varchar(256) NOT NULL,
  `contrasena` varchar(256) NOT NULL,
  `nombre` varchar(256) NOT NULL,
  `apellido` varchar(256) NOT NULL,
  `fecha_registro` datetime(6) NOT NULL,
  `rol` varchar(256) NOT NULL,
  `turno` varchar(256) NOT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inf236backend_usuario`
--

LOCK TABLES `inf236backend_usuario` WRITE;
/*!40000 ALTER TABLE `inf236backend_usuario` DISABLE KEYS */;
INSERT INTO `inf236backend_usuario` VALUES (1,'20288965-4','holamundo','Darael','Badilla','2024-06-28 20:36:10.657453','mecanico','4x7'),(2,'202490033-1','xavier','Laura','Levraud','2024-06-28 20:39:01.760429','mecanico','4x7'),(3,'20431255-9','isidora','Daniela','Stuven','2024-06-28 21:36:06.530091','jefedemotores','4x7'),(4,'201930050-4','tobar','Diego','Tobar','2024-06-28 21:51:00.457603','jefedemotores','4x7');
/*!40000 ALTER TABLE `inf236backend_usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-28 23:03:49
