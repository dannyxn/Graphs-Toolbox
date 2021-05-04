import sys
import numpy as np
import networkx as nx

"""
    find_minimum_spanning_tree methods used to fing mimimum spanning tree
    for given graph
    :param gr: nx.Graph type where we are looking for minimum spanning tree

    :return: minimum spanning tree as a grap
    :rtype: nx.Graph
"""
def find_minimum_spanning_tree(graph: nx.Graph) -> nx.Graph:
    # finding minimum spanning tree with Prim's algorithm performed for adjacency matrix
    adj_matrix = nx.to_numpy_array(graph)
    no_nodes = adj_matrix.shape[0]
    selected = np.zeros(no_nodes)
    minimum_spanning_tree = np.zeros((no_nodes, no_nodes))
    no_edge = 0
    selected[0] = True

    while no_edge < no_nodes - 1:
        minimum = sys.maxsize
        vertex_begin = 0
        vertex_end = 0
        for first_dim_iter in range(no_nodes):
            if selected[first_dim_iter]:
                for second_dim_iter in range(no_nodes):
                    if not selected[second_dim_iter] and adj_matrix[first_dim_iter][second_dim_iter]:
                        if minimum > adj_matrix[first_dim_iter][second_dim_iter]:
                            minimum = adj_matrix[first_dim_iter][second_dim_iter]
                            vertex_begin = first_dim_iter
                            vertex_end = second_dim_iter

        minimum_spanning_tree[vertex_begin][vertex_end] = adj_matrix[vertex_begin][vertex_end]
        minimum_spanning_tree[vertex_end][vertex_begin] = adj_matrix[vertex_begin][vertex_end]
        selected[vertex_end] = True
        no_edge += 1

    return nx.from_numpy_array(minimum_spanning_tree)

