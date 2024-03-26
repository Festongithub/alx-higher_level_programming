#!/usr/bin/mysql
--  lists all records of the table second_table of the database hbtn_0c_0
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 0
ORDER BY `score` DESC;
