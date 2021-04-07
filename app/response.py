class Response(object):
    def __init__(self, nodes):
        self._set_nodes(nodes)

    def _set_nodes(self, nodes):
        if type(nodes) != list:
            raise Exception('invalid nodes list provided')

        self._nodes = []
        for n in nodes:
            node = Node(n)
            self._nodes.append(node.serialize())

    @property
    def nodes(self):
        return self._nodes


class Node(object):
    def __init__(self, data):
        self._set_node_id(data['idNode'])
        self._set_name(data['nodeName'])
        self._set_children_count(data['childrenCount'])

    def _set_node_id(self, node_id):
        if type(node_id) != int:
            raise Exception('Invalid node id provided')
        self._node_id = node_id

    def _set_name(self, name):
        if type(name) != str:
            raise Exception('Invalid node name provided')
        self._name = name

    def _set_children_count(self, children_count):
        if type(children_count) != int:
            raise Exception('Invalid node children count provided')
        self._children_count = children_count

    def serialize(self):
        return {
            "node_id": self.node_id,
            "name": self.name,
            "children_count": self.children_count
        }

    @property
    def node_id(self):
        return self._node_id

    @property
    def name(self):
        return self._name

    @property
    def children_count(self):
        return self._children_count
