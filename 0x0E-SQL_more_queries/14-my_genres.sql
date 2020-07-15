-- Import the database dump from hbtn_0d_tvshows to your MySQL server: (same as 13-count_shows_by_genre.sql)
-- Script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE title = 'Dexter'
ORDER BY name;
