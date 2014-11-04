/*
 Navicat PostgreSQL Data Transfer

 Source Server         : local
 Source Server Version : 90301
 Source Host           : localhost
 Source Database       : ccademo
 Source Schema         : public

 Target Server Version : 90301
 File Encoding         : utf-8

 Date: 11/03/2014 13:44:12 PM
*/

-- ----------------------------
--  Table structure for importer_users
-- ----------------------------
DROP TABLE IF EXISTS "public"."importer_users";
CREATE TABLE "public"."importer_users" (
	"id"  SERIAL NOT NULL,
	"action" varchar(2) COLLATE "default",
	"person_id" int4,
	"section_id" int4,
	"first_name" varchar(24) COLLATE "default",
	"last_name" varchar(24) COLLATE "default",
	"email" varchar(32) COLLATE "default",
	"photo_url" varchar(140) COLLATE "default",
	"person_type" varchar(12) COLLATE "default"
)
WITH (OIDS=FALSE);
-- ALTER TABLE "public"."importer_users" OWNER TO "shacker";

-- ----------------------------
--  Primary key structure for table importer_users
-- ----------------------------
ALTER TABLE "public"."importer_users" ADD PRIMARY KEY ("id") NOT DEFERRABLE INITIALLY IMMEDIATE;

