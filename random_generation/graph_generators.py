from collections import defaultdict
from random import randint, random, choice

import networkx as nx
from typing import Tuple, List

from algorithms.Kosaraju_algorithm import component_list
from algorithms.checkers import check_if_seq_is_graphic
from algorithms.coherent_component import GraphRepresentationType, GraphRepresentation, CoherentComponentFinder
from algorithms.graph_randomization import randomize_graph

"""
This file contains methods to generate various types of graphs.
"""

"""
generate_with_edges method generate undirected graph based 
on the number of nodes and edges.

:param number_of_nodes: Int type number of nodes
:param number_of_edges: Int type number of edges

:return: Generated graph
:rtype: Adjacency List GraphRepresentation
"""


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
    return GraphRepresentation(GraphRepresentationType.ADJACENCY_LIST, graph)


"""
generate_with_probability method generate undirected graph based 
on the number of nodes and probability.

:param number_of_nodes: Int type number of nodes
:param number_of_edges: Float type number of the probability that
    there is an edge between two nodes

:return: Generated graph
:rtype: Adjacency List GraphRepresentation
"""


def generate_with_probability(number_of_nodes: int, probability: float) -> GraphRepresentation:
    G = defaultdict(list, {node: [] for node in range(number_of_nodes)})
    for node1 in range(number_of_nodes):
        for node2 in range(node1, number_of_nodes):
            if random() < probability:
                if node1 != node2:
                    G[node1].append(node2)
                    G[node2].append(node1)
    return GraphRepresentation(GraphRepresentationType.ADJACENCY_LIST, G)


"""
generate_random_euler_graph method generate undirected graph based 
on the number of nodes.

:param nodes: Int type number of nodes

:return: Generated graph
:rtype: Adjacency List GraphRepresentation
"""


def generate_random_euler_graph(nodes: int) -> GraphRepresentation:
    if nodes <= 2:
        raise ValueError("Invalid number of nodes provided")
    even_numbers_up_to_nodes = [number * 2 for number in range(1, nodes - 1)]
    graph = GraphRepresentation(GraphRepresentationType.GRAPHIC_SEQUENCE, [])
    is_graph_connected = False
    graphic_seq = []
    finder = CoherentComponentFinder()

    while not (is_graph_connected and check_if_seq_is_graphic(graphic_seq)):
        graphic_seq = []
        for _ in range(nodes):
            graphic_seq.append(choice(even_numbers_up_to_nodes))
        graph = GraphRepresentation(GraphRepresentationType.GRAPHIC_SEQUENCE, graphic_seq.copy())

        graph.convert(GraphRepresentationType.ADJACENCY_MATRIX)
        is_graph_connected = finder.check_if_graph_is_connected(graph)

    graph.convert(GraphRepresentationType.ADJACENCY_LIST)
    return graph


"""
generate_connected_graph method generate connected graph based 
on the number of nodes and paths.

:param nodes: Int type number of nodes
:param paths: Int type number of paths

:return: Generated connected graph
:rtype: nx.Graph
"""


def generate_connected_graph(nodes: int, paths: int) -> nx.Graph:
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


"""
generate_digraph_with_probability method generate digraph based 
on the number of nodes and probability.

:param number_of_nodes: Int type number of nodes
:param probability: Float type number of probability that
    there is an edge between two nodes

:return: Generated digraph
:rtype: nx.DiGraph
"""


def generate_digraph_with_probability(number_of_nodes: int, probability: float) -> nx.DiGraph:
    adjacency_list = defaultdict(list, {node: [] for node in range(number_of_nodes)})
    for node1 in range(number_of_nodes):
        for node2 in range(number_of_nodes):
            if random() < probability:
                if node1 != node2:
                    adjacency_list[node1].append(node2)
    return nx.DiGraph(adjacency_list)


"""
generate_strongly_connected_di_graph_with_weights method generate digraph 
with weights based on the number of nodes, probability and weight range

:param number_of_nodes: Int type number of nodes
:param probability: Float type number of probability that
    there is an edge between two nodes
:param down_value: Int type number representing the lower weight range
:param up_value: Int type number representing the upper weight range

:return: Generated digraph and matrix of branches
:rtype: tuple of nx.DiGraph and list[list]
"""


