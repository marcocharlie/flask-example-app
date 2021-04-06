from flask import Flask, request, jsonify, abort, escape
from models import *
from werkzeug.exceptions import BadRequest
from node_finder import find_nodes
#from response import Response

app = Flask(__name__)
app_prefix = '/api'


@app.route(app_prefix + '/', methods=['GET'])
def parse_request():
    try:
        request_object = ParseRequest(request.get_json(request.json))
    except Exception as e:
        raise BadRequest(e)

    try:
        nodes = find_nodes(
            request_object.node_id,
            request_object.language,
            request_object.search_keyword,
            request_object.page_num,
            request_object.page_size
        )

        response = Response.create(
            nodes
        )
    except Exception as e:
        raise Exception(e)

    return jsonify({'response': response.__dict__})


if __name__ == '__main__':
    app.run(host="0.0.0.0")
