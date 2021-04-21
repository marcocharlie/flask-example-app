import mysql.connector
from config import db_connection_config


class Database():

    def __init__(self):
        config = db_connection_config()
        self._conn = mysql.connector.connect(**config)
        self._cursor = self._conn.cursor()
        print("MySQL Database connection successful")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

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
