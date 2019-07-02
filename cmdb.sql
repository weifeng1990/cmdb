/*
 Navicat Premium Data Transfer

 Source Server         : 192.168.2.10
 Source Server Type    : MySQL
 Source Server Version : 50644
 Source Host           : 192.168.2.10:3306
 Source Schema         : cmdb

 Target Server Type    : MySQL
 Target Server Version : 50644
 File Encoding         : 65001

 Date: 02/07/2019 22:10:35
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for DEVICE
-- ----------------------------
DROP TABLE IF EXISTS `DEVICE`;
CREATE TABLE `DEVICE`  (
  `ID` int(32) UNSIGNED NOT NULL AUTO_INCREMENT,
  `NAME` varchar(16) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `DESCRIPTION` varchar(255) CHARACTER SET utf8 COLLATE utf8_german2_ci NOT NULL DEFAULT '',
  `IP` varchar(1024) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `TYPE` int(3) NOT NULL COMMENT '1表示为ssh,2表示为telnet，3表示http，4表示snmp',
  `PORT` int(255) UNSIGNED NOT NULL,
  `USER` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `PASSWORD` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `PRODUCTION` varchar(255) CHARACTER SET utf8 COLLATE utf8_german2_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of DEVICE
-- ----------------------------
INSERT INTO `DEVICE` VALUES (1, 'server1', '', '192.168.2.20', 1, 22, 'root', 'admin', '');
INSERT INTO `DEVICE` VALUES (4, 'server4', '', '192.168.2.20', 1, 22, 'root', 'admin', '');
INSERT INTO `DEVICE` VALUES (5, 'server5', '', '192.168.2.20', 1, 22, 'root', 'admin', '');

SET FOREIGN_KEY_CHECKS = 1;
