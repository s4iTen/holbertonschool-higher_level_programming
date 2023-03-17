-- This script list all the records and ordered by the id and sorted
SELECT id, name FROM cities WHERE state_id IN(SELECT id FROM states WHERE name = 'California') ORDER BY id;