from dotenv import load_dotenv
from os import environ


def connection_config():
    load_dotenv()

    return {
        'host': environ.get("DB_HOST"),  # localhost
        'port': environ.get("DB_PORT"),  # 3306
        'user': environ.get("DB_USER"),  # root
        'passwd': environ.get("DB_PWD"),  # secret mysql password
        'db': environ.get("DB_NAME")  # nodes
    }
