"""Testing module for shortest path graph class."""
import pytest


@pytest.fixture
def graph():
    """Init a graph from wgraph."""
    from shortest_path import WeightedGraph
    return WeightedGraph()


@pytest.fixture
def traverse(graph):
    """."""
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(2, 6)
    return graph


@pytest.fixture
def loop(graph):
    """."""
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(2, 6)
    graph.add_edge(6, 1)
    return graph


@pytest.fixture
def more_complex(graph):
    """."""
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(2, 6)
    graph.add_edge(3, 7)
    graph.add_edge(6, 1)
    graph.add_edge(4, 12)
    graph.add_edge(10, 13)
    return graph


@pytest.fixture
def tri_graph(graph):
    """Create a graph with 3 nodes one pointing to next in circle."""
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)
    return graph


def test_init_creates_graph(graph):
        """Initialize and empty graph."""
        assert graph.nodes() == []


def test_nodes_returns_list_of_all_nodes(tri_graph):
    """Return a list of all nodes in the graph."""
    assert tri_graph.nodes() == [1, 2, 3]


def test_edges_returns_list_of_all_edges(tri_graph):
    """Return a list of all edges in the graph."""
    tri_graph.add_edge(3, 2)
    assert tri_graph.edges() == [(1, 2, 0), (2, 3, 0), (3, 1, 0), (3, 2, 0)]


def test_add_node_adds_node(graph):
    """Add a new node with value 'val' to the graph."""
    graph.add_node('test')
    assert graph.nodes() == ['test']


def test_add_edge_adds_an_edge(tri_graph):
    """Add a new edge to the graph."""
    tri_graph.add_edge(3, 2)
    assert tri_graph.neighbors(3) == [1, 2]


def test_del_node_removes_a_node(tri_graph):
    """Delete the node containing 'val' from the graph."""
    tri_graph.del_node(3)
    assert tri_graph.nodes() == [1, 2]


def test_del_node_3_and_check_two_has_no_neighbors(tri_graph):
    """Delete the node containing 3 and check that 2 has no neighbors."""
    tri_graph.del_node(3)
    assert tri_graph.neighbors(2) == []


def test_del_node_raises_ValueError_when_node_not_in_graph(tri_graph):
    """Raise an error if no such node exists."""
    with pytest.raises(ValueError):
        tri_graph.del_node(10)


def test_del_edge_removes_edge_from_node(tri_graph):
    """Delete the edge connecting 'val1' and 'val2' from the graph."""
    tri_graph.del_edge(1, 2)
    assert tri_graph.neighbors(1) == []


def test_del_edge_raises_ValueError_when_edge_not_on_node(tri_graph):
    """Raise an error if no such edge exists."""
    with pytest.raises(ValueError):
        tri_graph.del_edge(1, 3)


def test_has_node_returns_true_or_false_if_node_present_or_not(tri_graph):
    """True if node containing 'val' is in the graph, False if not."""
    assert tri_graph.has_node(4) is False
    assert tri_graph.has_node(1) is True


def test_neighbors_returns_list_of_neighbors(tri_graph):
    """Return the list of all nodes connected to the node."""
    tri_graph.add_edge(3, 2)
    assert tri_graph.neighbors(3) == [1, 2]


def test_neighbors_raises_ValueError_if_node_not_in_graph(tri_graph):
    """Return the list of all nodes connected to the node."""
    with pytest.raises(ValueError):
        tri_graph.neighbors(4)


def test_adjacent_returns_true_or_false_if_node_has_the_edge_not(tri_graph):
    """Return True if there is an edge connecting val1 and val2."""
    assert tri_graph.adjacent(1, 2) is True
    assert tri_graph.adjacent(1, 3) is False


def test_adjacent_raises_ValueError_if_either_are_not_in_graph(tri_graph):
    """Raise an error if either of the supplied values are not in graph."""
    with pytest.raises(ValueError):
        tri_graph.adjacent(1, 4)
    with pytest.raises(ValueError):
        tri_graph.adjacent(4, 1)


def test_depth_first_transversal(traverse):
    """."""
    assert traverse.depth_first_traversal(1) == [1, 2, 4, 5, 6, 3]


def test_depth_first_transversal_more_complex(more_complex):
    """."""
    assert more_complex.depth_first_traversal(1) == [
        1, 2, 4, 12, 5, 6, 3, 7
    ]


def test_depth_first_transversal_start_value_not_in_graph(traverse):
    """."""
    with pytest.raises(ValueError):
        traverse.depth_first_traversal(25)


def test_depth_first_traversal_with_loop(loop):
    """."""
    assert loop.depth_first_traversal(1) == [1, 2, 4, 5, 6, 3]


def test_breadth_first_traversal(traverse):
    """."""
    assert traverse.breadth_first_traversal(1) == [1, 2, 3, 4, 5, 6]


def test_breadth_first_transversal_more_complex(more_complex):
    """."""
    assert more_complex.breadth_first_traversal(1) == [
        1, 2, 3, 4, 5, 6, 7, 12
    ]


def test_breath_first_transversal_start_value_not_in_graph(more_complex):
    """."""
    with pytest.raises(ValueError):
        more_complex.breadth_first_traversal(25)


def test_breadth_first_traversal_with_loop(loop):
    """."""
    assert loop.breadth_first_traversal(1) == [1, 2, 3, 4, 5, 6]


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
