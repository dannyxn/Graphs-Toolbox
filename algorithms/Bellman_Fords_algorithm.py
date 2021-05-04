import sys

"""
Class BellmanFordAlgorithm contains methods used to find
the shortest path using Bellman Ford algorithm.
"""

class BellmanFordAlgorithm:
    def __init__(self, adj_matrix, branch_matrix):
        self.number_of_nodes = len(adj_matrix)
        self.distance_tab = [0 for _ in range(len(adj_matrix))]
        self.previous_node_tab = [0 for _ in range(len(adj_matrix))]
        self.adj_matrix = adj_matrix
        self.branch_matrix = branch_matrix

    def distances_init(self, source_node):
        for i in range(len(self.adj_matrix)):
            self.distance_tab[i] = sys.maxsize
            self.previous_node_tab[i] = None
        self.distance_tab[source_node] = 0

    def relaxation(self, u, v):
        if self.distance_tab[v] > (self.distance_tab[u] + self.adj_matrix[u][v]):
            self.distance_tab[v] = self.distance_tab[u] + self.adj_matrix[u][v]
            self.previous_node_tab[v] = u

    def find_shortest_path(self, source_node):
        self.distances_init(source_node)
        G = [j for j in range(self.number_of_nodes)]

        for i in range(self.number_of_nodes - 1):
            for u in G:
                for v in G:
                    if self.branch_matrix[u][v]:
                        self.relaxation(u, v)
        for u in G:
            for v in G:
                if self.branch_matrix[u][v]:
                    if self.distance_tab[v] > (self.distance_tab[u] + self.adj_matrix[u][v]):
                        return False
        return True

    def all_shortest_paths(self, source_node):
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

    def get_distances_list(self):
        return self.distance_tab.copy()