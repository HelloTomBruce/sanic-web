-- MySQL dump 10.13  Distrib 5.7.23, for Win64 (x86_64)
--
-- Host: localhost    Database: notice
-- ------------------------------------------------------
-- Server version	5.7.23-log

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
-- Current Database: `notice`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `notice` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `notice`;

--
-- Table structure for table `notice`
--

DROP TABLE IF EXISTS `notice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `notice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=116 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notice`
--

LOCK TABLES `notice` WRITE;
/*!40000 ALTER TABLE `notice` DISABLE KEYS */;
INSERT INTO `notice` VALUES (45,'西京学院2019年硕士生调剂公告https://yz.chsi.com.cn/kyzx/yxzc'),(46,'延安大学2019年硕士研究生招生预调剂公告https://yz.chsi.com.cn/kyzx/yxzc'),(47,'中国计量大学2019年攻读硕士学位研究生调剂预报名https://yz.chsi.com.cn/kyzx/yxzc'),(48,'福建师范大学关于2019年硕士研究生招生考试成绩查询和调剂有关事项的通知https://yz.chsi.com.cn/kyzx/yxzc'),(49,'江苏师范大学2019年硕士研究生调剂预告及相关说明http://yjsy.jsnu.edu.cn/sszs/list.htm'),(50,'2019年硕士研究生初试成绩查询及调剂相关说明http://yjsy.nwnu.edu.cn/2713/list.htm'),(51,'长春师范大学2019年硕士研究生拟接收调剂信息                     \n            http://yjs.ccsfu.edu.cn/zsgz/zsjz.htm'),(52,'音乐学院2019年硕士研究生招生调剂预通知http://yz.ahnu.edu.cn/4472'),(53,'马克思主义学院2019年硕士研究生招生调剂预通知http://yz.ahnu.edu.cn/4472'),(54,'环工学院关于接收2019年硕士研究生调剂的通知http://yz.ahnu.edu.cn/4472'),(55,'化材学院2019年硕士研究生招生调剂公告http://yz.ahnu.edu.cn/4472'),(56,'生命科学学院关于接收2019年硕士研究生调剂的通知http://yz.ahnu.edu.cn/4472'),(57,'辽宁石油化工大学2019年硕士研究生预调剂的通知https://yz.chsi.com.cn/kyzx/tjxx/'),(58,'黑龙江省社会科学院2019年硕士研究生招生调剂说明https://yz.chsi.com.cn/kyzx/tjxx/'),(59,'天津外国语大学2019年各学院（所）硕士研究生预调剂的通知https://yz.chsi.com.cn/kyzx/tjxx/'),(60,'曲阜师范大学2019年硕士研究生预调剂信息https://yz.chsi.com.cn/kyzx/tjxx/'),(61,'北京市劳动保护科学研究所2019年硕士研究生调剂公告https://yz.chsi.com.cn/kyzx/tjxx/'),(62,'北京农学院2019年接收研究生考生调剂通知（一）https://yz.chsi.com.cn/kyzx/tjxx/'),(63,'云南农业大学2019年接收调剂研究生的通告https://yz.chsi.com.cn/kyzx/tjxx/'),(64,'中国矿业大学2019年硕士研究生预调剂系统开通通知https://yz.chsi.com.cn/kyzx/tjxx/'),(65,'江苏师范大学2019年硕士研究生调剂预告及相关说明https://yz.chsi.com.cn/kyzx/tjxx/'),(66,'山东交通学院2019年硕士研究生调剂须知https://yz.chsi.com.cn/kyzx/tjxx/'),(67,'西安科技大学2019年硕士研究生调剂公告https://yz.chsi.com.cn/kyzx/tjxx/'),(68,'中南民族大学2019年硕士研究生预调剂公告https://yz.chsi.com.cn/kyzx/tjxx/'),(69,'2019年兰州大学调剂考生意向征集系统开通https://yz.chsi.com.cn/kyzx/tjxx/'),(70,'青岛大学生命科学学院2019年硕士研究生招生预调剂通知https://yz.chsi.com.cn/kyzx/tjxx/'),(71,'齐鲁工业大学（山东省科学院）2019年硕士研究生预调剂信息https://yz.chsi.com.cn/kyzx/tjxx/'),(72,'中国民用航空飞行学院2019年硕士研究生调剂信息https://yz.chsi.com.cn/kyzx/tjxx/'),(73,'福建工程学院2019年硕士研究生招生预调剂公告https://yz.chsi.com.cn/kyzx/tjxx/'),(74,'郑州烟草研究院2019年硕士研究生招生调剂信息https://yz.chsi.com.cn/kyzx/tjxx/'),(75,'中国地震局工程力学研究所2019年考研调剂信息 https://yz.chsi.com.cn/kyzx/tjxx/'),(76,'西南石油大学2019年考研调剂公告https://yz.chsi.com.cn/kyzx/tjxx/'),(77,'关于华南农业大学2019年硕士生预调剂系统开通的通知https://yz.chsi.com.cn/kyzx/tjxx/'),(78,'潍坊医学院关于2019年硕士研究生招生预调剂信息接收的通知https://yz.chsi.com.cn/kyzx/tjxx/'),(79,'武汉科技大学2019年接收硕士研究生调剂预报名公告https://yz.chsi.com.cn/kyzx/tjxx/'),(80,'山东科技大学2019年硕士研究生预调剂通知（持续更新）https://yz.chsi.com.cn/kyzx/tjxx/'),(81,'重庆交通大学2019年硕士研究生招生调剂公告（一）https://yz.chsi.com.cn/kyzx/tjxx/'),(82,'哈尔滨音乐学院2019年硕士研究生预调剂公告https://yz.chsi.com.cn/kyzx/tjxx/'),(83,'中国地质大学（北京）关于2019年接收“退役大学生士兵”专项硕士研究生调剂的通知https://yz.chsi.com.cn/kyzx/tjxx/'),(84,'重庆三峡学院2019年硕士研究生招生预调剂公?告https://yz.chsi.com.cn/kyzx/tjxx/'),(85,'天津理工大学2019年招收硕士研究生预调剂的通知https://yz.chsi.com.cn/kyzx/tjxx/'),(86,'北京石油化工学院2019年全日制硕士研究生招生预调剂通知https://yz.chsi.com.cn/kyzx/tjxx/'),(87,'天津体育学院2019年硕士研究生招生拟接受调剂专业的信息https://yz.chsi.com.cn/kyzx/tjxx/'),(88,'宜春学院2019年药学硕士专业学位研究生调剂公告https://yz.chsi.com.cn/kyzx/tjxx/'),(89,'2019年河北传媒学院专业学位硕士研究生调剂信息https://yz.chsi.com.cn/kyzx/tjxx/'),(90,'沈阳大学2019年硕士研究生调剂信息及奖助政策https://yz.chsi.com.cn/kyzx/tjxx/'),(91,'北华大学2019年硕士研究生招生预调剂公告https://yz.chsi.com.cn/kyzx/tjxx/'),(92,'燕山大学关于2019年硕士研究生调剂咨询工作安排的通知https://yz.chsi.com.cn/kyzx/tjxx/'),(93,'山东工商学院2019年硕士研究生预调剂公告https://yz.chsi.com.cn/kyzx/tjxx/'),(94,'北京有色金属研究总院2019年调剂信息https://yz.chsi.com.cn/kyzx/tjxx/'),(95,'大连海洋大学2019年硕士研究生预调剂系统正式开通https://yz.chsi.com.cn/kyzx/tjxx/'),(96,'大连民族大学2019年硕士研究生招生预调剂报名管理系统正式开通https://yz.chsi.com.cn/kyzx/tjxx/'),(97,'防灾科技学院2019年接收硕士专业学位研究生调剂通知https://yz.chsi.com.cn/kyzx/tjxx/'),(98,'沈阳化工大学2019年硕士研究生预调剂信息https://yz.chsi.com.cn/kyzx/tjxx/'),(99,'大连工业大学2019年硕士研究生调剂信息https://yz.chsi.com.cn/kyzx/tjxx/'),(100,'大连交通大学硕士研究生预调剂报名https://yz.chsi.com.cn/kyzx/tjxx/'),(101,'湖北文理学院2019年硕士研究生调剂预登记通知https://yz.chsi.com.cn/kyzx/tjxx/'),(102,'厦门理工学院关于2019年硕士研究生招生预调剂的通知https://yz.chsi.com.cn/kyzx/tjxx/'),(103,'福建师范大学关于2019年硕士研究生招生考试成绩查询和调剂有关事项的通知https://yz.chsi.com.cn/kyzx/tjxx/'),(104,'天津师范大学2019年硕士研究生招生接收调剂考生的相关通知                     \n            http://yjsy.tjnu.edu.cn/zsxx.htm'),(105,'天津师范大学2019年硕士研究生招生接收调剂考生的相关通知https://yz.chsi.com.cn/kyzx/tjxx/'),(106,'南京工业大学招收2019年优质调剂生的通告https://yz.chsi.com.cn/kyzx/tjxx/'),(107,'中国地震局地壳应力研究所2019年度研究生招生调剂公告https://yz.chsi.com.cn/kyzx/tjxx/'),(108,'北华大学2019年硕士研究生招生预调剂公告                     \n            http://grad.beihua.edu.cn/index/zxzx.htm'),(109,'2019年全国研究生入学考试齐齐哈尔大学拟调剂信息                     \n            http://yjs.qqhru.edu.cn/zsks.htm'),(110,'关于公布安庆师范大学2019年硕士研究生预调剂信息http://grad.aqnu.edu.cn/zxdt.htm'),(111,'东华理工大学2019年硕士研究生调剂信息http://yjsy.ecut.edu.cn/427/list.htm'),(112,'\n   曲阜师范大学2019年硕士研究生预调剂信息\n      http://yjs.qfnu.edu.cn/zsgz/sszs.htm'),(113,'2019年硕士研究生接收调剂说明http://adge.hpu.edu.cn/channels/4148.html'),(114,'2018年接收硕士研究生优秀生源调剂相关事项http://adge.hpu.edu.cn/channels/4148.html'),(115,'\n鲁东大学2019年硕士研究生招生调剂公告http://www.grad.ldu.edu.cn/index.htm');
/*!40000 ALTER TABLE `notice` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-04 17:27:50
