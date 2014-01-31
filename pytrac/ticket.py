class Ticket(object):

    def __init__(self, server):
        self.api = server.ticket

    def search_raw(self, query):
        return self.api.query(query)

    def search(self, summary=None, owner=None, status=None):
        query = ''
        if summary:
            query += "summary~=%s&" % summary
        if owner:
            query += "owner=%s&" % owner
        if status:
            query += "status=%s&" % status
        if query == '':
            raise Exception("Query empty!")
        query = query.rstrip('&')
        return self.api.query(query)

    # id, summary, owner, ...
    def info(self):
        pass

    def update(self):
        pass

    def create(self):
        pass
