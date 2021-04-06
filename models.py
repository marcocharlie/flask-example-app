class ParseRequest(object):
    _node_id = None
    _language = None
    _search_keyword = None
    _page_num = 0
    _page_size = 100

    def __init__(self, data):
        if not data:
            raise Exception('empty request')

        # required fields
        self._set_node_id(data['node_id'])
        self._set_language(data['language'])

        # optional fields
        if 'search_keyword' in data:
            self._set_search_keyword(data['search_keyword'])
        if 'page_num' in data:
            self._set_page_num(data['page_num'])
        if 'page_size' in data:
            self._set_page_size(data['page_size'])

    def _set_node_id(self, node_id):
        if node_id == None:
            raise Exception('missing node_id in request')
        return self._node_id

    @property
    def node_id(self):
        return self._node_id

    def _set_language(self, language):
        if language == None:
            raise Exception('missing language in request')
        self._language = language

    @property
    def language(self):
        return self._language

    def _set_search_keyword(self, search_keyword):
        if type(search_keyword) != str:
            raise Exception('invalid search_keyword provided')
        self._search_keyword = search_keyword.lower()

    @property
    def search_keyword(self):
        return self._search_keyword

    def _set_page_num(self, page_num):
        if type(page_num) != int or page_num < 0:
            raise Exception('invalid page_num provided')
        self._page_num = page_num

    @property
    def page_num(self):
        return self._page_num

    def _set_page_size(self, page_size):
        if type(page_size) != int:
            raise Exception('invalid page_size provided')
        if page_size <= 0 or page_size > 1000:
            raise Exception('page_size must be a value between 0 and 1000')
        self._page_size = page_size

    @property
    def page_size(self):
        return self._page_size
