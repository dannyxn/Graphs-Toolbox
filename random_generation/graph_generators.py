from collections import defaultdict
from random import randint, random

import networkx as nx

from algorithms.coherent_component import GraphRepresentationType, GraphRepresentation, CoherentComponentFinder


#can be improved
def generate_with_edges(number_of_nodes: int, number_of_edges: int) -> GraphRepresentation:
    reset = True
    graph = None
    while reset:
        graph = defaultdict(list, {degree: [] for degree in range(number_of_nodes)})
        for _ in range(number_of_edges):
            node1 = randint(0, number_of_nodes - 1)
            node2 = randint(0, number_of_nodes - 1)
            while node1==node2:
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
    G = defaultdict(list, {degree: [] for degree in range(number_of_nodes)})
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
