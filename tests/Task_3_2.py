from algorithms.Dijkstras_algorithm import DijkstraAlgorithm, generate_branch_matrix
from random_generation.graph_generators import generate_connected_graph
from visualization.nx_graph import display_weighted_nx_graph

import networkx as nx

if __name__ == "__main__":
    G = generate_connected_graph(6, 7)

    adj_matrix = nx.to_numpy_array(G)
    adj_matrix = adj_matrix.tolist()
    branch_matrix = generate_branch_matrix(adj_matrix)

    dijkstra = DijkstraAlgorithm(adj_matrix, branch_matrix)
    dijkstra.all_shortest_paths(1)

    display_weighted_nx_graph(G)
