from os import getenv


def connection_config():

    db_host = getenv("DB_HOST")
    db_port = getenv("DB_PORT")
    db_user = getenv("DB_USER")
    db_pwd = getenv("DB_PWD")
    db_name = getenv("DB_NAME")

    return {
        'host': db_host,
        'port': db_port,
        'user': db_user,
        'passwd': db_pwd,
        'db': db_name
    }
