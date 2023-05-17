-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
SELECT title FROM tv_shows
WHERE tv_shows.id NOT IN (
	SELECT tv_show_genres.show_id FROM tv_show_genres
	JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
	WHERE tv_genres.name = "Comedy"
)
ORDER BY tv_shows.title;
