from database.database import Database
from .node_formatter import format_query_results


# Return nodes data from DB
def find_nodes(node_id, language):

    # Init database
    db = Database()

    # Connect to the Database
    connection = db.create_connection()

    # Search for parent node data
    parent_node_data = get_parent_node(db, node_id)

    # Keep parent node data for children search
    left = parent_node_data[0]["iLeft"]
    right = parent_node_data[0]["iRight"]

    # Query database
    query = """
        SELECT *
        FROM node_tree
        LEFT JOIN node_tree_names
        ON node_tree.idNode = node_tree_names.idNode
        WHERE (node_tree.iLeft > %s) AND (node_tree.iRight < %s) AND (node_tree_names.language = '%s');
        """ % (left, right, language)

    field_names, results = db.read_query(query)
    connection.close()   

    return field_names, results


# Return parent node data
def get_parent_node(db, node_id):

    query = """
        SELECT *
        FROM %s
        WHERE idNode = %s;
        """ % ("node_tree", node_id)

    field_names, results = db.read_query(query)
    if len(results) == 0:
        raise Exception("Invalid node id provided")

    df = format_query_results(field_names, results)
    data = df.to_dict(orient='records')

    return data
