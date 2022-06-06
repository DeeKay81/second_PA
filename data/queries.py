from psycopg import sql

from data import data_manager


def get_shows():
    return data_manager.execute_select(sql.SQL(
        """
        SELECT id, title
        FROM shows;
        """))


def get_genres():
    return data_manager.execute_select(sql.SQL(
        """
        SELECT genres.id, genres.name AS genre
        FROM genres;
        """))


def get_mystery_horror():
    return data_manager.execute_select(sql.SQL(
        """
        SELECT shows.id,
        shows.title,
        ARRAY_AGG(genres.name) AS genres,
        DATE_PART('year', shows.year::date) AS year,
        ROUND(shows.rating::numeric, 3) AS rating,
        shows.overview
        FROM show_genres
            JOIN genres ON show_genres.genre_id = genres.id
            JOIN shows ON show_genres.show_id = shows.id
        WHERE genres.name = 'Mystery' OR genres.name = 'Horror'
        GROUP BY shows.id, genres.name, shows.title
        ORDER BY shows.title;
        """
    ))
