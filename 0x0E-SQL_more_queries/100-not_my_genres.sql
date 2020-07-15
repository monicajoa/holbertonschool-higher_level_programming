-- Import the database dump from hbtn_0d_tvshows to your MySQL server: (same as 16-shows_by_genre.sql)
-- Script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT name
FROM tv_genres
WHERE name NOT IN (
SELECT tg.name
FROM tv_shows ts
JOIN tv_show_genres tsg ON ts.id = tsg.show_id
JOIN tv_genres tg ON tsg.genre_id = tg.id
WHERE ts.title = 'Dexter')
ORDER BY name;
