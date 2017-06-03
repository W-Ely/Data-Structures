"""Module tests the graph datastructure."""
import pytest


@pytest.fixture
def empty_graph():
    """Create an empty graph."""
    from graph import Graph
    return Graph()

def tri_graph(empty_graph):
    """Create a graph with 3 nodes one pointing to next in circle."""
    from graph import Graph
    new_graph = empty_graph
    
    return
