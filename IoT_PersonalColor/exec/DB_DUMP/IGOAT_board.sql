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
-- Table structure for table `board`
--

DROP TABLE IF EXISTS `board`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `board` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `personalcolor` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `imageUrl` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `board_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `board`
--

LOCK TABLES `board` WRITE;
/*!40000 ALTER TABLE `board` DISABLE KEYS */;
INSERT INTO `board` VALUES (6,'수정1','테스트1','autumn','images/20230216030043_15.jpg','2023-02-16 02:21:52','2023-02-16 03:01:04',5),(7,'dddddddd','ddddd','summer','images/20230216023218_beauty2.jpg','2023-02-16 02:32:18','2023-02-16 02:32:18',1),(8,'eeeeee','eeeeeeeeeeee','winter','images/20230216023339_beauty.jpg','2023-02-16 02:33:39','2023-02-16 02:33:39',3),(9,'weijasdqwe','difjweqwe','winter','images/20230216024014_ìì§1.jpg','2023-02-16 02:40:14','2023-02-16 02:40:14',3),(10,'수지수지123124123123','수지수지','autumn','images/20230216030947_ìì§1.jpg','2023-02-16 03:09:47','2023-02-16 03:10:30',3),(12,'ㅁㅇㅇ','ㄹㄴㅇ','autumn','images/20230216063400_19.jpg','2023-02-16 06:33:15','2023-02-16 06:34:00',4),(13,'ㅇㄴㅁ','ㅁㄴㅇ','winter','images/20230216063435_21.jpg','2023-02-16 06:34:35','2023-02-16 06:34:35',4),(14,'asd','asd','autumn','images/20230216071758_15.jpg','2023-02-16 07:17:59','2023-02-16 07:17:59',4),(15,'13','42','summer','images/20230216081155_32.jpg','2023-02-16 08:11:55','2023-02-16 08:11:55',4),(16,'두번째가','글을 씀','winter','images/20230216081913_13.jpg','2023-02-16 08:19:13','2023-02-16 08:19:49',5),(17,'1d','2d','autumn','images/20230216083602_22.jpg','2023-02-16 08:36:02','2023-02-16 08:36:02',4);
/*!40000 ALTER TABLE `board` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-16 17:36:04
