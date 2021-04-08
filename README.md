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
pip install -r requirements.txt
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

### Testing

A simple rest file is provided.