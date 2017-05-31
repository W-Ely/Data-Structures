    """Module Implements stack data structure"""
from linked_list import LinkedList


class Stack(object):

    def __init__(self, iterable=None):
        """Initalizes a stack"""
        self._tools = LinkedList
        self.head = None
        self.length = 0
        if iterable is not None:
            if type(iterable) in [list, tuple, str]:
                for val in iterable:
                    self.push(val)
            else:
                raise TypeError(iterable, 'is not iterable')

    def push(self, val):
        """Add an item to Stack"""
        self._tools.push(self, val)

    def pop(self):
        """Remove item from stack"""
        return self._tools.pop(self)

    def __len__(self):
        """Get length"""
        return self._tools.size(self)
