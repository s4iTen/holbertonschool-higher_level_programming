-- This script list the number of the records with the same score in the table
-- and it is ordered by descending count
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score ORDER BY number DESC;