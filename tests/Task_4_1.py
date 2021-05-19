import networkx as nx
import numpy as np

from random_generation.graph_generators import generate_digraph_with_probability
from visualization.nx_graph import display_nx_digraph

if __name__ == "__main__":
    G = generate_digraph_with_probability(10, 0.15)
    display_nx_digraph(G)

    g = nx.to_dict_of_lists(G)
    print("\n adjacency list")
    for node, neighbours in g.items():
        tmp = [str(x) for x in neighbours]
        print(f"{node}: {' '.join(tmp)}")

    g = nx.to_numpy_array(G)
    print("\n adjacency matrix")
    for row in g:
        tmp = [str(int(x)) for x in row]
        print(f"{' '.join(tmp)}")

    g = -nx.incidence_matrix(G, oriented=True)
    g = g.toarray()
    print("\n incidence matrix")
    for row in g:
        tmp = '\t'.join([str(int(x)) for x in row])
        print(f"{tmp}")
    print()
