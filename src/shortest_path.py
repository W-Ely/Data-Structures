"""Module that implements the shortest path algorithms."""
from weighted_graph import WeightedGraph


def dijkstra(graph, start, end):
    """Dijkstra algorithm for finding the shortest path."""
    tent_dict = {key: int('inf') for key in graph.nodes()}
    edges = {(edge[0], edge[1]): edge[2] for edge in graph.edges()}
    unvisited = {key for key in graph.nodes()}
    tent_dict[start] = 0
    current_node = graph[start]
    while unvisited:
        for edge in current_node:
            neighbor = edge.keys()[0]
            distance = edge.values()[0]
            if tent_dict[neighbor] > distance:
                tent_dict[neighbor] = distance


def other_shortest_path():
    """Which will we choose."""
    pass


new_graph = WeightedGraph()
new_graph.add_edge('a', 'b', 1)
new_graph.add_edge('a', 'c', 3)
new_graph.add_edge('b', 'd', 2)
new_graph.add_edge('c', 'd', 4)
