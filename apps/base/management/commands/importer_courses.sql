DROP TABLE IF EXISTS "public"."importer_courses";

CREATE TABLE "public"."importer_courses" (
  "id"  SERIAL NOT NULL,
  "action" varchar(2) COLLATE "default",
  "course_sec_id" varchar(128) DEFAULT NULL,
  "course" varchar(128) DEFAULT NULL,
  "section" varchar(128) DEFAULT NULL,
  "sec_short_title" varchar(128) DEFAULT NULL,
  "sec_desc" text,
  "sec_start_date" varchar(128) DEFAULT NULL,
  "sec_end_date" varchar(128) DEFAULT NULL,
  "dept" varchar(128) DEFAULT NULL,
  "sec_csxl" varchar(128) DEFAULT NULL,
  "sec_term" varchar(128) DEFAULT NULL,
  "short_title_formatted" varchar(128) DEFAULT NULL
)
WITH (OIDS=FALSE);

ALTER TABLE "public"."importer_courses" ADD PRIMARY KEY ("id") NOT DEFERRABLE INITIALLY IMMEDIATE;
