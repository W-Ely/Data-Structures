"""Double linked list module."""


class Node(object):
    """Create node object."""

    def __init__(self, value=None, next_node=None, prev_node=None):
        """Initalize a node."""
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node


class Dll(object):
    """Create a doubly linked list class."""

    def __init__(self):
        """Initalize a doubly linked list."""
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        """Push to the dll."""
        self.length += 1
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            new_node = Node(val, self.head)
            self.head.prev_node = new_node
            self.head = new_node

    def append(self, val):
        """Append value to the end of the dll."""
        if self.length == 0:
            self.push(val)
        else:
            new_node = Node(val, None, self.tail)
            self.tail.next_node = new_node
            self.tail = new_node
            self.length += 1

    def pop(self):
        """Pop item from head and return it."""
        try:
            val = self.head.value
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next_node
                self.head.prev_node = None
            self.length -= 1
            return val
        except AttributeError:
            print("Can not pop from empty list.")
            return "Can not pop from empty list."

    def remove(self, node):
        """Remove the specified node."""
        check = self.head
        while check.next_node is not node and hasattr(check, 'next_node'):
            check = check.next_node
        if check.next_node is None:
            raise AttributeError("Can not remove node, not found.")
        else:
            check.next_node = check.next_node.next_node
            self.length -= 1

    def __repr__(self):
        """Print the list."""
        string = '('
        head = self.head
        while head is not None:
            string += str(head.value) + ', '
            head = head.next_node
        string = string[:-2] + ')'
        return string

    def __len__(self):
        """Return the size of the list."""
        return self.length
