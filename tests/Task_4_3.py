from algorithms.Kosaraju_algorithm import component_list
from random_generation.graph_generators import generate_diGraph_with_probability, \
    generate_strongly_connected_di_graph_with_weights

from algorithms.Bellman_Fords_algorithm import BellmanFordAlgorithm
from visualization.nx_graph import display_weighted_nx_graph, display_weighted_nx_di_graph

if __name__ == "__main__":
    adj_matrix = [[0,2,2,0,0],
                  [0,0,4,0,0],
                  [0,0,0,2,4],
                  [4,0,0,0,0],
                  [0,2,0,2,0]
    ]

    G = generate_strongly_connected_di_graph_with_weights(5,0.3,-5,10)
    display_weighted_nx_di_graph(G)



    x = BellmanFordAlgorithm(adj_matrix)
    x.all_shortest_paths(4)
