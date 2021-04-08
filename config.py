from os import getenv


def connection_config():
    return {
        'host': getenv("DB_HOST"),
        'port': getenv("DB_PORT"),
        'user': getenv("DB_USER"),
        'passwd': getenv("DB_PWD"),
        'db': getenv("DB_NAME")
    }
