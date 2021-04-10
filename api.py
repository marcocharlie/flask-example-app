from flask import Flask, request, jsonify
from app.request import ValidateNodeRequest
from app.node_finder import find_nodes
from app.response import NodesResponse


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app_prefix = '/api'


@app.route(app_prefix + '/nodes', methods=['GET'])
def parse_request():
    try:
        # Validate request
        request_object = ValidateNodeRequest(request.get_json(request.json))
        # Query on database
        nodes = find_nodes(
            request_object.node_id,
            request_object.language,
            request_object.search_keyword,
            request_object.page_num,
            request_object.page_size
        )
        # Format nodes response
        response = NodesResponse(nodes)
        return jsonify({'nodes': response.nodes})
    except Exception as e:
        return jsonify({'nodes': [], 'error': str(e)})


if __name__ == '__main__':
    app.run(host="0.0.0.0")
