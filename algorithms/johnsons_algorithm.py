from algorithms.bellman_fords_algorithm import BellmanFordAlgorithm
from algorithms.dijkstras_algorithm import DijkstraAlgorithm


class JohnsonAlgorithm:
    def __init__(self, adj_matrix_with_distances: list, adj_matrix: list):
        self.number_of_nodes = len(adj_matrix_with_distances)
        self.distance_tab = [0 for j in range(len(adj_matrix_with_distances))]
        self.previous_node_tab = [0 for j in range(len(adj_matrix_with_distances))]
        self.adj_matrix_with_distances = adj_matrix_with_distances
        self.adj_matrix = adj_matrix

    def add_s(self) -> tuple:
        new_adj_matrix_with_distances = self.adj_matrix_with_distances.copy()
        new_adj_matrix = self.adj_matrix.copy()
        new_adj_matrix_with_distances.append([0.0 for j in range(self.number_of_nodes + 1)])
        new_node_list = [True for j in range(self.number_of_nodes)]
        new_node_list.append(False)
        new_adj_matrix.append(new_node_list)
        for i in range(self.number_of_nodes):
            new_adj_matrix_with_distances[i].append(0.0)
            new_adj_matrix[i].append(False)

        return new_adj_matrix_with_distances, new_adj_matrix

    def johnson(self) -> list:
        new_adj_matrix_with_distances, new_adj_matrix = self.add_s()
        new_G = [j for j in range(self.number_of_nodes + 1)]
        G = [j for j in range(self.number_of_nodes)]
        bellman = BellmanFordAlgorithm(new_adj_matrix_with_distances, new_adj_matrix)
        if not bellman.find_shortest_path(self.number_of_nodes):
            print("ERROR negative cycle")
            return []
        else:
            new_g_distances_tab = bellman.get_distances_list()
            for u in new_G:
                for v in new_G:
                    if new_adj_matrix[u][v]:
                        new_adj_matrix_with_distances[u][v] = new_adj_matrix_with_distances[u][v] + new_g_distances_tab[u] - new_g_distances_tab[v]
            new_adj_matrix.pop()
            new_adj_matrix_with_distances.pop()
            for i in range(self.number_of_nodes):
                new_adj_matrix[i].pop()
                new_adj_matrix_with_distances[i].pop()
            distance_matrix = [[0] * self.number_of_nodes for _ in range(self.number_of_nodes)]

            dijkstra = DijkstraAlgorithm(new_adj_matrix_with_distances, new_adj_matrix)
            for u in G:
                dijkstra.find_shortest_path(u)
                d_tab = dijkstra.get_distance_list()
                for v in G:
                    distance_matrix[u][v] = d_tab[v] - new_g_distances_tab[u] + new_g_distances_tab[v]

            return distance_matrix
