import networkx as nx

from algorithms.Johnsons_algorithm import JohnsonAlgorithm
from random_generation.graph_generators import generate_strongly_connected_di_graph_with_weights
from visualization.nx_graph import display_weighted_nx_di_graph

if __name__ == "__main__":
    # adj_matrix = [[0 ,2 ,2 ,0 ,0],
    #               [0 ,0 ,4 ,0 ,0],
    #               [0 ,0 ,0 ,2 ,4],
    #               [4 ,0 ,0 ,0 ,0],
    #               [0 ,2 ,0 ,2 ,0]
    # ]

    G, branch_matrix = generate_strongly_connected_di_graph_with_weights(3, 0.6, -5, 10)
    display_weighted_nx_di_graph(G)

    adj_matrix = nx.to_numpy_array(G)
    adj_matrix = adj_matrix.tolist()
    # print(adj_matrix)
    johnson = JohnsonAlgorithm(adj_matrix,branch_matrix)

    distance_matrix = johnson.johnson()

    print()
    for i in range(len(distance_matrix)):
        print(distance_matrix[i])
