from core.graph_representation import GraphRepresentation, GraphRepresentationType
from random import randint


def randomize_graph(graph: GraphRepresentation, number_of_randomization: int) -> GraphRepresentation:
    graph.convert(GraphRepresentationType.ADJACENCY_MATRIX)
    adjacency_matrix = graph.math_repr
    number_of_nodes = len(adjacency_matrix)

    for step in range(number_of_randomization):
        while True:
            while True:
                node_a = randint(0, number_of_nodes - 1)
                node_b = randint(0, number_of_nodes - 1)
                if ((adjacency_matrix[node_a][node_b] == adjacency_matrix[node_b][node_a]) and (
                        adjacency_matrix[node_b][node_a] == 1)) and node_a != node_b:
                    break

            while True:
                node_c = randint(0, number_of_nodes - 1)
                node_d = randint(0, number_of_nodes - 1)
                if ((adjacency_matrix[node_c][node_d] == adjacency_matrix[node_d][node_c]) and (
                        adjacency_matrix[node_c][node_d] == 1)) and node_c != node_d:
                    break

            if (adjacency_matrix[node_a][node_d] == 0) and (
                    adjacency_matrix[node_b][node_c] == 0) and node_a != node_d and node_b != node_c:
                break

        adjacency_matrix[node_a][node_b] = 0
        adjacency_matrix[node_b][node_a] = 0
        adjacency_matrix[node_c][node_d] = 0
        adjacency_matrix[node_d][node_c] = 0

        adjacency_matrix[node_a][node_d] = 1
        adjacency_matrix[node_d][node_a] = 1
        adjacency_matrix[node_b][node_c] = 1
        adjacency_matrix[node_c][node_b] = 1

    randomized_graph = GraphRepresentation(GraphRepresentationType.ADJACENCY_MATRIX, adjacency_matrix)

    return randomized_graph