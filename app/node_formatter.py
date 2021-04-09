import pandas as pd
from math import ceil
import numpy as np


def formatter(field_names, results, search_keyword, page_num, page_size):
    # Format and enrich raw data
    df = format_query_results(field_names, results)

    # Add filter on node name (if provided)
    if search_keyword != None:
        df = df[df['nodeName'].str.contains(search_keyword, case=False)]

    # Paginate dataframe
    paginated_df = paginate_dataframe(df, page_num, page_size)

    # Turn dataframe to list of objects
    data = paginated_df.to_dict(orient='records')
    return data


# Return query results as a pandas DataFrame
def format_query_results(field_names, results):
    data = [list(result) for result in results]
    df = pd.DataFrame(data, columns=field_names)
    df = df.loc[:, ~df.columns.duplicated()]
    if df.shape[0] == 0:
        raise Exception("No children nodes available for given node id")

    # Enrich node data
    df['childrenCount'] = df.apply(
        lambda row: get_children_count(df, row.iLeft, row.iRight), axis=1)

    return df


# Return children count by node
def get_children_count(df, left, right):
    children_count = df[(df['iLeft'] > left) & (df['iRight'] < right)].shape[0]
    return children_count


# Return paginated dataframe
def paginate_dataframe(df, page_num, page_size):
    total = df.shape[0]
    page_count = ceil(total/page_size)

    if page_count == 1:
        if page_num == 0:
            return df
        elif page_num > 0:
            raise Exception(
                "No other nodes available for the given parameters")

    # split dataframe into separate tables
    rows = np.arange(len(df))
    dfs = [sub_df for _, sub_df in df.groupby(rows // page_size)]
    if len(dfs) <= page_num:
        raise Exception("No other nodes available for the given parameters")

    return dfs[page_num]
