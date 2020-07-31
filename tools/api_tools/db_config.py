import psycopg2
from .config import dbname, user, password, host


class ConnDB:
    @staticmethod
    def get_connect():
        conn = psycopg2.connect(dbname=dbname, user=user,
                                password=password,
                                host=host)
        return conn

    @staticmethod
    def get_cursor(conn):
        cursor = conn.cursor()
        return cursor

    @staticmethod
    def get_query_result(cursor, update):
        cursor.execute(f"SELECT mode FROM users WHERE userid = '{update.message.chat_id}'")
        query_result = cursor.fetchone()
        return query_result
