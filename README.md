# flask-example-app

App providing organizational chart nodes from a mySQL database through a Web API endpoint.
Written in Python 3 using [Flask](https://flask.palletsprojects.com/en/1.1.x/).

## Usage

### Requirements

- Docker engine version >= 18.06.1
- Linux / Unix machine w/GNU make installed

### Run app

To start the application, run:
```bash
make start-app
```

### Available endpoints

The app offers an HTTP `GET` `/api` endpoint which queries a mySQL database and returns a list of children nodes from an organizational chart for the given node id and language.

#### Parameters:

- `node_id` (integer, required): the unique ID of the selected node.
- `language` (enum, required): language identifier. Possible values: "english", "italian".
- `search_keyword` (string, optional): a search term used to filter results. If provided, restricts the results to "all children nodes under node_id whose nodeName in the given language contains search_keyword (case insensitive)".
- `page_num` (integer, optional): the 0-based identifier of the page to retrieve. If not provided, defaults to “0”.
- `page_size` (integer, optional): the size of the page to retrieve, ranging from 0 to 1000. If not provided, defaults to “100”.

### Examples

The [examples](https://github.com/marcocharlie/flask-example-app/tree/master/examples) folder provides a REST file as example. It is meant to be used on [VSCode](https://code.visualstudio.com/) [REST Client plugin](https://github.com/Huachao/vscode-restclient).

## Application structure

The application is structured as follows:

- An internal app wich contains:
    - a Flask HTTP api route providing a JSON response
    - a config file (providing DB access credentials)
    - internal utils doing the dirty work
- A mySQL database setup