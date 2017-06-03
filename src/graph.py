"""Module implements a graph data strcture"""


class Node(object):
    """Create node object."""

    def __init__(self, value=None, next_node=None, prev_node=None):
        """Initalize a node."""
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node
