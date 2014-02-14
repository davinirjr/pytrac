import unittest
from mock import Mock
import sys
import os

from pytrac import Ticket


class TestTicket(unittest.TestCase):

    def setUp(self):
        server = Mock()
        self.ticket = Ticket(server)

    def testSearchWithAllParams(self):
        self.ticket.search(summary='test_summary', owner='someowner', status='new')
        self.ticket.api.query.assert_called_with('max=0&summary~=test_summary&owner=someowner&status=new')


if __name__ == '__main__':
    unittest.main()
