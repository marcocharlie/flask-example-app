from flask import Flask, request, jsonify, abort, escape
from app.request import *
from app.node_finder import find_nodes
from app.response import Response


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app_prefix = '/api'


@app.route(app_prefix + '/', methods=['GET'])
def parse_request():
    try:
        request_object = ParseRequest(request.get_json(request.json))
    except Exception as e:
        return jsonify({'nodes': [], 'error': str(e)})

    try:
        nodes = find_nodes(
            request_object.node_id,
            request_object.language,
            request_object.search_keyword,
            request_object.page_num,
            request_object.page_size
        )
        response = Response(nodes)
    except Exception as e:
        return jsonify({'nodes': [], 'error': str(e)})

    return jsonify({'nodes': response._nodes})


if __name__ == '__main__':
    app.run(host="0.0.0.0")
