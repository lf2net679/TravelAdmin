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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-10-10 17:51:57.420884'),(2,'contenttypes','0002_remove_content_type_name','2024-10-10 17:51:57.460886'),(3,'auth','0001_initial','2024-10-10 17:51:57.568886'),(4,'auth','0002_alter_permission_name_max_length','2024-10-10 17:51:57.595887'),(5,'auth','0003_alter_user_email_max_length','2024-10-10 17:51:57.606893'),(6,'auth','0004_alter_user_username_opts','2024-10-10 17:51:57.609886'),(7,'auth','0005_alter_user_last_login_null','2024-10-10 17:51:57.611894'),(8,'auth','0006_require_contenttypes_0002','2024-10-10 17:51:57.613895'),(9,'auth','0007_alter_validators_add_error_messages','2024-10-10 17:51:57.616893'),(10,'auth','0008_alter_user_username_max_length','2024-10-10 17:51:57.618893'),(11,'auth','0009_alter_user_last_name_max_length','2024-10-10 17:51:57.621885'),(12,'auth','0010_alter_group_name_max_length','2024-10-10 17:51:57.627886'),(13,'auth','0011_update_proxy_permissions','2024-10-10 17:51:57.630892'),(14,'auth','0012_alter_user_first_name_max_length','2024-10-10 17:51:57.633885'),(15,'myapp','0001_initial','2024-10-10 17:51:57.802885'),(16,'admin','0001_initial','2024-10-10 17:51:57.890885'),(17,'admin','0002_logentry_remove_auto_add','2024-10-10 17:51:57.895885'),(18,'admin','0003_logentry_add_action_flag_choices','2024-10-10 17:51:57.898885'),(19,'sessions','0001_initial','2024-10-10 17:51:57.918895'),(20,'myapp','0002_alter_article_pub_date_message','2024-10-11 15:20:55.964798'),(21,'myapp','0003_auto_20241011_2338','2024-10-11 15:38:47.453621'),(22,'myapp','0004_product_restaurant_alter_member_managers_and_more','2024-10-11 15:42:50.771727'),(23,'myapp','0005_member_favorite_products_member_favorite_restaurants','2024-10-11 15:46:48.358208'),(24,'myapp','0006_message_quoted_message','2024-10-11 15:59:00.692211'),(25,'myapp','0007_alter_message_content','2024-10-11 16:05:28.963519'),(26,'myapp','0008_member_address_alter_member_full_name','2024-10-11 17:03:19.637187'),(27,'forum_system','0001_initial','2024-10-11 17:20:27.838415'),(28,'forum_system','0002_category_article_comment','2024-10-11 17:32:38.391791');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
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
