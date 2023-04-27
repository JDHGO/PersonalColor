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
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `username` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `personalcolor` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `usermyself` varchar(1000) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `userimgurl` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `follower` varchar(5000) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'test1234@naver.com','test','125816a6c8f287f2712b43d37265739ea3e9bd7274b3f983ed1c1e9572c074c4181c4ce0386ff7edd92ff1e8ab1cbb92ad5f54a8a34dd6f7bac4a2763a772577','spring',NULL,'images/20230216023208_face.jpg','3','2023-02-16 01:32:17','2023-02-16 02:32:59'),(3,'test@naver.com','test1234','125816a6c8f287f2712b43d37265739ea3e9bd7274b3f983ed1c1e9572c074c4181c4ce0386ff7edd92ff1e8ab1cbb92ad5f54a8a34dd6f7bac4a2763a772577','autumn',NULL,'images/20230216024045_face.jpg',NULL,'2023-02-16 01:34:20','2023-02-16 04:44:24'),(4,'g@g.g','첫번째','9902165140fc8c35cfb016cdd5ae7d3fc6783d129e8311b549929e978e248736541f5b4b0503eda7622e3f6eda47fde35fffa14c2803a62141eba20579df419f','spring','안녕\r\n나는\r\n배중권이야','images/20230216072715_3.jpg','','2023-02-16 02:06:24','2023-02-16 07:27:15'),(5,'gg@g.g','두번째','9902165140fc8c35cfb016cdd5ae7d3fc6783d129e8311b549929e978e248736541f5b4b0503eda7622e3f6eda47fde35fffa14c2803a62141eba20579df419f','spring',NULL,'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',NULL,'2023-02-16 02:19:59','2023-02-16 02:19:59'),(6,'testtest@gmail.com','제이크','c08feb38bd42963375f925ada5e2f7e032584c8ef0278ccc9805afaaf56a9252178eb832c5f2a8ebb6dd412124ac761346c18d70e808b706cd00429ea918de60','spring',NULL,'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',NULL,'2023-02-16 07:29:10','2023-02-16 07:29:10');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
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
