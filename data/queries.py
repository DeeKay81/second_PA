from psycopg import sql

from data import data_manager


def get_shows():
    return data_manager.execute_select(sql.SQL(
        """
        SELECT id, title
        FROM shows
        """))


def get_fifteen_highest_rated_shows():
    return data_manager.execute_select(sql.SQL(
        """
        SELECT shows.id,
        shows.title,
        DATE_PART('year', shows.year::date) AS year,
        shows.runtime,
        ROUND(shows.rating::numeric, 1) AS rating,
        string_agg(genres.name, ','
            ORDER BY genres.name ASC) genres,
        shows.trailer,
        shows.homepage
        FROM shows
             JOIN show_genres ON shows.id = show_genres.show_id
             JOIN genres ON genres.id = show_genres.genre_id
        GROUP BY shows.id
        ORDER BY rating DESC
        """))


def get_show_details(show_id):
    return data_manager.execute_select(sql.SQL(
        """
        SELECT shows.id,
        shows.title,
        shows.runtime,
        shows.trailer,
        ROUND(shows.rating::numeric, 1) rating,
        string_agg(DISTINCT genres.name, ',' ORDER BY genres.name ASC) genres,
        shows.overview,
        array_to_string((array_agg(DISTINCT actors.name))[1:3], ', ') Actors
        FROM shows
        JOIN show_characters on shows.id = show_characters.show_id
        JOIN show_genres on shows.id = show_genres.show_id
        JOIN genres on genres.id = show_genres.genre_id
        JOIN actors on actors.id = show_characters.actor_id
        WHERE shows.id = {show_id}
        GROUP BY shows.id
        """).format(show_id=sql.Literal(show_id)))


def get_seasons(show_id):
    return data_manager.execute_select(sql.SQL(
        """
        SELECT seasons.season_number, seasons.title, COALESCE(seasons.overview, '') as overview
        FROM seasons
        JOIN shows on shows.id = seasons.show_id
        WHERE shows.id = {show_id}
        GROUP BY shows.id, seasons.id;
        """).format(show_id=sql.Literal(show_id)))


def get_show_count():
    return data_manager.execute_select(sql.SQL(
        """
        SELECT COUNT(*)
        FROM shows
        """))


def get_hundred_actors():
    return data_manager.execute_select(sql.SQL(
        """
        SELECT a.name, string_agg(DISTINCT s.title, '#') AS titles, COUNT(*) as show_numbers 
        FROM actors a 
        JOIN show_characters sc on a.id = sc.actor_id 
        JOIN shows s on sc.show_id = s.id 
        GROUP BY a.name 
        ORDER BY show_numbers DESC 
        LIMIT 100;"""))
