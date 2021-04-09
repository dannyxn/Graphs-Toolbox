from core.graph_representation import GraphRepresentationType, GraphRepresentation


if __name__ == "__main__":
    graph = GraphRepresentation(GraphRepresentationType.ADJACENCY_MATRIX, [[0,  1, 0], [1, 0, 1], [0, 1, 0]])
    graph.convert(GraphRepresentationType.ADJACENCY_LIST)
    print(graph)
    graph.convert(GraphRepresentationType.ADJACENCY_MATRIX)
    print(graph)
    graph.convert(GraphRepresentationType.INCIDENCE_MATRIX)
    print(graph)

