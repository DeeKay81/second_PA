from psycopg import sql

from data import data_manager


def get_shows():
    return data_manager.execute_select(sql.SQL(
        """
        SELECT id, title 
        FROM shows;
        """))


def get_all_shows_table():
    return data_manager.execute_select(sql.SQL(
        """
        SELECT shows.id,
        shows.title,
        DATE_PART('year', shows.year::date) AS year,
        shows.runtime,
        ROUND(shows.rating::numeric, 1) AS rating,
        string_agg(genres.name, ', '
            ORDER BY genres.name) genres,
        shows.trailer,
        shows.homepage
        FROM shows
             JOIN show_genres ON shows.id = show_genres.show_id
             JOIN genres ON genres.id = show_genres.genre_id
        GROUP BY shows.id
        ORDER BY rating DESC
        """))


def get_actors():
    return data_manager.execute_select(sql.SQL(
        """
        SELECT id, name
        FROM actors;
        """))


def get_episodes():
    return data_manager.execute_select(sql.SQL(
        """
        SELECT id, title
        FROM episodes;
        """))


def get_genres():
    return data_manager.execute_select(sql.SQL(
        """
        SELECT id, name
        FROM genres;
        """))


def get_seasons():
    return data_manager.execute_select(sql.SQL(
        """
        SELECT id, title
        FROM seasons;
        """))


def get_all_seasons_table():
    return data_manager.execute_select(sql.SQL(
        """
        SELECT seasons.id,
        seasons.title AS season_title,
        seasons.season_number,
        seasons.overview,
        shows.title AS show_title
        FROM seasons JOIN shows ON seasons.show_id = shows.id
        WHERE show_id = shows.id
        """))
