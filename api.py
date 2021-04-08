from flask import Flask, request, jsonify, abort, escape
from app.request import ParseRequest
from app.node_finder import find_nodes
from app.node_formatter import formatter
from app.response import Response


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app_prefix = '/api'


@app.route(app_prefix + '/', methods=['GET'])
def parse_request():
    # Validate request
    try:
        request_object = ParseRequest(request.get_json(request.json))
    except Exception as e:
        return jsonify({'nodes': [], 'error': str(e)})
    
    # Query on database
    try:
        field_namess, nodes = find_nodes(
            request_object.node_id,
            request_object.language
        )
    except Exception as e:
        return jsonify({'nodes': [], 'error': str(e)})
    
    # Format response
    try:
        formatted_nodes = formatter(field_namess, nodes, request_object.search_keyword, request_object.page_num, request_object.page_size)
        response = Response(formatted_nodes)
        return jsonify({'nodes': response.nodes})
    except Exception as e:
        return jsonify({'nodes': [], 'error': str(e)})


if __name__ == '__main__':
    app.run(host="0.0.0.0")
