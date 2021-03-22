from core.graph_representation import GraphRepresentationType, GraphRepresentation

if __name__ == "__main__":
    graph = GraphRepresentation(GraphRepresentationType.ADJACENCY_MATRIX, [[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    graph.convert(GraphRepresentationType.ADJACENCY_LIST)
    graph.display()
