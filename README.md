# flask-example-app

A flask app to retrieve organizational chart nodes from a mySQL database.

## Requirements

You can run the application in a Python 3.7 environment.
To execute the program, you’ll need to have :
- mySQL installed on your machine
- a mySQL library (e.g. “mysql-connector-python”) to query the database
- a text editor such as Visual Studio Code.

### Python env

Install requirements via PIP

```bash
virtualenv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

### Setup

Initialize mySql database and tables launching
```bash
python setup.py
```
The command will create `nodes` database, `node_tree` and `node_tree_names` tables.

### Run App

Execute the application

```bash
python api.py
```

### Available endpoints

The app offers an HTTP `GET` `/api` endpoint which queries a mySQL database and returns a list of children nodes from an organizational chart for the given node.

#### Parameters:

- `node_id` (integer, required): the unique ID of the selected node.
- `language` (enum, required): language identifier. Possible values: "english", "italian".
- `search_keyword` (string, optional): a search term used to filter results. If provided, restricts the results to "all children nodes under node_id whose nodeName in the given language contains search_keyword (case insensitive)".
- `page_num` (integer, optional): the 0-based identifier of the page to retrieve. If not provided, defaults to “0”.
- `page_size` (integer, optional): the size of the page to retrieve, ranging from 0 to 1000. If not provided, defaults to “100”.

### Examples

The [example](https://github.com/marcocharlie/flask-example-app/tree/master/examples) folder provides REST examples. They are meant to be used on VSCode REST Client plugin.