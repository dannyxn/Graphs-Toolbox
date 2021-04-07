from random_generation.graph_generators import generate_connected_graph
from visualization.nx_graph import display_weighted_nx_graph

if __name__ == "__main__":
    G = generate_connected_graph(7, 8)
    display_weighted_nx_graph(G)


