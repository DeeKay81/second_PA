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


def get_genres_detail(genre_id):
    return data_manager.execute_select(sql.SQL(
        f"""
        SELECT genres.id, genres.name AS genre,
        shows.title,
        ROUND(shows.rating::numeric, 1) AS rating,
        DATE_PART('year', shows.year::date) AS year,
        COUNT(actors.name) AS actor_count
        FROM genres
            JOIN show_genres ON genres.id = show_genres.genre_id
            JOIN shows ON shows.id = show_genres.show_id
            JOIN show_characters ON shows.id = show_characters.show_id
            JOIN actors ON actors.id = show_characters.actor_id
        WHERE genres.id = {genre_id}
        GROUP BY genres.id, shows.id
        HAVING COUNT(actors.name) < 20;
        """), {'genre_id': genre_id})
