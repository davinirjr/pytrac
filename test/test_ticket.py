import unittest
from mock import Mock
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(BASE_DIR, '../')))

from pytrac import Ticket


class TestTicket(unittest.TestCase):

    def setUp(self):
        server = Mock()
        self.ticket = Ticket(server)

    def testSearchWithAllParams(self):
        self.ticket.search(summary='test_summary', owner='someowner', status='new')
        self.ticket.api.query.assert_called_with('summary~=test_summary&owner=someowner&status=new')


if __name__ == '__main__':
    unittest.main()
