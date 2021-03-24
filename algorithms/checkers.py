import numpy as np

from core.graph_representation import GraphRepresentation, GraphRepresentationType

def check_if_seq_is_graphic(sequence_of_numbers):
    a = np.array(sequence_of_numbers)
    a.sort()
    a = a[::-1]
    print(a)

    if a[a % 2 == 1].size % 2:
        return False

    while True:
        if all([v == 0 for v in a]):
            return True

        if a[0] < 0 or a[0] >= a.size or a[a < 0].size > 0:
            return False
        i = 1
        while i <= a[0]:
            a[i] = a[i] - 1
            i = i + 1
        a[0] = 0
        a.sort()
        a = a[::-1]


class HamiltonianGraphChecker:
    def __init__(self, graph: GraphRepresentation):
        graph.convert(GraphRepresentationType.ADJACENCY_MATRIX)
        self.adjacency_matrix = graph.math_repr
        self.number_of_nodes = len(self.adjacency_matrix)
        self.stack = [-1] * self.number_of_nodes
        self.stack[0] = 0

    def check_if_graph_is_hamiltonian(self) -> bool:

        if not self.__rec_hamiltonian_util(1):
            print("Given graph is not hamiltonian\n")
            return False

        self.__print_hamiltonian_cycle()
        return True

    def __rec_hamiltonian_util(self, actual_position: int) -> bool:
        if actual_position == self.number_of_nodes:
            if self.adjacency_matrix[self.stack[actual_position - 1]][self.stack[0]] == 1:
                return True
            else:
                return False

        for node in range(1, self.number_of_nodes):
            if self.__check_node_in_stack(node, actual_position):
                self.stack[actual_position] = node
                if self.__rec_hamiltonian_util(actual_position + 1):
                    return True
                self.stack[actual_position] = -1

        return False

    def __check_node_in_stack(self, node: int, actual_position: int) -> bool:
        if self.adjacency_matrix[self.stack[actual_position - 1]][node] == 0:
            return False

        for n in self.stack:
            if n == node:
                return False

        return True

    def __print_hamiltonian_cycle(self):
        print("Given graph is hamiltonian: ", end="")
        print("[", end="")
        for node in self.stack:
            print(node + 1, end=" - ")
        print(self.stack[0] + 1, end="")
        print("]\n")
