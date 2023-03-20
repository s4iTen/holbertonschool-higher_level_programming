-- This script list all the genre names and how many show have this genre
SELECT 
  g.name AS genre, 
  COUNT(sg.show_id) AS number_of_shows 
FROM 
  tv_genres g, 
  tv_show_genres sg 
WHERE 
  g.id = sg.genre_id 
GROUP BY 
  g.id 
ORDER BY 
  number_of_shows DESC;