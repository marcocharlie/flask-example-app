from data.utils import create_db_connection, read_query, format_query_results
from os import getenv


# Return nodes data from DB
def find_nodes(node_id, language, search_keyword, page_num, page_size):

    db_address = getenv("DB_ADDRESS")
    db_user = getenv("DB_USER")
    db_pwd = getenv("DB_PWD")
    db_name = getenv("DB_NAME")

    # Connect to the Database
    connection = create_db_connection(db_address, db_user, db_pwd, db_name)

    # Search for primary node data
    primary_node_data = get_node(connection, node_id)
    if len(primary_node_data) == 0:
        raise Exception("Invalid node id provided")

    # Keep primary node data for children search
    left = primary_node_data[0]["iLeft"]
    right = primary_node_data[0]["iRight"]

    # Query database
    query = """
        SELECT *
        FROM node_tree
        LEFT JOIN node_tree_names
        ON node_tree.idNode = node_tree_names.idNode
        WHERE (node_tree.iLeft > %s) AND (node_tree.iRight < %s) AND (node_tree_names.language = '%s');
        """ % (left, right, language)

    if search_keyword != None:
        query = query.replace(";", "")
        query = "%s AND (node_tree_names.nodeName = '%s');" % (
            query, search_keyword)

    # Format and enrich raw data
    field_names, results = read_query(connection, query)
    df = format_query_results(field_names, results)

    connection.close()

    return df.to_dict(orient='records')


# Return primary node data
def get_node(connection, node_id):

    query = """
        SELECT *
        FROM %s
        WHERE idNode = %s;
        """ % ("node_tree", node_id)

    field_names, results = read_query(connection, query)
    df = format_query_results(field_names, results)

    return df.to_dict(orient='records')
