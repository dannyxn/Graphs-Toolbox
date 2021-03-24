from algorithms.checkers import HamiltonianGraphChecker
from core.graph_representation import *

if __name__ == "__main__":
    adj_matrix = [
        [0, 1, 0, 1, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 0, 0],
        [0, 1, 0, 1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0, 1, 1, 0],
        [1, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 0, 0, 1],
        [0, 0, 1, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 1, 1, 0]
    ]
    graph = GraphRepresentation(GraphRepresentationType.ADJACENCY_MATRIX, adj_matrix)
    ham_graph_checker = HamiltonianGraphChecker(graph)
    ham_graph_checker.check_if_graph_is_hamiltonian()
