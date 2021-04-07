from collections import defaultdict
from random import randint, random
from algorithms.Kosaraju_algorithm import component_list

import networkx as nx
import numpy as np

from algorithms.coherent_component import GraphRepresentationType, GraphRepresentation, CoherentComponentFinder


# can be improved
from visualization.nx_graph import display_weighted_nx_di_graph


def generate_with_edges(number_of_nodes: int, number_of_edges: int) -> GraphRepresentation:
    reset = True
    graph = None
    while reset:
        graph = defaultdict(list, {degree: [] for degree in range(number_of_nodes)})
        for _ in range(number_of_edges):
            node1 = randint(0, number_of_nodes - 1)
            node2 = randint(0, number_of_nodes - 1)
            while node1 == node2:
                node2 = randint(0, number_of_nodes - 1)
            graph[node1].append(node2)
            graph[node2].append(node1)
            reset = False
            for node, neighbours in graph.items():
                if node in neighbours:
                    reset = True
                for x in neighbours:
                    if neighbours.count(x) != 1:
                        reset = True
    print(graph)
    return GraphRepresentation(GraphRepresentationType.ADJACENCY_LIST, graph)


def generate_with_probability(number_of_nodes: int, probability: float):
    G = defaultdict(list, {node: [] for node in range(number_of_nodes)})
    for node1 in range(number_of_nodes):
        for node2 in range(node1, number_of_nodes):
            if random() < probability:
                if node1 != node2:
                    G[node1].append(node2)
                    G[node2].append(node1)
    print(G)
    return GraphRepresentation(GraphRepresentationType.ADJACENCY_LIST, G)


def generate_connected_graph(nodes, paths) -> nx.Graph:
    finder = CoherentComponentFinder()
    while True:
        graph = generate_with_edges(nodes, paths)
        graph.convert(GraphRepresentationType.ADJACENCY_MATRIX)
        if finder.check_if_graph_is_connected(graph):
            break

    graph.convert(GraphRepresentationType.ADJACENCY_LIST)
    G = nx.Graph(graph.math_repr)
    for (u, v, w) in G.edges(data=True):
        w['weight'] = randint(1, 10)

    return G


def generate_diGraph_with_probability(number_of_nodes: int, probability: float) -> nx.DiGraph:
    adjency_list = defaultdict(list, {node: [] for node in range(number_of_nodes)})
    for node1 in range(number_of_nodes):
        for node2 in range(number_of_nodes):
            if random() < probability:
                if node1 != node2:
                    adjency_list[node1].append(node2)
    return nx.DiGraph(adjency_list)


def generate_strongly_connected_di_graph_with_weights(num_of_nodes, probability, down_value, up_value):
    while True:
        G = generate_diGraph_with_probability(num_of_nodes, probability)
        component = component_list(G)
        if len(component) == 1:
            for u, v in component.items():
                print(v, end=" ")
            print()
            break
    adj_matrix = nx.to_numpy_array(G)
    branch_matrix = [[] for _ in G]
    for i in range(len(adj_matrix)):
        branch_matrix[i] = [False for _ in G]
    for i in range(len(branch_matrix)):
        for j in range(len(branch_matrix)):
            if adj_matrix[i][j] != 0:
                branch_matrix[i][j] = True

    print(branch_matrix)
    for (u, v, w) in G.edges(data=True):
        w['weight'] = randint(down_value, up_value)
    return G, branch_matrix
