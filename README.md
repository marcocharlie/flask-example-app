# flask-example-app

A flask app to retrieve organizational chart nodes from mySQL.

## Requirements

You can run the application in a Python 3.7 environment.

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

### Run App

Execute the application

```bash
python api.py
```

### Testing

A simple rest file is provided.