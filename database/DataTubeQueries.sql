--Queries used to clean and merge data
--Create a table for US Videos
CREATE TABLE public."USVideos"(
    video_id text, trending_date text, title text, channel_title text, category_id int, 
    publish_time TIMESTAMP, tags text, views int, likes int, dislikes int,	comment_count int, 
    thumbnail_link text, comments_disabled varchar(100), ratings_disabled varchar(100), 
    video_error_or_removed varchar(100), description text);
--Import CSV
COPY public."USVideos" FROM  '/Library/PostgreSQL/14/doc/USVideo.csv’ DELIMITER ',' CSV HEADER;

--Handle unquoted newline found in csv 
* Add a page break in your excel file where your data ends.
* Select just next cell (empty cell) after your last data cell and go to File > Page Layout > Breaks > Insert Page Break.
* Save your csv file and import it again with pgadmin.

--Add a column
ALTER TABLE public."USVideos" ADD COLUMN country char(10);
UPDATE public."USVideos"
SET country  = 'US';
SELECT * FROM public."USVideos";

--Get rid of redundancy
SELECT
	video_id,
	MAX (views)
INTO "Videos" 
FROM
	"USVideos"
GROUP BY
	video_id;

--Create a table for Canada videos 
CREATE TABLE public."CAVideos"(
    video_id text, trending_date text, title text, channel_title text, category_id int, 
    publish_time TIMESTAMP, tags text, views int, likes int, dislikes int,	comment_count int, 
    thumbnail_link text, comments_disabled varchar(100), ratings_disabled varchar(100), 
    video_error_or_removed varchar(100), description text);

--Import CSV
COPY public."USVideos" FROM  '/Library/PostgreSQL/14/doc/CAVideo.csv’ DELIMITER ',' CSV HEADER;

--Handle unquoted newline found in csv 
* Add a page break in your excel file where your data ends.
* Select just next cell (empty cell) after your last data cell and go to File > Page Layout > Breaks > Insert Page Break.
* Save your csv file and import it again with pgadmin.

--Add a column
ALTER TABLE public."CAVideos" ADD COLUMN country char(10);
UPDATE public."CAVideos"
SET country  = 'CA';
SELECT * FROM public."CAVideos";

INSERT INTO
    "Videos"
SELECT
	video_id,
	MAX (views)
FROM
	“CAVideos"
GROUP BY
	video_id;


-- Create the DataTube Table
CREATE TABLE public."DataTube"(
    video_id text, trending_date text, title text, channel_title text, category_id int, 
    publish_time TIMESTAMP, tags text, views int, likes int, dislikes int,	comment_count int, 
    thumbnail_link text, comments_disabled varchar(100), ratings_disabled varchar(100), 
    video_error_or_removed varchar(100), description text,  country char(10), video_id2 text, max int);

-- Insert the cleaned data  
INSERT INTO "DataTube"
SELECT *
FROM "USVideos"
INNER JOIN "Videos"
ON "USVideos".video_id = "Videos".video_id AND "USVideos".views = "Videos".max;

INSERT INTO "DataTube"
SELECT * 
FROM "CAVideos"
INNER JOIN "Videos"
ON "CAVideos".video_id = "Videos".video_id AND "CAVideos".views = "Videos".max;