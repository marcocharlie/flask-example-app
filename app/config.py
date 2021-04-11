from os import getenv


def db_connection_config():
    return {
        'host': getenv("DB_HOST"),
        'port': getenv("DB_PORT"),
        'user': getenv("DB_USER"),
        'password': getenv("DB_PWD"),
        'database': getenv("DB_NAME")
    }
