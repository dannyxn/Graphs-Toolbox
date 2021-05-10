from algorithms.coherent_component import CoherentComponentFinder
from core.graph_representation import GraphRepresentationType, GraphRepresentation
from random_generation.graph_generators import generate_with_probability

if __name__ == "__main__":
    raw_adjacency_matrix = [[0, 1, 0, 0, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 0],
                            [0, 0, 1, 0, 1, 1], [1, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0]]
    #graph = GraphRepresentation(GraphRepresentationType.ADJACENCY_MATRIX, raw_adjacency_matrix)
    graph = generate_with_probability(7, 0.3)
    graph.convert(GraphRepresentationType.ADJACENCY_MATRIX)
    finder = CoherentComponentFinder()
    ret = finder.most_common_component(graph)
    print("Najwieksza składowa:")
    print(ret)

    graph.convert(GraphRepresentationType.ADJACENCY_LIST)
    graph.display()

