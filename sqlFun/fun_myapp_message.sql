-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: fun
-- ------------------------------------------------------
-- Server version	8.0.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `myapp_message`
--

DROP TABLE IF EXISTS `myapp_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_message` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `subject` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `is_read` tinyint(1) NOT NULL,
  `recipient_id` bigint NOT NULL,
  `sender_id` bigint NOT NULL,
  `quoted_message_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_message_recipient_id_9a174643_fk_myapp_member_id` (`recipient_id`),
  KEY `myapp_message_sender_id_4e6ade5c_fk_myapp_member_id` (`sender_id`),
  KEY `myapp_message_quoted_message_id_c270d5d9_fk_myapp_message_id` (`quoted_message_id`),
  CONSTRAINT `myapp_message_quoted_message_id_c270d5d9_fk_myapp_message_id` FOREIGN KEY (`quoted_message_id`) REFERENCES `myapp_message` (`id`),
  CONSTRAINT `myapp_message_recipient_id_9a174643_fk_myapp_member_id` FOREIGN KEY (`recipient_id`) REFERENCES `myapp_member` (`id`),
  CONSTRAINT `myapp_message_sender_id_4e6ade5c_fk_myapp_member_id` FOREIGN KEY (`sender_id`) REFERENCES `myapp_member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_message`
--

LOCK TABLES `myapp_message` WRITE;
/*!40000 ALTER TABLE `myapp_message` DISABLE KEYS */;
INSERT INTO `myapp_message` VALUES (6,'你好喔','<p>dsadsf</p>','2024-10-11 17:39:23.478807',1,1,1,NULL);
/*!40000 ALTER TABLE `myapp_message` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-12 10:42:51
