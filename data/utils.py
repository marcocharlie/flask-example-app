import mysql.connector
from mysql.connector import Error
#import pandas as pd


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


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


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


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


#pw = "martina8"
#connection = create_server_connection("localhost", "root", pw)
#create_database_query = "CREATE DATABASE nodes"
#create_database(connection, create_database_query)
#
# create_node_tree_table = """
# create table node_tree(
#    idNode integer PRIMARY KEY,
#    level integer,
#    iLeft integer,
#    iRight integer
# );
# """
#
# create_node_tree_names_table = """
# create table node_tree_names(
#    idNode integer,
#    language varchar(100),
#    nodeName varchar(100),
#    FOREIGN KEY (idNode) REFERENCES node_tree (idNode)
# );
# """
#
# Connect to the Database
#connection = create_db_connection("localhost", "root", pw, "nodes")
# Create tables
#execute_query(connection, create_node_tree_table)
#execute_query(connection, create_node_tree_names_table)
#
# fill tables
# node_tree_data = """
# insert into node_tree(idNode, level, iLeft, iRight) values
#(1, 2, 2, 3),
#(2, 2, 4, 5),
#(3, 2, 6, 7),
#(4, 2, 8, 9),
#(5, 1, 1, 24),
#(6, 2, 10, 11),
#(7, 2, 12, 19),
#(8, 3, 15, 16),
#(9, 3, 17, 18),
#(10, 2, 20, 21),
#(11, 3, 13, 14),
#(12, 2, 22, 23);
# """
#
# node_tree_names_data = """
# insert into node_tree_names(idNode, language, nodeName) values
#(1, "english", "Marketing"),
#(1, "italian", "Marketing"),
#(2, "english", "Helpdesk"),
#(2, "italian", "Supporto tecnico"),
#(3, "english", "Managers"),
#(3, "italian", "Managers"),
#(4, "english", "Customer Account"),
#(4, "italian", "Assistenza Cliente"),
#(5, "english", "Docebo"),
#(5, "italian", "Docebo"),
#(6, "english", "Accounting"),
#(6, "italian", "Amministrazione"),
#(7, "english", "Sales"),
#(7, "italian", "Supporto Vendite"),
#(8, "english", "Italy"),
#(8, "italian", "Italia"),
#(9, "english", "Europe"),
#(9, "italian", "Europa"),
#(10, "english", "Developers"),
#(10, "italian", "Sviluppatori"),
#(11, "english", "North America"),
#(11, "italian", "Nord America"),
#(12, "english", "Quality Assurance"),
#(12, "italian", "Controllo Qualità");
# """
#
#execute_query(connection, node_tree_data)
#execute_query(connection, node_tree_names_data)
#
