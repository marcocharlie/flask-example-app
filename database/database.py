import mysql.connector
from mysql.connector import Error
from .config import db_connection_config


class Database():

    connection = None

    # Create db connection
    def create_connection(self):

        # get connection config
        db_config = db_connection_config()

        try:
            self.connection = mysql.connector.connect(
                host=db_config['host'],
                user=db_config['user'],
                passwd=db_config['passwd'],
                database=db_config['db']
            )
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")

        return self.connection

    # Create new db

    def create_database(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            print("Database created successfully")
        except Error as err:
            print(f"Error: '{err}'")

    # Run query on db for creating tables and insert data

    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")

    # Run query for reading data

    def read_query(self, query):
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query)
            field_names = cursor.column_names
            results = cursor.fetchall()
            cursor.close()
            return field_names, results
        except Error as err:
            print(f"Error: '{err}'")
