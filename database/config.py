from dotenv import load_dotenv
from os import environ


def db_connection_config():
    load_dotenv()

    return {
        'host': environ.get("DB_HOST"),  # <YOUR-MYSQL-HOST>
        'port': environ.get("DB_PORT"),  # <YOUR-MYSQL-PORT>
        'user': environ.get("DB_USER"),  # <YOUR-MYSQL-USER>
        'passwd': environ.get("DB_PWD"),  # <YOUR-MYSQL-PWD>
        'db': environ.get("DB_NAME")  # nodes
    }
