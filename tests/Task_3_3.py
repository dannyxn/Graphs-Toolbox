from algorithms.Dijkstras_algorithm import DijkstraAlgorithm
from random_generation.graph_generators import generate_connected_graph
from visualization.circle_representation import display_weighted_nx_graph

import networkx as nx

if __name__ == "__main__":
    G = generate_connected_graph(6, 7)
    adj_matrix = nx.to_numpy_array(G)

    dijkstra = DijkstraAlgorithm(adj_matrix)
    distance_matrix = dijkstra.create_distance_matrix()
    for i in range(len(distance_matrix)):
        print(distance_matrix[i])

    display_weighted_nx_graph(G)