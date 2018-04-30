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
INSERT INTO `Friendships` VALUES (12,13,'\0'),(14,13,''),(15,13,'\0'),(16,13,'\0'),(17,13,'\0'),(18,13,''),(19,13,''),(20,13,''),(12,15,''),(15,19,'\0'),(12,18,''),(12,17,''),(14,16,''),(12,14,''),(12,12,'\0'),(14,20,'\0'),(14,19,'\0'),(15,18,'\0');
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
  `username_a` varchar(30) DEFAULT NULL,
  `username_b` varchar(30) DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  `content` text,
  PRIMARY KEY (`post_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Posts`
--

LOCK TABLES `Posts` WRITE;
/*!40000 ALTER TABLE `Posts` DISABLE KEYS */;
INSERT INTO `Posts` VALUES (1,14,12,'scheng829','cwei3','2018-04-30 16:26:00','once upon a time'),(2,15,12,'enigmamemoryg','cwei3','2018-04-30 16:26:00','there was a person'),(3,18,12,'sabooap','cwei3','2018-04-30 16:26:00','who wanted to eat '),(4,17,12,'tritus','cwei3','2018-04-30 16:26:00','cup noooooodles all the time'),(5,15,12,'enigmamemoryg','cwei3','2018-04-30 16:26:00','and his name was........ exdee');
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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (12,'Cardy','Wei','cwei3','cardywei','','5V ground','wei@cooper.edu','2018-04-24 18:54:46',''),(13,'Jasmine','Tang','jtangqt','jasminetang','','Friends dont harrass other friends.','tang@cooper.edu','2018-04-24 18:54:46',''),(14,'sam','cheng','scheng829','samcheng','','Watch my dance moves','scheng839@gmail.com','2018-04-24 18:54:46',''),(15,'alex','hu','enigmamemoryg','alexhu','','AHH NLP','hu5@cooper.edu','2018-04-24 18:54:46',''),(16,'casey','he','squishybluewristbutt','caseyhe','','ROCK CLIMBING','he@cooper.edu','2018-04-24 18:54:46',''),(17,'joey','benghaasllkfdldaflaf','tritus','joey','','@everyone, league???','jbengtlfdf15@gmail.com','2018-04-24 18:54:46',''),(18,'jeremiah','pratt','sabooap','jeremiahpratt','','Again, our sincere apologies to the families who went home disappointed.','pratt@cooper.edu','2018-04-24 18:54:46',''),(19,'dan','park','solarien','danpark','','Join the army with me!','park100000@cooper.edu','2018-04-24 18:54:46',''),(20,'chris','watkins','WATGOIN','chriswatkins','','I am a front end developer','watkins@cooper.edu','2018-04-24 18:54:46','');
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

-- Dump completed on 2018-04-30 16:27:22
