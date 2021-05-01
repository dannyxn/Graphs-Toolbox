from core.graph_representation import GraphRepresentationType, GraphRepresentation


if __name__ == "__main__":
    matrix = [[0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
              [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0],
              [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
              [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
              [0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0]]
    graph = GraphRepresentation(GraphRepresentationType.ADJACENCY_MATRIX, matrix)
    graph.convert(GraphRepresentationType.ADJACENCY_LIST)
    print(graph)
    graph.convert(GraphRepresentationType.ADJACENCY_MATRIX)
    print(graph)
    graph.convert(GraphRepresentationType.INCIDENCE_MATRIX)
    print(graph)