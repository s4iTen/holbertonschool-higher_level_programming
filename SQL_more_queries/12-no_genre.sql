-- This script list all shows in hbtn_0d_tvshows databases
SELECT s.title, gen.genre_id FROM tv_shows AS s
 LEFT JOIN tv_show_genres AS gen ON s.id = gen.show_id
 WHERE gen.genre_id IS NULL
 ORDER BY s.title ASC, gen.genre_id ASC;