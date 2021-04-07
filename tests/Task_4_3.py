import networkx as nx

from algorithms.Kosaraju_algorithm import component_list
from random_generation.graph_generators import generate_diGraph_with_probability, \
    generate_strongly_connected_di_graph_with_weights

from algorithms.Bellman_Fords_algorithm import BellmanFordAlgorithm
from visualization.nx_graph import display_weighted_nx_graph, display_weighted_nx_di_graph

if __name__ == "__main__":
    # adj_matrix = [[0,2,2,0,0],
    #               [0,0,4,0,0],
    #               [0,0,0,2,4],
    #               [4,0,0,0,0],
    #               [0,2,0,2,0]
    # ]

    G, branch_matrix = generate_strongly_connected_di_graph_with_weights(5, 0.6, -2, 10)
    display_weighted_nx_di_graph(G)

    adj_matrix = nx.to_numpy_array(G)
    print(adj_matrix)

    x = BellmanFordAlgorithm(adj_matrix, branch_matrix)
    x.all_shortest_paths(0)
