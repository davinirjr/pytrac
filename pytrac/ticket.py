import xmlrpclib


class Ticket(object):

    def __init__(self, user, host, password):
        self.url = 'https://%s:%s@%s/trac/login/xmlrpc' % (user, password, host)
        self.server = xmlrpclib.ServerProxy(self.url)
        self.api = self.server.ticket

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
