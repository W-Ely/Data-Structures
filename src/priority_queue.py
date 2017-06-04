"""Priority queue module for data structures."""


class PriorityQueue(object):
    """Our Priority queue."""

    def __init__(self, iterable=None):
        """Initialize the Priority queue."""
        self.queue = {}
        if iterable is not None:
            for data, priority, in iterable:
                self.insert(data, priority)

    def insert(self, data, priority=0):
        """Insert values into the priority queue."""
        if priority in self.queue:
            self.queue[priority].insert(0, data)
        else:
            self.queue[priority] = [data]

    def pop(self):
        """Pop the top item off of the priority queue."""
        for priority in sorted(self.queue):
            if len(self.queue[priority]) > 0:
                return self.queue[priority].pop()
        raise IndexError("Cannot pop from an empty priority queue.")

    def peek(self):
        """Peek at the highest priority value."""
        for priority in sorted(self.queue):
            if len(self.queue[priority]) > 0:
                return self.queue[priority][-1]
