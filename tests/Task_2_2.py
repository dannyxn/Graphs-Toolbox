from algorithms.graph_randomization import randomize_graph
from core.graph_representation import GraphRepresentationType, GraphRepresentation

if __name__ == "__main__":
    adjacency_matrix = [[0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
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

    graph = GraphRepresentation(GraphRepresentationType.ADJACENCY_MATRIX, adjacency_matrix)
    graph.convert(GraphRepresentationType.ADJACENCY_LIST)
    graph.display()
    print(graph)

    randomized_graph = randomize_graph(graph, 10)
    randomized_graph.convert(GraphRepresentationType.ADJACENCY_LIST)
    randomized_graph.display()
    print(randomized_graph)
