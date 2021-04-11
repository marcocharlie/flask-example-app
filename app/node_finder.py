from database import Database


# Return nodes data from DB
def find_nodes(node_id, language, search_keyword, page_num, page_size):

    # Connect to database
    db = Database()
    connection = db.create_connection()

    # Set sql mode in session
    # This will prevent from the following error:
    # Error Code: 1055. Expression #2 of SELECT list is not in GROUP BY clause and contains nonaggregated column
    db.execute_query("set session sql_mode='';")

    # Declare database to be used for queries
    db.execute_query("use nodes;")

    # Query database combining the following queries:
    # - depth on requested subtree children nodes
    # - children count for each parent node
    query = """
    SELECT depth_subtree_select.idNode, depth_subtree_select.nodeName, COALESCE (children_counts_select.childrenCount , 0) AS childrenCount
    FROM
    (SELECT node.idNode, (COUNT(parent.idNode) - (sub_tree.depth + 1)) AS depth,
        (SELECT nodeName FROM node_tree_names WHERE idNode = node.idNode AND language = '%s') AS nodeName
    FROM node_tree AS node,
    node_tree AS parent,
    node_tree AS sub_parent,
        (
            SELECT node.idNode, (COUNT(parent.idNode) - 1) AS depth
            FROM node_tree AS node,
                node_tree AS parent
            WHERE node.iLeft BETWEEN parent.iLeft AND parent.iRight	AND node.idNode = %s
            GROUP BY node.idNode
            ORDER BY node.iLeft
        ) AS sub_tree
    WHERE node.iLeft BETWEEN parent.iLeft AND parent.iRight
        AND node.iLeft BETWEEN sub_parent.iLeft AND sub_parent.iRight
        AND sub_parent.idNode = sub_tree.idNode
    GROUP BY node.idNode
    HAVING depth = 1
    ORDER BY node.iLeft
    ) AS depth_subtree_select
    LEFT JOIN
    (
    SELECT node.idNode, count(*) AS childrenCount
    FROM node_tree AS child join
    node_tree AS node
    on node.iLeft < child.iLeft AND node.iRight > child.iRight
    GROUP BY node.idNode
    ) AS children_counts_select
    ON depth_subtree_select.idNode = children_counts_select.idNode
    """ % (language, node_id)

    # Add filter on node name (if provided)
    if search_keyword != None:
        search_keyword = '%'+search_keyword.lower()+'%'
        query = query+"WHERE nodeName LIKE '%s'" % search_keyword

    # Use offset and limit for pagination
    limit = page_size
    offset = (limit * (page_num+1)) - limit
    query = query+"LIMIT %s, %s;" % (offset, limit)

    field_names, results = db.read_query(query)
    connection.close()

    if len(results) == 0:
        raise Exception("No children nodes available for the given parameters")

    # Unpack results and field names
    data = [dict(zip(field_names, values)) for values in results]

    return data
