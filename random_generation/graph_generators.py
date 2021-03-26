from collections import defaultdict
from random import randint, random

from algorithms.coherent_component import GraphRepresentationType, GraphRepresentation, CoherentComponentFinder


def generate_with_edges(number_of_nodes: int, number_of_edges: int) -> GraphRepresentation:
    G = defaultdict(list, {degree: [] for degree in range(number_of_nodes)})
    for _ in range(number_of_edges):
        x = randint(0, number_of_nodes - 1)
        y = randint(0, number_of_nodes - 1)
        while True:
            if y != x and y not in G[x]:
                break
            y = randint(0, number_of_nodes - 1)
        G[x].append(y)
        G[y].append(x)
    return GraphRepresentation(GraphRepresentationType.ADJACENCY_LIST, G)


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


def generate_connected_graph(nodes, paths) -> GraphRepresentation:
    finder = CoherentComponentFinder()
    while True:
        graph = generate_with_edges(nodes, paths)
        graph.convert(GraphRepresentationType.ADJACENCY_MATRIX)
        if finder.check_if_graph_is_connected(graph):
            break
    return graph