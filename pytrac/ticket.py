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

    def _parse_ticket_info(self, ticket_data):
        '''make nice dict out of ticket info'''
        ticket_info = {
            'id': ticket_data[0],
            'created': ticket_data[1],  # this is xmlrpc.DateTime!
            'modified': ticket_data[2],
        }
        ticket_info.update(ticket_data[3])

        return ticket_info

    # id, summary, owner, ...
    def info(self, ticket_id):
        '''return info about specfic ticket'''
        ticket_data = self.api.get(ticket_id)
        return self._parse_ticket_info(ticket_data)

    def update(self, ticket_id, comment='', attrs=None, action='leave', notify=False):
        '''update the ticket with XXX'''
        ticket_info = self.info(ticket_id)

        attributes = {
            'action': action,
            '_ts': ticket_info['_ts'],
        }
        if attrs is not None:
            attributes.update(attrs)

        # catch exception (eg: set ticket to next although it is already at
        # next)
        result = self.api.update(
            ticket_info['id'],
            comment,
            attributes,
            notify,
        )
        return self._parse_ticket_info(result)

    def comment(self, ticket_id, comment):
        '''add comment to ticket'''
        return self.update(ticket_id, comment)

    def create(self):
        pass
