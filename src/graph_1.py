"""Module implements a graph data strcture."""


class Graph(dict):
    """Create a graph data strcture modeled off a dictionary."""

    def __init__(self):
        """Inialize probably wont need anthing."""
        pass

    def nodes(self):
        """Return a list of all nodes in the graph."""
        return list(self.keys())

    def edges(self):
        """Return a list of all edges in the graph."""
        edges = []
        for key in self:
            if key:
                for edge in self[key]:
                    edges.append((key, edge))
        return edges

    def add_node(self, val):
        """Add a new node with value 'val' to the graph."""
        if val not in self:
            self.setdefault(val, [])

    def add_edge(self, val1, val2):
        """Add a new edge to the graph.

        connecting the node containing 'val1' and the node containing 'val2'.
        If either val1 or val2 are not already present in the graph,
        they should be added. If an edge already exists, overwrite it.
        """
        self.setdefault(val1, [])
        self.setdefault(val2, [])
        if val2 not in self[val1]:
            self[val1].append(val2)

    def del_node(self, val):
        """Delete the node containing 'val' from the graph.

        Raises an error if no such node exists.
        """
        try:
            del self[val]
            for key in self:
                if val in self[key]:
                    self[key].remove(val)
        except KeyError:
            raise ValueError('Value not in graph')

    def del_edge(self, val1, val2):
        """Delete the edge connecting 'val1' and 'val2' from the graph.

        Raises an error if no such edge exists.
        """
        try:
            self[val1].remove(val2)
        except ValueError:
            raise ValueError('No such edge.')

    def has_node(self, val):
        """True if node containing 'val' is in the graph, False if not."""
        return val in self

    def neighbors(self, val):
        """Return the list of all nodes connected to the node containing.

        'Val' by edges; raises an error if val is not in the graph.
        """
        if val in self:
            return self[val]
        else:
            raise ValueError('Value not in graph')

    def adjacent(self, val1, val2):
        """Return True if there is an edge connecting val1 and val2.

        False if not; raises an error if either of the supplied.
        values are not in g.
        """
        if val1 not in self or val2 not in self:
            raise ValueError('Node not found.')
        if val2 in self[val1]:
            return True
        return False

    def depth_first_traversal(self, start_val):
        """Return the path with depth transversal."""
        depth = []
        ref = []
        def recurse(start_val, depth):
            """."""
            print(depth)
            if start_val not in depth:
                depth.append(start_val)
                if self.neighbors(start_val):
                    for val in self.neighbors(start_val):
                        depth += self.depth_first_traversal(val)
        recurse(start_val, depth)
        return depth

    def breadth_first_traversal(self, start_val):
        """Return the path with breadth transversal."""
        pass


# empty_graph = Graph()
# empty_graph.add_edge(1, 2)
# empty_graph.add_edge(1, 3)
# empty_graph.add_edge(2, 4)
# empty_graph.add_edge(2, 5)
# empty_graph.add_edge(2, 6)
# empty_graph.add_edge()
# print(empty_graph.breadth_first_traversal(1))
