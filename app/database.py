import mysql.connector
from config import db_connection_config


class Database():

    def __init__(self):
        config = self.get_congif()
        self._conn = mysql.connector.connect(**config)
        self._cursor = self._conn.cursor()
        print("MySQL Database connection successful")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def get_congif(self):
        return db_connection_config()

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        print("Query successful")
        return self.cursor.column_names, self.fetchall()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor
