from copy import deepcopy

from core.graph_representation import GraphRepresentationType, GraphRepresentation


class EulerCycleFinder:
    """
    EulerCycleFinder class contains methods used to find euler cycle
    inside given graph.
    """

    def __init__(self):
        self.no_nodes = 0
        self.result = []
        self.adjacency_matrix = []

    def find_euler_cycle(self, graph: GraphRepresentation) -> list:
        graph.convert(GraphRepresentationType.ADJACENCY_MATRIX)
        self.adjacency_matrix = deepcopy(graph.math_repr)
        self.no_nodes = len(graph.math_repr)
        self.depth_first_search(0)

        string_repr = "->".join(str(first) for first in self.result)
        print(string_repr)
        return self.result

    def depth_first_search(self, v):
        for u in range(self.no_nodes):
            if self.adjacency_matrix[v][u] > 0:
                self.adjacency_matrix[v][u] -= 1
                self.adjacency_matrix[u][v] -= 1
                self.depth_first_search(u)
        self.result.append(v)
