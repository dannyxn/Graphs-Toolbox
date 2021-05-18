from algorithms.Bellman_Fords_algorithm import BellmanFordAlgorithm
from algorithms.Dijkstras_algorithm import DijkstraAlgorithm


class JohnsonAlgorithm:
    def __init__(self, adj_matrix: list, branch_matrix: list):
        self.number_of_nodes = len(adj_matrix)
        self.distance_tab = [0 for j in range(len(adj_matrix))]
        self.previous_node_tab = [0 for j in range(len(adj_matrix))]
        self.adj_matrix = adj_matrix
        self.branch_matrix = branch_matrix

    def add_s(self) -> tuple[list, list]:
        new_adj_matrix = self.adj_matrix.copy()
        new_branch_matrix = self.branch_matrix.copy()
        new_adj_matrix.append([0.0 for j in range(self.number_of_nodes + 1)])
        new_node_list = [True for j in range(self.number_of_nodes)]
        new_node_list.append(False)
        new_branch_matrix.append(new_node_list)
        for i in range(self.number_of_nodes):
            new_adj_matrix[i].append(0.0)
            new_branch_matrix[i].append(False)

        return new_adj_matrix, new_branch_matrix

    def johnson(self) -> list:
        new_adj_matrix, new_branch_matrix = self.add_s()
        new_G = [j for j in range(self.number_of_nodes + 1)]
        G = [j for j in range(self.number_of_nodes)]
        bellman = BellmanFordAlgorithm(new_adj_matrix, new_branch_matrix)
        if not bellman.find_shortest_path(self.number_of_nodes):
            print("ERROR negative cycle")
            return []
        else:
            new_g_distances_tab = bellman.get_distances_list()
            for u in new_G:
                for v in new_G:
                    if new_branch_matrix[u][v]:
                        new_adj_matrix[u][v] = new_adj_matrix[u][v] + new_g_distances_tab[u] - new_g_distances_tab[v]
            new_branch_matrix.pop()
            new_adj_matrix.pop()
            for i in range(self.number_of_nodes):
                new_branch_matrix[i].pop()
                new_adj_matrix[i].pop()
            distance_matrix = [[0] * self.number_of_nodes for _ in range(self.number_of_nodes)]

            dijkstra = DijkstraAlgorithm(new_adj_matrix, new_branch_matrix)
            for u in G:
                dijkstra.find_shortest_path(u)
                d_tab = dijkstra.get_distance_list()
                for v in G:
                    distance_matrix[u][v] = d_tab[v] - new_g_distances_tab[u] + new_g_distances_tab[v]

            return distance_matrix
