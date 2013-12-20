import xmlrpclib


class Ticket(Object):

    def __init__(self, user, host, password):
        self.url = 'https://%s:%s@%s/trac/login/xmlrpc' % (user, password, host)
        self.server = xmlrpclib.ServerProxy(self.url)
        self.api = self.server.ticket

    def search(self, query):
        result = self.api.query(query)
        print result


#
#def update():
#    print "dummy"
#
#
#def create():
#    print "dummy"
