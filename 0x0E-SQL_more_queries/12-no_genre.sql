-- Import the database dump from hbtn_0d_tvshows to your MySQL server: (same as 11-genre_id_all_shows.sql)
-- Script that lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id is NULL
ORDER BY title, genre_id;
