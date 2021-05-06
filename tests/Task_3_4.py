from algorithms.Dijkstras_algorithm import DijkstraAlgorithm, generate_branch_matrix
from random_generation.graph_generators import generate_connected_graph
from algorithms.center_node import center_node, center_node_minimax
from visualization.nx_graph import display_weighted_nx_graph

import networkx as nx

if __name__ == "__main__":
    G = generate_connected_graph(6, 7)
    adj_matrix = nx.to_numpy_array(G)
    branch_matrix = generate_branch_matrix(adj_matrix)

    dijkstra = DijkstraAlgorithm(adj_matrix, branch_matrix)

    distance_matrix = dijkstra.create_distance_matrix()
    for i in range(len(distance_matrix)):
        print(f"{i}: ", distance_matrix[i], "\tsum:", sum(distance_matrix[i]), "\tmax", max(distance_matrix[i]))

    print(f"\ncenter node: {center_node(distance_matrix)}")
    print(f"center minimax node: {center_node_minimax(distance_matrix)}")
    display_weighted_nx_graph(G)
