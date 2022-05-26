from data import data_manager as dm
from psycopg import sql


def get_shows():
    return dm.execute_select('SELECT id, title FROM shows;')


def get_most_rated_shows(column='rating', order='desc', limit=0, offset=0):
    return dm.execute_select(sql.SQL(
        """
        SELECT s.id, s.title, s.year, s.runtime, s.homepage, s.trailer,
        to_char(s.rating::float, '0.9') as rating,
        string_agg(genres.name, ', ' ORDER BY genres.name) as genres
        FROM shows as s
        JOIN show_genres on s.id = show_genres.show_id
        JOIN genres on show_genres.genre_id = genres.id
        GROUP BY s.id
        ORDER BY case when %(order)s = 'asc' then {column} end ASC, case when %(order)s = 'desc' then {column} end DESC
        LIMIT %(limit)s
        OFFSET %(offset)s
        """).format(column=sql.Identifier(column)),
                                       {'order': order,
                                        'limit': limit,
                                        'offset': offset}
                                       )


def get_show_count():
    return dm.execute_select(
        'SELECT COUNT(*) '
        'FROM shows;')


def get_show_details(show_id):
    return dm.execute_select(sql.SQL(
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
    return dm.execute_select(sql.SQL("""
        SELECT season_number AS snum,
               title,
               overview
        FROM seasons
        WHERE show_id = {s_id}
        """).format(s_id=sql.Literal(show_id)))
