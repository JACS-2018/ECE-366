-- MySQL dump 10.13  Distrib 5.7.21, for Linux (x86_64)
--
-- Host: localhost    Database: playgroundapr8
-- ------------------------------------------------------
-- Server version	5.7.21-0ubuntu0.16.04.1

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
-- Table structure for table `Friendships`
--

DROP TABLE IF EXISTS `Friendships`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Friendships` (
  `user_id_a` int(11) DEFAULT NULL,
  `user_id_b` int(11) DEFAULT NULL,
  `status` bit(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Friendships`
--

LOCK TABLES `Friendships` WRITE;
/*!40000 ALTER TABLE `Friendships` DISABLE KEYS */;
INSERT INTO `Friendships` VALUES (1,2,'\0'),(1,4,''),(1,3,'\0'),(2,3,''),(2,5,''),(3,5,'\0'),(5,1,'\0'),(4,3,''),(4,2,'\0');
/*!40000 ALTER TABLE `Friendships` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Posts`
--

DROP TABLE IF EXISTS `Posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Posts` (
  `post_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_a` int(11) DEFAULT NULL,
  `user_b` int(11) DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  `content` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`post_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Posts`
--

LOCK TABLES `Posts` WRITE;
/*!40000 ALTER TABLE `Posts` DISABLE KEYS */;
INSERT INTO `Posts` VALUES (10,1,2,'2018-04-10 15:01:36','hehe'),(11,2,3,'2018-04-10 15:01:36','hi bff'),(12,3,2,'2018-04-10 15:01:36','hello to you too bff');
/*!40000 ALTER TABLE `Posts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(20) DEFAULT NULL,
  `last_name` varchar(30) DEFAULT NULL,
  `username` varchar(30) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  `pro_pic` varchar(30) DEFAULT NULL,
  `about` varchar(150) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `signup_date` datetime DEFAULT NULL,
  `active` bit(1) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'Cardy','Wei','cwei1','hehexd',NULL,NULL,'hehe@gmail.com','2018-04-10 03:08:36',''),(2,'Jas','Tea','jtangqt','heh',NULL,NULL,'tang@cooper.edu','2018-04-10 03:08:36',''),(3,'sam','cheng','scheng839','wow',NULL,NULL,'scheng839@gmail.com','2018-04-10 04:36:12',''),(4,'alex','hu','enigmamemory','cupnoodles',NULL,NULL,'hu5@cooper.edu','2018-04-10 04:36:12',''),(5,'eric','n','eric.ng.501','hehe',NULL,NULL,'501@col.edu','2018-04-10 04:36:12','');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-04-10 15:46:03
