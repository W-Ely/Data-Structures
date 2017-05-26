"""Module Implements stack data structure"""
from linked_list import LinkedList


class Stack(object):

    def __init__(self, iterable=None):
        """Initalizes a stack"""
        self._stack = LinkedList(iterable)

    def push(self, val):
        """Add an item to Stack"""
        self._stack.push(val)

    def pop(self):
        """Remove item from stack"""
        return self._stack.pop()

    def __len__(self):
        """Get length"""
        return self._stack.size()
