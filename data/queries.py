from psycopg import sql

from data import data_manager


def get_shows():
    return data_manager.execute_select(sql.SQL(
        """
        SELECT id, title
        FROM shows;
        """))


def get_():
    return None