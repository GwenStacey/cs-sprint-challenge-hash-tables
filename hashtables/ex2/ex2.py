#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    ticket_table = {}
    route = []
    for i in tickets:
        ticket_table[i.source] = i.destination
    while len(route) < length:
        if len(route) == 0:
            route.append(ticket_table.get('NONE'))
        i = len(route)-1
        route.append(ticket_table.get(route[i]))


    return route
