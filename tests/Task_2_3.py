from algorithms.coherent_component import CoherentComponentFinder
from core.graph_representation import GraphRepresentationType, GraphRepresentation

if __name__ == "__main__":
    raw_adjacency_matrix = [[0, 1, 0, 0, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 0],
                            [0, 0, 1, 0, 1, 1], [1, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0]]
    graph = GraphRepresentation(GraphRepresentationType.ADJACENCY_MATRIX, raw_adjacency_matrix)
    finder = CoherentComponentFinder()
    print("Największa składowa ma wierzchołki:")
    print(finder.find(graph))
    graph.convert(GraphRepresentationType.ADJACENCY_LIST)
    graph.display()

