"""This module creates a linked list data structure."""


class Node(object):

    def __init__(self, value=None, next_node=None):
        """Initalizes a node."""
        self.value = value
        self.next_node = next_node


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initalizes a linked list"""
        self.head = None
        self.length = 0
        if iterable is not None:
            if type(iterable) in [list, tuple, str]:
                for val in iterable:
                    self.push(val)
            else:
                raise TypeError(iterable, 'is not iterable')

    def push(self, val):
        self.length += 1
        new_node = Node(val, self.head)
        self.head = new_node

    def pop(self):
        try:
            val = self.head.value
            self.head = self.head.next_node
            self.length -= 1
            return val
        except AttributeError:
            print("Can not pop from empty list.")
            return "Can not pop from empty list."

    def size(self):
        return self.length

    def search(self, val):
        check = self.head
        while check is not None:
            print(check.value)
            if check.value == val:
                return check
            else:
                check = check.next_node
        return None

    def remove(self, node):
        check = self.head
        while check.next_node is not node and hasattr(check, 'next_node'):
            check = check.next_node
        if check.next_node is None:
            raise AttributeError("Can not remove node, not found.")
        else:
            check.next_node = check.next_node.next_node
            self.length -= 1

    def display(self):
        string = '('
        head = self.head
        while head is not None:
            string += str(head.value) + ', '
            head = head.next_node
        string = string[:-2] + ')'
        return string

    def __len__(self):
        """Returns the length"""
        self.size()

    def __repr__(self):
        """Prints it out"""
        self.display()
