-- This script lis all the names from the states and the cities tables that have the same id
SELECT c.`id`, c.`name`, s.`name` FROM `cities` AS c INNER JOIN `states` AS s ON c.`state_id` = s.`id`
ORDER BY c.`id`;