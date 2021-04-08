-- Database structure
-- The following MYSQL tables contain an organizational chart, along with the role names in various languages,
-- flattened as per the Nested Set model.

-- Database
CREATE DATABASE [IF NOT EXISTS] nodes

-- Table node_tree
CREATE TABLE [IF NOT EXISTS] node_tree(
    idNode integer PRIMARY KEY NOT NULL,
    level integer NOT NULL,
    iLeft integer NOT NULL,
    iRight integer NOT NULL
);

-- Table node_tree_names (idNode is Foreign Key referencing node_tree.idNode)
CREATE TABLE [IF NOT EXISTS] node_tree_names(
    idNode integer NOT NULL,
    language varchar(100) NOT NULL,
    nodeName varchar(100) NOT NULL,
    FOREIGN KEY (idNode) REFERENCES node_tree (idNode)
);