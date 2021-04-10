from database.database import Database


def main():

    create_database_query = "CREATE DATABASE IF NOT EXISTS nodes"

    create_node_tree_table_query = """
    CREATE TABLE IF NOT EXISTS node_tree(
        idNode integer PRIMARY KEY NOT NULL,
        level integer NOT NULL,
        iLeft integer NOT NULL,
        iRight integer NOT NULL
    );
    """

    create_node_tree_names_table_query = """
    CREATE TABLE IF NOT EXISTS node_tree_names(
        idNode integer NOT NULL,
        language varchar(100) NOT NULL,
        nodeName varchar(100) NOT NULL,
        UNIQUE unique_index(idNode, language),
        FOREIGN KEY (idNode) REFERENCES node_tree (idNode)
    );
    """

    node_tree_data = """
    insert ignore into node_tree(idNode, level, iLeft, iRight) values
    (1, 2, 2, 3),
    (2, 2, 4, 5),
    (3, 2, 6, 7),
    (4, 2, 8, 9),
    (5, 1, 1, 24),
    (6, 2, 10, 11),
    (7, 2, 12, 19),
    (8, 3, 15, 16),
    (9, 3, 17, 18),
    (10, 2, 20, 21),
    (11, 3, 13, 14),
    (12, 2, 22, 23);
    """

    node_tree_names_data = """
    insert ignore into node_tree_names(idNode, language, nodeName) values
    (1, "english", "Marketing"),
    (1, "italian", "Marketing"),
    (2, "english", "Helpdesk"),
    (2, "italian", "Supporto tecnico"),
    (3, "english", "Managers"),
    (3, "italian", "Managers"),
    (4, "english", "Customer Account"),
    (4, "italian", "Assistenza Cliente"),
    (5, "english", "Docebo"),
    (5, "italian", "Docebo"),
    (6, "english", "Accounting"),
    (6, "italian", "Amministrazione"),
    (7, "english", "Sales"),
    (7, "italian", "Supporto Vendite"),
    (8, "english", "Italy"),
    (8, "italian", "Italia"),
    (9, "english", "Europe"),
    (9, "italian", "Europa"),
    (10, "english", "Developers"),
    (10, "italian", "Sviluppatori"),
    (11, "english", "North America"),
    (11, "italian", "Nord America"),
    (12, "english", "Quality Assurance"),
    (12, "italian", "Controllo Qualità");
    """

    # Init database
    db = Database()

    # Connect to mySql server
    connection = db.create_connection()

    # Create Database
    db.create_database(create_database_query)

    # Create tables
    db.execute_query(create_node_tree_table_query)
    db.execute_query(create_node_tree_names_table_query)

    # Insert data into tables
    db.execute_query(node_tree_data)
    db.execute_query(node_tree_names_data)


if __name__ == "__main__":
    main()
