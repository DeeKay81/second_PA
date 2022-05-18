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


def get_hundred_actors():
    return data_manager.execute_select(sql.SQL(
        """
        SELECT split_part("name", ' ', 1 ) AS firstname 
        FROM actors
        ORDER BY actors.birthday LIMIT 100;
        """))


def get_actor_detail():
    return data_manager.execute_select(sql.SQL(
        """
        SELECT
        split_part("name", ' ', 1) AS firstname,
        array_agg(s.title) shows,
        a.birthday
        FROM show_characters sc
            JOIN actors a ON sc.actor_id = a.id
            JOIN shows s ON sc.show_id = s.id
        GROUP BY a.id
        ORDER BY a.birthday
        LIMIT 100;
        """))


def get_genres():
    return data_manager.execute_select(sql.SQL(
        """
        SELECT g.id, g.name as genre
        FROM genres g;
        """))


def get_genre_detailed(genre_id):
    return data_manager.execute_select(
        """
        Select g.id, g.name,s.title,
        ROUND(s.rating::numeric,1) as rating,
        DATE_PART('year', s.year::date) as year,
        count(a.name) as actor_count
        FROM genres g
        JOIN show_genres sg on g.id = sg.genre_id
        JOIN shows s on s.id = sg.show_id
        JOIN show_characters sc on s.id = sc.show_id
        JOIN actors a on a.id = sc.actor_id
        WHERE g.id = %(genre_id)s
        GROUP BY g.id, s.id
        HAVING count(a.name)  < 20;
        """, {"genre_id": genre_id})



def get_shows_by_rating():
    return data_manager.execute_select(sql.SQL(
        """
        SELECT shows.title, ROUND(shows.rating - 7.94, 2) AS rating
        FROM shows
             JOIN seasons on shows.id = seasons.show_id
             JOIN episodes on seasons.id = episodes.season_id
        GROUP BY shows.id
        ORDER BY COUNT(episodes.id)
        LIMIT 10;
        """))
