"""Module implements a graph data strcture"""


class Graph(dict):
    """Create a graph data strcture modeled off a dictionary."""

    def __init__(self):
        """Inialize probably wont need."""
        pass

    def nodes():
        """Return a list of all nodes in the graph."""
        pass

    def edges():
        """Return a list of all edges in the graph."""
        pass

    def add_node(val):
        """Add a new node with value ‘n’ to the graph."""
        pass

    def add_edge(val1, val2):
        """Adds a new edge to the graph.

         connecting the node containing ‘val1’ and the node containing ‘val2’.
         If either val1 or val2 are not already present in the graph,
         they should be added. If an edge already exists, overwrite it.
         """
        pass

    def del_node(val):
        """Deletes the node containing ‘val’ from the graph;

         raises an error if no such node exists.
         """
        pass

    def del_edge(val1, val2):
        """Deletes the edge connecting ‘val1’ and ‘val2’ from the graph;

        raises an error if no such edge exists.
        """
        pass

    def has_node(val):
        """True if node containing ‘val’ is in the graph, False if not."""
        pass

    def neighbors(val):
        """Returns the list of all nodes connected to the node containing
        ‘val’ by edges; raises an error if val is not in the graph."""
        pass

    def adjacent(val1, val2):
        """Returns True if there is an edge connecting val1 and val2,
        False if not; raises an error if either of the supplied
        values are not in g."""
        pass
