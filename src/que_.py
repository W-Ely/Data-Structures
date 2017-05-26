"""Queue using composition."""
from dll import Dll


class Queue(object):
    """Create queue data structure."""

    def __init__(self):
        """Initalize a Queue."""
        self._que = Dll()

    def enqueue(self, val):
        """Add an item to the queue."""
        self._que.push(val)

    def dequeue(self):
        """Remove item from queue."""
        return self._que.shift()

    def peek(self):
        """Returns next value in queue without dequeueing it."""
        if self._que.tail is not None:
            return self._que.tail.value
        return None

    def size(self):
        """Get length of queue."""
        return self._que.__len__()
