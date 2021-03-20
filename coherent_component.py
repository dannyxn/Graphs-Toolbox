from enum import Enum


class GraphRepresentationType(Enum):
    ADJACENCY_MATRIX = 1


class GraphRepresentation:
    def __init__(self, repr_type: GraphRepresentationType, math_repr: list):
        self.repr_type = repr_type
        self.math_repr = math_repr

    def __len__(self) -> int:
        return len(self.math_repr)


class CoherentComponentFinder:
    def __init__(self):
        self.components = []

    def find(self, graph: GraphRepresentation) -> list:
        if graph.repr_type != GraphRepresentationType.ADJACENCY_MATRIX:
            raise ValueError("Adjacency matrix must be supplied for this algorithm")

        else:
            number_of_nodes = len(graph)
            component_index = 0
            self.components = [-1 for _ in range(number_of_nodes)]
            for node in range(number_of_nodes):
                if self.components[node] == -1:
                    component_index += 1
                    self.components[node] = component_index
                    self.find_recursively(graph, component_index, node)

            return self.components

    def find_recursively(self, graph: GraphRepresentation, component_index: int, node: int) -> None:
        for other_node in range(len(graph)):
            # if two nodes are neighbors
            if graph.math_repr[other_node][node] != 0:
                if self.components[other_node] == -1:
                    self.components[other_node] = component_index
                    self.find_recursively(graph, component_index, other_node)



