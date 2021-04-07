from data.utils import create_db_connection, read_query
from config import connection_config
import pandas as pd


# Return nodes data from DB
def find_nodes(node_id, language, search_keyword, page_num, page_size):

    # get connection config
    config = connection_config()

    # Connect to the Database
    connection = create_db_connection(
        config['host'], config['user'], config['passwd'], config['db'])

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
