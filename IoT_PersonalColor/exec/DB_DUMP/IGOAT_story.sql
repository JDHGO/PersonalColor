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
-- Table structure for table `story`
--

DROP TABLE IF EXISTS `story`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `story` (
  `id` int NOT NULL AUTO_INCREMENT,
  `content` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `shopname` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `stylename` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `styleinfo` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `address` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `imageUrl` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `membership` tinyint(1) DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `board_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `board_id` (`board_id`),
  CONSTRAINT `story_ibfk_1` FOREIGN KEY (`board_id`) REFERENCES `board` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `story`
--

LOCK TABLES `story` WRITE;
/*!40000 ALTER TABLE `story` DISABLE KEYS */;
INSERT INTO `story` VALUES (1,'ㅁㄴㅇ','ㅁㄴ','ㄴ','ㄴ','ㄴ','images/20230216050809_23.jpg',0,'2023-02-16 05:08:09','2023-02-16 05:08:09',NULL),(2,'','유니클로','','','','images/20230216072536_21.jpg',0,'2023-02-16 07:25:37','2023-02-16 07:25:37',14),(3,'','ad','da','qsv','fs','images/20230216073755_10.jpg',1,'2023-02-16 07:37:55','2023-02-16 07:37:55',14),(4,'','1','3','4','2','images/20230216080053_1.jpg',0,'2023-02-16 08:00:53','2023-02-16 08:00:53',14),(5,'','ad','fs','fs','da','images/20230216081211_19.jpg',0,'2023-02-16 08:12:17','2023-02-16 08:12:17',15),(6,'','ad','fs','fs','da','images/20230216081216_19.jpg',0,'2023-02-16 08:12:19','2023-02-16 08:12:19',15),(7,'','ㅁㄴㅇ','ㅁㄴㅇ','ㄹㄴㅇ','ㄹㅇㄴ','images/20230216081924_15.jpg',0,'2023-02-16 08:19:24','2023-02-16 08:19:24',16);
/*!40000 ALTER TABLE `story` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-16 17:36:02