def generate_strongly_connected_di_graph_with_weights(num_of_nodes: int, probability: float, down_value: int = -5,
                                                      up_value: int = 10) -> Tuple[nx.DiGraph, List[list]]:
    while True:
        G = generate_digraph_with_probability(num_of_nodes, probability)
        component = component_list(G)
        if len(component) == 1:
            break
    adj_matrix = nx.to_numpy_array(G)
    branch_matrix = [[] for _ in G]
    for i in range(len(adj_matrix)):
        branch_matrix[i] = [False for _ in G]
    for i in range(len(branch_matrix)):
        for j in range(len(branch_matrix)):
            if adj_matrix[i][j] != 0:
                branch_matrix[i][j] = True

    for (u, v, w) in G.edges(data=True):
        w['weight'] = randint(down_value, up_value)
    return G, branch_matrix


"""
k_regular_graph method generate undirected k regular graph based 
on the number of nodes and degree.

:param number_of_nodes: Int type number of nodes
:param degree: Int type number of degree

:return: Generated graph
:rtype: Adjacency List GraphRepresentation
"""

def k_regular_graph(number_of_nodes: int, degree: int) -> GraphRepresentation:
    reset = True
    graph = None
    while reset:
        graph = defaultdict(list, {node: [] for node in range(number_of_nodes)})
        for _ in range(int((number_of_nodes * degree) / 2)):
            node1 = randint(0, number_of_nodes - 1)
            node2 = randint(0, number_of_nodes - 1)
            while node1 == node2:
                node1 = randint(0, number_of_nodes - 1)
                node2 = randint(0, number_of_nodes - 1)
            graph[node1].append(node2)
            graph[node2].append(node1)
        reset = False
        for node, neighbours in graph.items():
            if node in neighbours or len(neighbours) != degree:
                reset = True
            for x in neighbours:
                if neighbours.count(x) != 1:
                    reset = True
    return GraphRepresentation(GraphRepresentationType.ADJACENCY_LIST, graph)


"""
Class FLowNetworkGenerator contains methods used to generate
random flow network between single source and single sink. 
"""

class FLowNetworkGenerator:

    def generate_flow_network(self, N: int) -> nx.DiGraph:
        layers_edges = [1] + [randint(2, N) for _ in range(N)] + [1]
        G = nx.DiGraph()
        counter = 0
        layer_c = 0
        layers = []
        for i in range(len(layers_edges)):
            layers.append([])

        max_edges = 0
        for i in range(1, len(layers_edges) - 2):
            max_edges += self.return_n(layers_edges[i] + layers_edges[i + 1])
            if 1 < i < len(layers_edges) - 2:
                max_edges -= self.return_n(layers_edges[i])

        for i in layers_edges:
            for j in range(i):
                layers[layer_c].append(counter)
                G.add_node(counter, layer=layer_c)
                counter += 1
            layer_c += 1

        for i in range(1, len(layers) - 1):
            for node in layers[i]:
                G.add_edge(choice(layers[i - 1]), node, color='black')
                G.add_edge(node, choice(layers[i + 1]), color='black')

        all_edges = len(G.edges)
        all_edges -= layers_edges[1]
        all_edges -= layers_edges[len(layers_edges) - 2]

        edges = 0
        while edges < 2 * (len(layers) - 2) and all_edges < max_edges:
            layer_1 = randint(1, len(layers) - 2)

            if layer_1 == 1:
                layer_2 = randint(1, 2)
            elif layer_1 == len(layers) - 2:
                layer_2 = randint(len(layers) - 3, len(layers) - 2)
            else:
                layer_2 = randint(layer_1 - 1, layer_1 + 1)

            edge_1 = choice(layers[layer_1])
            edge_2 = choice(layers[layer_2])

            if G.has_edge(edge_1, edge_2) or G.has_edge(edge_2, edge_1) or edge_1 == edge_2:
                continue
            G.add_edge(edge_1, edge_2, color='red')
            edges += 1
            all_edges += 1

        return G

    @staticmethod
    def return_n(n):
        return (n * (n - 1)) / 2
