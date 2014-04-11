import xmlrpclib
from .ticket import Ticket


def connect(host, user, password):
    '''connect to trac'''
    url = 'https://%s:%s@%s/trac/login/xmlrpc' % (user, password, host)
    server = xmlrpclib.ServerProxy(url)
    return Ticket(server)

__all__ = ['connect']
