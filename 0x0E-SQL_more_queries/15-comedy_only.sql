-- Import the database dump from hbtn_0d_tvshows to your MySQL server: (same as 14-my_genres.sql)
-- Script that lists all Comedy shows in the database hbtn_0d_tvshows
SELECT tv_shows.title
FROM tv_show_genres
JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = "Comedy"
ORDER BY tv_shows.title ASC;
