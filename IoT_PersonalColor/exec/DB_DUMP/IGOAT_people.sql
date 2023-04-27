-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: ec2-52-78-177-38.ap-northeast-2.compute.amazonaws.com    Database: IGOAT
-- ------------------------------------------------------
-- Server version	8.0.32-0ubuntu0.20.04.2

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
-- Table structure for table `people`
--

DROP TABLE IF EXISTS `people`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `people` (
  `count` int NOT NULL,
  `color` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`count`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `people`
--

LOCK TABLES `people` WRITE;
/*!40000 ALTER TABLE `people` DISABLE KEYS */;
INSERT INTO `people` VALUES (0,'winter'),(1,'spring'),(2,'winter'),(3,'winter'),(4,'spring'),(5,'spring'),(6,'summer'),(7,'winter'),(8,'winter'),(9,'spring'),(10,'summer'),(11,'winter'),(12,'summer'),(13,'winter'),(14,'spring'),(15,'winter'),(16,'winter'),(17,'winter'),(18,'winter'),(19,'winter'),(20,'winter'),(21,'winter'),(22,'winter'),(23,'winter'),(24,'winter'),(25,'spring'),(26,'spring'),(27,'winter'),(28,'spring'),(29,'summer'),(30,'summer'),(31,'winter'),(32,'spring'),(33,'winter'),(34,'winter'),(35,'winter'),(36,'spring'),(37,'winter'),(38,'summer'),(39,'summer'),(40,'summer'),(41,'spring'),(42,'winter'),(43,'summer'),(44,'summer'),(45,'spring'),(46,'spring'),(47,'winter'),(48,'summer'),(49,'winter'),(50,'summer'),(51,'summer'),(52,'winter'),(53,'winter'),(54,'summer'),(55,'winter'),(56,'spring'),(57,'summer'),(58,'summer'),(59,'winter');
/*!40000 ALTER TABLE `people` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-16 17:36:03
