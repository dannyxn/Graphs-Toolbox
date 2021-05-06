import time

from random_generation.graph_generators import generate_connected_graph
from visualization.nx_graph import display_weighted_nx_graph

if __name__ == "__main__":
    start = time.time()
    G = generate_connected_graph(50, 60)
    print((time.time() - start))

    display_weighted_nx_graph(G)
