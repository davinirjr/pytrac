import unittest
from mock import Mock
import sys
import os
import datetime

from pytrac import Ticket


class TestTicket(unittest.TestCase):

    def setUp(self):
        server = Mock()
        self.ticket = Ticket(server)

    def testSearchWithAllParams(self):
        self.ticket.search(summary='test_summary', owner='someowner', status='new')
        self.ticket.api.query.assert_called_with('max=0&summary~=test_summary&owner=someowner&status=new')


class TestUpdateTicket(unittest.TestCase):

    ticket_id = 1

    def setUp(self):
        server = Mock()
        timestamp = datetime.datetime.now()
        server.ticket.get.return_value = [self.ticket_id,
                                          timestamp,
                                          timestamp,
                                          {'_ts': timestamp,
                                           'action': 'leave'}]
        server.ticket.update.return_value = [self.ticket_id,
                                             timestamp,
                                             timestamp,
                                             {'_ts': timestamp,
                                              'action': 'leave'}]
        self.ticket = Ticket(server)

    def testComment(self):
        self.ticket.comment(self.ticket_id, "some comment")
        self.ticket.api.get.assert_called_with(1)


if __name__ == '__main__':
    unittest.main()
