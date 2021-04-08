from dotenv import load_dotenv
from os import environ


def connection_config():
    load_dotenv()

    return {
        'host': environ.get("DB_HOST"),
        'port': environ.get("DB_PORT"),
        'user': environ.get("DB_USER"),
        'passwd': environ.get("DB_PWD"),
        'db': environ.get("DB_NAME")
    }
