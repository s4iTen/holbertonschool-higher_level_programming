-- This script list all records of the table ordered by descending score
-- and score must be >= 10
 SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;