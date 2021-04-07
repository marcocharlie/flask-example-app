import mysql.connector
from mysql.connector import Error
import pandas as pd


# Create server connection
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


# Create new db
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


# Create db connection
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


# Run query on db for creating tables and insert data
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


# Run query for reading data
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        field_names = cursor.column_names
        result = cursor.fetchall()
        cursor.close()
        return field_names, result
    except Error as err:
        print(f"Error: '{err}'")


# Return query results as a pandas DataFrame
def format_query_results(field_names, results):
    data = []

    for result in results:
        result = list(result)
        data.append(result)

    df = pd.DataFrame(data, columns=field_names)
    df = df.loc[:, ~df.columns.duplicated()]
    print(df)
    #index = list(df.columns)[0]
    #df = df.set_index(index)

    # Enrich node data
    df['childrenCount'] = df.apply(
        lambda row: get_children_count(df, row.iLeft, row.iRight), axis=1)

    return df


# Return children count by node
def get_children_count(df, left, right):
    children_count = df[(df['iLeft'] > left) & (df['iRight'] < right)].shape[0]
    return children_count
