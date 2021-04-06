from data.utils import create_db_connection, read_query


def find_nodes(node_id, language, search_keyword, page_num, page_size):

    # Connect to the Database
    connection = create_db_connection("localhost", "root", "martina8", "nodes")

    q1 = """
        SELECT *
        FROM node_tree;
        """

    results = read_query(connection, q1)

    for result in results:
        print(result)
