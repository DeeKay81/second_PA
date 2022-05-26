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


def get_show_details(show_id):
    return data_manager.execute_select(sql.SQL(
        """
        SELECT shows.id,
           shows.title,
           shows.year,
           shows.overview,
           CASE
               WHEN shows.runtime > 60 THEN CONCAT(CAST((shows.runtime / 60) AS text), 'h', ' ',
                                                        CAST((shows.runtime % 60) AS text), 'min')
               WHEN shows.runtime = 60 THEN '1h'
               ELSE CONCAT(shows.runtime::text, 'min')
               END                                                  runtime,
           ROUND(shows.rating, 1)::VARCHAR                       AS rating,
           ARRAY_TO_STRING(ARRAY_AGG(DISTINCT genres.name), ', ') AS genres,
           shows.trailer,
           shows.homepage,
           (SELECT ARRAY_AGG(actors.name ORDER BY show_characters.id)
            FROM shows
                     LEFT JOIN show_characters ON shows.id = show_characters.show_id
                     LEFT JOIN actors ON show_characters.actor_id = actors.id
            WHERE shows.id = {id}
            GROUP BY shows.id)                                   AS actors
        FROM shows
                 LEFT JOIN show_genres ON shows.id = show_genres.show_id
                 LEFT JOIN genres ON show_genres.genre_id = genres.id
                 LEFT JOIN show_characters ON shows.id = show_characters.show_id
                 LEFT JOIN actors ON show_characters.actor_id = actors.id
        WHERE shows.id = {id}
        GROUP BY shows.id
        """).format(id=sql.Literal(show_id)), fetchall=False)


def get_seasons(show_id):
    return data_manager.execute_select(sql.SQL("""
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

