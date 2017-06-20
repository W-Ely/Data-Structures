"""Testing module for shortest path graph class."""
import pytest


@pytest.fixture
def graph():
    """Return initialized graph."""
    from shortest_path import WeightedGraph
    graph = WeightedGraph()
    return graph


@pytest.fixture
def complex_g(graph):
    """."""
    graph.add_edge('A', 'B', 10)
    graph.add_edge('A', 'C', 6)
    graph.add_edge('B', 'D', 3)
    graph.add_edge('B', 'E', 5)
    graph.add_edge('C', 'F', 8)
    graph.add_edge('C', 'G', 7)
    graph.add_edge('D', 'X', 4)
    graph.add_edge('D', 'Y', 9)
    graph.add_edge('E', 'B', 3)
    graph.add_edge('E', 'Z', 1)
    return graph


SIMPLE_WGRAPH = [("A", "B", 3), ("A", "D", 4), ("B", "C", 2), ("B", "E", 5), ("C", "D" , 1), ("C", "G", 6), ("D", "E", 3), ("D", "B", 4), ("E", "G", 5), ("E", "C", 2), ("E", "F", 5), ("F", "G", 2)]


@pytest.fixture
def simple_wgraph():
    """Return a simple weighted graph with edges."""
    from shortest_path import WeightedGraph
    wg = WeightedGraph()
    for edge in SIMPLE_WGRAPH:
        wg.add_edge(edge[0], edge[1], edge[2])
    return wg


def test_dijkstra_shortest_path(simple_wgraph):
    """Test dijkstra shortest path."""
    assert simple_wgraph.dijkstra("A", "G") == ["A", "B", "C", "G"]


def test_dijkstra_shortest_path_a_to_g(simple_wgraph):
    """Test the Dijkstra shortest path for simple graph, A to G."""
    assert simple_wgraph.dijkstra("A", "G") == ["A", "B", "C", "G"]


def test_dijkstra_shortest_path_b_to_d(simple_wgraph):
    """Test the Dijkstra shortest path for simple graph, B to D."""
    assert simple_wgraph.dijkstra("B", "D") == ["B", "C", "D"]


def test_dijkstra_shortest_path_a_to_f(simple_wgraph):
    """Test the Dijkstra shortest path for simple graph, A to F."""
    assert simple_wgraph.dijkstra("A", "F") == ["A", "D", "E", "F"]


def test_dijkstra_shortest_path_d_to_c(simple_wgraph):
    """Test the Dijkstra shortest path for simple graph, D to C."""
    assert simple_wgraph.dijkstra("D", "C") == ["D", "E", "C"]


def test_dijkstra_shortest_path_d_to_g(simple_wgraph):
    """Test the Dijkstra shortest path for simple graph, D to G."""
    assert simple_wgraph.dijkstra("D", "G") == ["D", "E", "G"]


def test_dijkstra_shortest_path_d_to_f(simple_wgraph):
    """Test the Dijkstra shortest path for simple graph, D to F."""
    assert simple_wgraph.dijkstra("D", "F") == ["D", "E", "F"]


def test_dijkstra_shortest_path_e_to_b(simple_wgraph):
    """Test the Dijkstra shortest path for simple graph, E to B."""
    assert simple_wgraph.dijkstra("E", "B") == ["E", "C", "D", "B"]


def test_dijkstra_shortest_path_e_to_d(simple_wgraph):
    """Test the Dijkstra shortest path for simple graph, E to D."""
    assert simple_wgraph.dijkstra("E", "D") == ["E", "C", "D"]


def test_floyd_warshall_shortest_path_a_to_g(simple_wgraph):
    """Test the floyd Warshall shortest path for simple graph, A to G."""
    assert simple_wgraph.floyd_warshall("A", "G") == ["A", "B", "C", "G"]


def test_floyd_warshall_shortest_path_b_to_d(simple_wgraph):
    """Test the floyd Warshall shortest path for simple graph, B to D."""
    assert simple_wgraph.floyd_warshall("B", "D") == ["B", "C", "D"]


def test_floyd_warshall_shortest_path_a_to_f(simple_wgraph):
    """Test the floyd Warshall shortest path for simple graph, A to F."""
    assert simple_wgraph.floyd_warshall("A", "F") == ["A", "D", "E", "F"]


def test_floyd_warshall_shortest_path_d_to_c(simple_wgraph):
    """Test the floyd Warshall shortest path for simple graph, D to C."""
    assert simple_wgraph.floyd_warshall("D", "C") == ["D", "E", "C"]


def test_floyd_warshall_shortest_path_d_to_g(simple_wgraph):
    """Test the floyd Warshall shortest path for simple graph, D to G."""
    assert simple_wgraph.floyd_warshall("D", "G") == ["D", "E", "G"]


def test_floyd_warshall_shortest_path_d_to_f(simple_wgraph):
    """Test the floyd Warshall shortest path for simple graph, D to F."""
    assert simple_wgraph.floyd_warshall("D", "F") == ["D", "E", "F"]


def test_floyd_warshall_shortest_path_e_to_b(simple_wgraph):
    """Test the floyd Warshall shortest path for simple graph, E to B."""
    assert simple_wgraph.floyd_warshall("E", "B") == ["E", "C", "D", "B"]


def test_floyd_warshall_shortest_path_e_to_d(simple_wgraph):
    """Test the floyd Warshall shortest path for simple graph, E to D."""
    assert simple_wgraph.floyd_warshall("E", "D") == ["E", "C", "D"]
