from core.graph_representation import GraphRepresentation, GraphRepresentationType

# TODO waiting for graphic seq -> adj matrix convert fix
if __name__ == "__main__":
    graphic_seq = [2, 2, 2, 2]
    graph = GraphRepresentation(GraphRepresentationType.GRAPHIC_SEQUENCE, graphic_seq)
    print(graph)
    graph.convert(GraphRepresentationType.ADJACENCY_MATRIX)
    print(graph)
