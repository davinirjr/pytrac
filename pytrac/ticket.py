import xmlrpclib


class Ticket(object):

    def __init__(self, user, host, password):
        self.url = 'https://%s:%s@%s/trac/login/xmlrpc' % (user, password, host)
        self.server = xmlrpclib.ServerProxy(self.url)
        self.api = self.server.ticket

    def search_raw(self, query):
        result = self.api.query(query)
        print result

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
        print '"%s"' % query
        result = self.api.query(query)
        print result

#    def search(self, query):

#
#def update():
#    print "dummy"
#
#
#def create():
#    print "dummy"
