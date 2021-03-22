from core.graph_representation import GraphRepresentation, GraphRepresentationType
from random import randint
from collections import defaultdict


def degree_regular_graph(number_of_nodes: int, degree: int) -> GraphRepresentation:
    reset = True
    graph = None
    while reset:
        graph = defaultdict(list, {degree: [] for degree in range(number_of_nodes)})
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

