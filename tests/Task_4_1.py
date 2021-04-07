from random_generation.graph_generators import generate_diGraph_with_probability
from visualization.nx_graph import display_nx_DiGraph
import networkx as nx

if __name__ == "__main__":
    G = generate_diGraph_with_probability(7,0.3)
    display_nx_DiGraph(G)