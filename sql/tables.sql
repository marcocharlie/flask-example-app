-- Database structure
-- The following MYSQL tables contain an organizational chart, along with the role names in various languages,
-- flattened as per the Nested Set model.


-- Table node_tree
create table node_tree(
    idNode integer PRIMARY KEY,
    level integer,
    iLeft integer,
    iRight integer
);

-- Table node_tree_names (idNode is Foreign Key referencing node_tree.idNode)
create table node_tree_names(
    idNode integer,
    language varchar(100),
    nodeName varchar(100),
    FOREIGN KEY (idNode) REFERENCES node_tree (idNode)
);