from core.graph_representation import GraphRepresentation, GraphRepresentationType


class CoherentComponentFinder:
    """
    CoherentComponentFinder class contains methods used to find
    the biggest coherent component in given graph.
    """
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
                    self._find_recursively(graph, component_index, node)

            return self.components

    def _find_recursively(self, graph: GraphRepresentation, component_index: int, node: int) -> None:
        for other_node in range(len(graph)):
            # if two nodes are neighbors
            if graph.math_repr[other_node][node] != 0:
                if self.components[other_node] == -1:
                    self.components[other_node] = component_index
                    self._find_recursively(graph, component_index, other_node)

    def check_if_graph_is_connected(self, graph: GraphRepresentation) -> bool:
        return all(v == 1 for v in self.find(graph))
