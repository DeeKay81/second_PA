from psycopg import sql

from data import data_manager as dm


def get_shows():
    return dm.execute_select(sql.SQL(
        """
        SELECT id, title
        FROM shows
        """))


def get_fifteen_highest_rated_shows():
    return dm.execute_select(sql.SQL(
        """
        SELECT shows.id,
        shows.title,
        DATE_PART('year', shows.year::date) AS year,
        shows.runtime,
        ROUND(shows.rating::numeric, 1) AS rating,
        string_agg(genres.name, ','
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
    return dm.execute_select(sql.SQL(
        """
        SELECT shows.id, 
        shows.title, 
        shows.runtime,
        shows.trailer,
        ROUND(shows.rating::numeric, 1) rating,
        string_agg(DISTINCT genres.name, ',' ORDER BY genres.name) genres,
        shows.overview,
        array_to_string((array_agg(DISTINCT actors.name))[1:3], ', ') Actors
        FROM shows
        JOIN show_characters on shows.id = show_characters.show_id
        JOIN show_genres on shows.id = show_genres.show_id
        JOIN genres on genres.id = show_genres.genre_id
        JOIN actors on actors.id = show_characters.actor_id
        WHERE shows.id = {show_id}
        GROUP BY shows.id
        ORDER BY shows.id ASC
        """).format(show_id=sql.Literal(show_id)))


def get_seasons(show_id):
    return dm.execute_select(sql.SQL(
        """
        SELECT seasons.season_number, seasons.title, COALESCE(seasons.overview, '') as overview
        FROM seasons
        JOIN shows on shows.id = seasons.show_id
        WHERE shows.id = {show_id}
        GROUP BY shows.id, seasons.id;
        """).format(show_id=sql.Literal(show_id)))


def get_show_count():
    return dm.execute_select(sql.SQL(
        """
        SELECT COUNT(*)
        FROM shows
        """))


def get_hundred_actors():
    return dm.execute_select(sql.SQL(
        """
        SELECT REGEXP_REPLACE(actors.name, '\s+\S+$', '') AS firstname
        FROM actors
        ORDER BY actors.birthday
        LIMIT 100
        """))


def get_shows_by_actor_name(name):
    name = name + '%'
    print(name)
    return dm.execute_select(sql.SQL(
        """
        SELECT string_agg(shows.title, '  |  ') AS title
        FROM shows
        JOIN show_characters on shows.id = show_characters.show_id
        JOIN actors on show_characters.actor_id = actors.id
        WHERE actors.name LIKE {firstname}
        """).format(firstname=sql.Literal(name)))


def get_genres_by_limit():
    return dm.execute_select(sql.SQL(
        """
        Select g.name,s.title,
       ROUND(s.rating::numeric,1) as rating,
       DATE_PART('year', s.year::date) as year,
       count(a.name) as actor_count
    FROM genres g
    JOIN show_genres sg on g.id = sg.genre_id
    JOIN shows s on s.id = sg.show_id
    JOIN show_characters sc on s.id = sc.show_id
    JOIN actors a on a.id = sc.actor_id
    GROUP BY g.id, s.id
    HAVING count(a.name)  < 20;
        """
    ))