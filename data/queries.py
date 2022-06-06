from psycopg import sql

from data import data_manager


def get_shows():
    return data_manager.execute_select(sql.SQL(
        """
        SELECT id, title
        FROM shows;
        """))


def get_details(show_id):
    return data_manager.execute_select(sql.SQL(
        f"""
        SELECT shows.id,
        show_characters.character_name,
        actors.name AS actor_name,
        DATE_PART('year', age(actors.birthday)) AS age
        FROM show_characters
        JOIN actors ON actors.id = show_characters.actor_id
        JOIN shows ON shows.id = show_characters.show_id
        WHERE shows.id = {show_id}
        """).format(show_id=sql.Literal(show_id)))


def get_trailer(show_id):
    return data_manager.execute_select(sql.SQL(
        f"""
        SELECT shows.trailer
        FROM shows
        WHERE shows.id = {show_id}
        """
    ).format(show_id=sql.Literal(show_id)), None, False)
