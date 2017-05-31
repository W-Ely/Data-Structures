"""Double ended queue module."""
from dll import Dll


class Deque(object):
    """Create deque data structure."""

    def __init__(self):
        """Initalize a Deque."""
        self._que = Dll()

    def append(self, val):
        """Add an item to the deque."""
        self._que.push(val)

    def appendleft(self, val):
        """Append value to the front of the deque."""
        self._que.append(val)

    def pop(self):
        """Pop value from end of the deque and returns it."""
        return self._que.pop()

    def popleft(self):
        """Pop value from front of the deque and return it."""
        return self._que.shift()

    def peek(self):
        """Return next value in deque without dequeueing it."""
        if self._que.tail is not None:
            return self._que.tail.value
        return None

    def peekleft(self):
        """Return value of popleft but leaves value in deque."""
        if self._que.head is not None:
            return self._que.head.value
        return None

    def size(self):
        """Get length of deque."""
        return self._que.__len__()
