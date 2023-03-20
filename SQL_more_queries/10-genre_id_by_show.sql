-- This script list all shows in hbtn_0d_tvshows databases
SELECT s.title, gen.show_id FROM tv_shows AS s
 INNER JOIN tv_show_genres AS gen ON s.id = gen.show_id
 ORDER BY s.title ASC , gen.show_id ASC;