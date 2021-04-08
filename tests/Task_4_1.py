from random_generation.graph_generators import generate_digraph_with_probability
from visualization.nx_graph import display_nx_digraph
import networkx as nx

if __name__ == "__main__":
    G = generate_digraph_with_probability(7, 0.3)
    display_nx_digraph(G)

    g = nx.to_dict_of_lists(G)
    print("\n adjency list")
    print(g)

    g = nx.to_numpy_matrix(G)
    print("\n adjency matrix")
    print(g)

    g = -nx.incidence_matrix(G, oriented=True)
    print("\n incidence matrix")
    print(g.toarray())