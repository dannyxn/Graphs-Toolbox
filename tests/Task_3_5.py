from random_generation.graph_generators import generate_connected_graph
from visualization.nx_graph import display_weighted_nx_graph
from algorithms.minimum_spanning_tree import find_minimum_spanning_tree

if __name__ == "__main__":
    graph = generate_connected_graph(6, 12)
    display_weighted_nx_graph(graph, filename="input_graph.png")
    minimum_spanning_tree = find_minimum_spanning_tree(graph)
    display_weighted_nx_graph(minimum_spanning_tree, filename="mse.png")
