from coherent_component import GraphRepresentationType, GraphRepresentation, CoherentComponentFinder


if __name__ == "__main__":
    raw_adjacency_matrix = [[0, 1, 0, 0, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 0],
                            [0, 0, 1, 0, 1, 1], [1, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0]]
    graph = GraphRepresentation(GraphRepresentationType.ADJACENCY_MATRIX, raw_adjacency_matrix)
    finder = CoherentComponentFinder()
    print(finder.find(graph))