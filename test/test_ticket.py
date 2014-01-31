import unittest
from mock import Mock
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(BASE_DIR, '../')))


class TestTicket(unittest.TestCase):

    def setUp(self):
        import pytrac
        # how to mock Ticket() / server?
#        self.pytrac.Ticket.__init__.server = Mock()
        pytrac.Ticket = Mock()
        self.ticket = pytrac.Ticket()

    def testSearchWithAllParams(self):
        self.api.query = Mock()
        self.ticket.search(summary='test_summary', owner='someowner', status='new')
        self.api.query.assert_called_with('summary~=test_summary&owner=someowner&status=new')


if __name__ == '__main__':
    unittest.main()
