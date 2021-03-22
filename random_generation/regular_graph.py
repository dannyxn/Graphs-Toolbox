from core.graph_representation import GraphRepresentation, GraphRepresentationType
from random import randint
from collections import defaultdict


def k_regular_graph(n, k):
    reset = True
    graph = None
    while reset:
        graph = defaultdict(list, {k: [] for k in range(n)})
        for _ in range(int((n * k) / 2)):
            vertex1 = randint(0, n - 1)
            vertex2 = randint(0, n - 1)
            while vertex1 == vertex2:
                vertex1 = randint(0, n - 1)
                vertex2 = randint(0, n - 1)
            graph[vertex1].append(vertex2)
            graph[vertex2].append(vertex1)
        reset = False
        for vertex, neighbours in graph.items():
            if vertex in neighbours or len(neighbours) != k:
                reset = True
            for x in neighbours:
                if neighbours.count(x) != 1:
                    reset = True
    return GraphRepresentation(GraphRepresentationType.ADJACENCY_LIST, graph)

