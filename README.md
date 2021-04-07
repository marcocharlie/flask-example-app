# flask-example-app

A flask app to retrieve organizational chart nodes from mySQL.

## Requirements

To execute the program, you’ll need to have mySQL installed on your machine and a a text editor such as Visual Studio Code.
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