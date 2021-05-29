from algorithms.dijkstras_algorithm import DijkstraAlgorithm, generate_adjacency_matrix
from random_generation.graph_generators import generate_connected_graph
from visualization.nx_graph import display_weighted_nx_graph

import networkx as nx

if __name__ == "__main__":
    G = generate_connected_graph(6, 7)

    adj_matrix_with_distances = nx.to_numpy_array(G)
    adj_matrix_with_distances = adj_matrix_with_distances.tolist()
    adj_matrix = generate_adjacency_matrix(adj_matrix_with_distances)

    dijkstra = DijkstraAlgorithm(adj_matrix_with_distances, adj_matrix)
    dijkstra.all_shortest_paths(1)

    display_weighted_nx_graph(G)
