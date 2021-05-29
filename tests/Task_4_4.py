import networkx as nx

from algorithms.johnsons_algorithm import JohnsonAlgorithm
from random_generation.graph_generators import generate_strongly_connected_di_graph_with_weights
from visualization.nx_graph import display_weighted_nx_di_graph

if __name__ == "__main__":

    G, adj_matrix = generate_strongly_connected_di_graph_with_weights(5, 0.6, -2, 10)
    display_weighted_nx_di_graph(G)

    adj_matrix_with_distances = nx.to_numpy_array(G)
    adj_matrix_with_distances = adj_matrix_with_distances.tolist()

    johnson = JohnsonAlgorithm(adj_matrix_with_distances, adj_matrix)

    distance_matrix = johnson.johnson()

    print()
    for i in range(len(distance_matrix)):
        for j in distance_matrix[i]:
            print(str(j)+"  ", end='')
        print()
