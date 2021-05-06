from algorithms.coherent_component import CoherentComponentFinder
from core.graph_representation import GraphRepresentationType, GraphRepresentation

if __name__ == "__main__":
    raw_adjacency_matrix = [[0, 1, 0, 0, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 0],
                            [0, 0, 1, 0, 1, 1], [1, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0]]
    graph = GraphRepresentation(GraphRepresentationType.ADJACENCY_MATRIX, raw_adjacency_matrix)
    finder = CoherentComponentFinder()
    components = finder.find(graph)
    most_common_component = max(components, key=components.count)
    new_components = []
    for i in range(len(components)):
        if components[i] == most_common_component:
            new_components.append(i + 1)
    print("Najwieksza składowa:")
    print(new_components)

    graph.convert(GraphRepresentationType.ADJACENCY_LIST)
    graph.display()

