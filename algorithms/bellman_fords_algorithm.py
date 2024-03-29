import sys


class BellmanFordAlgorithm:
    """
    Class BellmanFordAlgorithm contains methods used to find
    the shortest path using Bellman Ford algorithm.
    """

    def __init__(self, adj_matrix_with_distances: list, adj_matrix: list):
        self.number_of_nodes = len(adj_matrix_with_distances)
        self.distance_tab = [0 for _ in range(len(adj_matrix_with_distances))]
        self.previous_node_tab = [0 for _ in range(len(adj_matrix_with_distances))]
        self.adj_matrix_with_distances = adj_matrix_with_distances
        self.adj_matrix = adj_matrix

    def distances_init(self, source_node: int):
        for i in range(len(self.adj_matrix_with_distances)):
            self.distance_tab[i] = sys.maxsize
            self.previous_node_tab[i] = None
        self.distance_tab[source_node] = 0

    def relaxation(self, u: int, v: int):
        if self.distance_tab[v] > (self.distance_tab[u] + self.adj_matrix_with_distances[u][v]):
            self.distance_tab[v] = self.distance_tab[u] + self.adj_matrix_with_distances[u][v]
            self.previous_node_tab[v] = u

    def find_shortest_path(self, source_node: int) -> bool:
        self.distances_init(source_node)
        G = [j for j in range(self.number_of_nodes)]

        for i in range(self.number_of_nodes - 1):
            for u in G:
                for v in G:
                    if self.adj_matrix[u][v]:
                        self.relaxation(u, v)
        for u in G:
            for v in G:
                if self.adj_matrix[u][v]:
                    if self.distance_tab[v] > (self.distance_tab[u] + self.adj_matrix_with_distances[u][v]):
                        return False
        return True

    def all_shortest_paths(self, source_node: int):
        print("Distances from node: {}".format(source_node))
        if self.find_shortest_path(source_node):
            for i in range(len(self.distance_tab)):
                path_string = "d[{}] = {} ==> [".format(i, self.distance_tab[i])
                path_nodes_tab = []
                path_nodes_tab.append(i)
                x = self.previous_node_tab[i]
                while x != None:
                    path_nodes_tab.append(x)
                    x = self.previous_node_tab[x]

                path_nodes_tab.reverse()

                for i in range(len(path_nodes_tab) - 1):
                    path_string += "{} - ".format(path_nodes_tab[i])
                path_string += "{}".format(path_nodes_tab[len(path_nodes_tab) - 1])
                path_string += "]"
                print(path_string)
        else:
            print("ERROR negative cycle")

    def get_distances_list(self) -> list:
        return self.distance_tab.copy()
