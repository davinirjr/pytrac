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
        self.timestamp = datetime.datetime.now()
        server.ticket.get.return_value = [self.ticket_id,
                                          self.timestamp,
                                          self.timestamp,
                                          {'_ts': self.timestamp,
                                           'action': 'leave'}]
        server.ticket.update.return_value = [self.ticket_id,
                                             self.timestamp,
                                             self.timestamp,
                                             {'_ts': self.timestamp,
                                              'action': 'leave'}]
        self.ticket = Ticket(server)

    def testComment(self):
        self.ticket.comment(self.ticket_id, "some comment")
        self.ticket.api.update.assert_called_with(
            self.ticket_id,
            comment="some comment",
            attrs={'action': 'leave', '_ts': self.timestamp},
            notify=True)


if __name__ == '__main__':
    unittest.main()
