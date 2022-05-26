from psycopg import sql

from data import data_manager


def get_shows():
    return data_manager.execute_select(sql.SQL(
        """
        SELECT id, title
        FROM shows
        """))


def get_fifteen_highest_rated_shows(order_by='rating', order='desc', limit=0, offset=0):
    return data_manager.execute_select(sql.SQL(
        """
        SELECT s.id, s.title, s.year, s.runtime, s.homepage, s.trailer,
            to_char(s.rating::float, '0.9') as rating,
            STRING_AGG(genres.name, ', ' ORDER BY genres.name) as genres
        FROM shows as s
        JOIN show_genres on s.id = show_genres.show_id
        JOIN genres on show_genres.genre_id = genres.id
        GROUP BY s.id
        ORDER BY case when %(order)s = 'asc' then {order_by} end ASC, case when %(order)s = 'desc' then {order_by} end DESC
        LIMIT %(limit)s
        OFFSET %(offset)s
        """).format(order_by=sql.Identifier(order_by)),
                                       {'order': order,
                                        'limit': limit,
                                        'offset': offset})


def get_show_count():
    return data_manager.execute_select(sql.SQL(
        """
        SELECT COUNT(*)
        FROM shows
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
           ARRAY_TO_STRING(ARRAY_AGG(DISTINCT genres.name), ',') AS genres,
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
    return data_manager.execute_select(sql.SQL(
        """
        SELECT season_number AS season_num,
           title,
           overview
        FROM seasons
        WHERE show_id = {s_id}
        """).format(s_id=sql.Literal(show_id)))
