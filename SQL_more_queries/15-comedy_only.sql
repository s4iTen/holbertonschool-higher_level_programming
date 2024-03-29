-- This script list all the tv shows that have the genre Comedy
SELECT tv_shows.title AS title FROM tv_shows, tv_genres, tv_show_genres
WHERE 
    tv_genres.id = tv_show_genres.genre_id AND
    tv_shows.id = tv_show_genres.show_id AND
    tv_genres.name = "Comedy"
ORDER BY tv_shows.title ASC;