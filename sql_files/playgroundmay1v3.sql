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
INSERT INTO `Friendships` VALUES (1,1,'\0'),(1,7,'\0'),(5,1,'\0'),(3,2,''),(7,4,''),(6,2,''),(5,2,''),(4,1,''),(9,2,''),(8,2,''),(6,7,''),(1,2,''),(9,11,'\0'),(7,8,'\0'),(4,3,'\0'),(12,13,'\0'),(10,9,'\0'),(8,10,'\0'),(13,7,'\0'),(11,12,'\0'),(6,1,'\0');
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
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Posts`
--

LOCK TABLES `Posts` WRITE;
/*!40000 ALTER TABLE `Posts` DISABLE KEYS */;
INSERT INTO `Posts` VALUES (1,3,2,'scheng829','jtangqt','2018-05-01 04:43:28','once upon a time'),(2,1,1,'cwei3','cwei3','2018-05-01 04:43:28','there was a person'),(3,7,4,'sabooap','enigmamemory','2018-05-01 04:43:28','who wanted to eat '),(4,6,2,'tritus','jtangqt','2018-05-01 04:43:28','cup noooooodles all the time'),(5,5,2,'squishybluewristbutt','jtangqt','2018-05-01 04:43:28','and his name was........ exdee'),(6,4,4,'enigmamemory','enigmamemory','2018-05-01 04:43:28','and his name was........ exdee'),(7,1,4,'cwei3','enigmamemory','2018-05-01 04:43:28','and his name was........ exdee'),(8,9,2,'dongkyu0419','jtangqt','2018-05-01 04:43:28','and his name was........ exdee'),(9,8,2,'solarien','jtangqt','2018-05-01 04:43:28','YA LIKE JAZZ?'),(10,7,4,'sabooap','enigmamemory','2018-05-01 04:43:28','i know you do'),(11,4,1,'enigmamemory','cwei3','2018-05-01 04:43:28','HEH');
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
  `occupation` varchar(100) DEFAULT NULL,
  `bday` varchar(50) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `signup_date` datetime DEFAULT NULL,
  `active` bit(1) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'Cardy','Wei','cwei3','cardywei','','5V ground','UNDERWATER DOLPHIN CHARMER','2016-05-09','wei@cooper.edu','2018-05-01 04:42:47',''),(2,'Jasmine','Tang','jtangqt','jasminetang','','Friends dont harrass other friends.','supermodel','2016-05-09','tang@cooper.edu','2018-05-01 04:42:47',''),(3,'sam','cheng','scheng829','samcheng','','Watch my dance moves','professional dancer','2016-05-09','scheng839@gmail.com','2018-05-01 04:42:47',''),(4,'alex','hu','enigmamemory','alexhu','','AHH NLP','cooper union student','2016-05-09','hu5@cooper.edu','2018-05-01 04:42:47',''),(5,'casey','he','squishybluewristbutt','caseyhe','','ROCK CLIMBING','ALIVE','2016-05-09','he@cooper.edu','2018-05-01 04:42:47',''),(6,'joey','benghaasllkfdldaflaf','tritus','joey','','@everyone, league???','miner in data','2016-05-09','jbengtlfdf15@gmail.com','2018-05-01 04:42:47',''),(7,'jeremiah','pratt','sabooap','jeremiahpratt','','Again, our sincere apologies to the families who went home disappointed.','politician','2016-05-09','pratt@cooper.edu','2018-05-01 04:42:47',''),(8,'dan','park','solarien','danpark','','Join the army with me!','General of the ONE Korean Army','2016-05-09','park100000@cooper.edu','2018-05-01 04:42:47',''),(9,'dongkyu','kim','dongkyu0419','dongkyukim','','TRIVIAL','Professor Kirtman :POGGERS:','2016-05-09','kim800@cooper.edu','2018-05-01 04:42:47',''),(10,'minyoung','na','BSEintruder','minyuongna','','REEEEEEEEEEEEE','i want to be a puppy','2016-05-09','na4@cooper.edu','2018-05-01 04:42:47',''),(11,'brian','hong','th0m4s','brianhong','','66k+ groups','thomas','2016-05-09','bri@cooper.edu','2018-05-01 04:42:47',''),(12,'paul','kang','cheeseheadpk','paulkang','','I own a burger joint','Construction Worker/Bob the Builder','2016-05-09','kang3@cooper.edu','2018-05-01 04:42:47',''),(13,'chris','watkins','WATGOIN','chriswatkins','','I am a front end developer','full stack developer','2016-05-09','watkins@cooper.edu','2018-05-01 04:42:47','');
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

-- Dump completed on 2018-05-01  6:11:17
