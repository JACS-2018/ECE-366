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
INSERT INTO `Friendships` VALUES (3,2,''),(4,2,'\0'),(5,2,'\0'),(6,2,'\0'),(7,2,''),(8,2,''),(9,2,''),(1,4,''),(4,8,'\0'),(1,7,'\0'),(1,6,''),(3,5,''),(1,3,''),(1,1,'\0'),(3,9,'\0'),(3,8,'\0'),(4,7,'');
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
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Posts`
--

LOCK TABLES `Posts` WRITE;
/*!40000 ALTER TABLE `Posts` DISABLE KEYS */;
INSERT INTO `Posts` VALUES (1,3,1,'scheng829','cwei3','2018-04-30 16:26:00','once upon a time'),(2,4,1,'enigmamemory','cwei3','2018-04-30 16:26:00','there was a person'),(3,7,1,'sabooap','cwei3','2018-04-30 16:26:00','who wanted to eat '),(5,4,1,'enigmamemory','cwei3','2018-04-30 16:26:00','and his name was........ exdee'),(6,3,2,'scheng829','jtangqt','2018-04-30 18:29:44','once upon a time'),(7,2,2,'jtangqt','jtangqt','2018-04-30 18:29:44','there was a person'),(8,7,2,'sabooap','jtangqt','2018-04-30 18:29:44','who wanted to eat '),(9,6,2,'tritus','jtangqt','2018-04-30 18:29:44','cup noooooodles all the time'),(10,5,2,'squishybluewristbutt','jtangqt','2018-04-30 18:29:44','and his name was........ exdee'),(11,4,4,'enigmamemory','enigmamemory','2018-04-30 18:29:44','and his name was........ exdee'),(12,1,4,'cwei3','enigmamemory','2018-04-30 18:29:44','and his name was........ exdee'),(13,1,2,'cwei3','jtangqt','2018-04-30 18:29:44','and his name was........ exdee'),(14,19,13,'solarien','jtangqt','2018-04-30 18:29:44','YA LIKE JAZZ?'),(15,8,2,'solarien','jtangqt','2018-04-30 18:29:44','i know you do'),(16,7,4,'sabooap','enigmamemory','2018-04-30 21:38:25','i know you do'),(17,7,4,'sabooap','enigmamemory','2018-04-30 21:38:25','HEH');
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
  `bday` date DEFAULT NULL,
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
INSERT INTO `User` VALUES (1,'Cardy','Wei','cwei3','cardywei','','5V ground','UNDERWATER DOLPHIN CHARMER','2016-05-09','wei@cooper.edu','2018-05-01 01:17:28',''),(2,'Jasmine','Tang','jtangqt','jasminetang','','Friends dont harrass other friends.','supermodel','2016-05-09','tang@cooper.edu','2018-05-01 01:17:28',''),(3,'sam','cheng','scheng829','samcheng','','Watch my dance moves','professional dancer','2016-05-09','scheng839@gmail.com','2018-05-01 01:17:28',''),(4,'alex','hu','enigmamemory','alexhu','','AHH NLP','cooper union student','2016-05-09','hu5@cooper.edu','2018-05-01 01:17:28',''),(5,'casey','he','squishybluewristbutt','caseyhe','','ROCK CLIMBING','ALIVE','2016-05-09','he@cooper.edu','2018-05-01 01:17:28',''),(6,'joey','benghaasllkfdldaflaf','tritus','joey','','@everyone, league???','miner in data','2016-05-09','jbengtlfdf15@gmail.com','2018-05-01 01:17:28',''),(7,'jeremiah','pratt','sabooap','jeremiahpratt','','Again, our sincere apologies to the families who went home disappointed.','politician','2016-05-09','pratt@cooper.edu','2018-05-01 01:17:28',''),(8,'dan','park','solarien','danpark','','Join the army with me!','General of the ONE Korean Army','2016-05-09','park100000@cooper.edu','2018-05-01 01:17:28',''),(9,'dongkyu','kim','dongkyu0419','dongkyukim','','TRIVIAL','Professor Kirtman :POGGERS:','2016-05-09','kim800@cooper.edu','2018-05-01 01:17:28',''),(10,'minyoung','na','BSEintruder','minyoungna','','REEEEEEEEEEEEE','i want to be a puppy','2016-05-09','na4@cooper.edu','2018-05-01 01:17:28',''),(11,'brian','hong','th0m4s','brianhong','','66k+ groups','thomas','2016-05-09','bri@cooper.edu','2018-05-01 01:17:28',''),(12,'paul','kang','cheeseheadpk','paulkang','','I own a burger joint','Construction Worker/Bob the Builder','2016-05-09','kang3@cooper.edu','2018-05-01 01:17:28',''),(13,'chris','watkins','WATGOIN','chriswatkins','','I am a front end developer','full stack developer','2016-05-09','watkins@cooper.edu','2018-05-01 01:17:28','');
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

-- Dump completed on 2018-05-01  1:22:26
