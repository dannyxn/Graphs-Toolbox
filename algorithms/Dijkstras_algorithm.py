import sys


class DijkstraAlgorithm():
    def __init__(self, adj_matrix):
        self.distance_tab = [0 for j in range(len(adj_matrix))]
        self.previous_node_tab = [0 for j in range(len(adj_matrix))]
        self.adj_matrix = adj_matrix

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
        S = []
        G = [j for j in range(len(self.adj_matrix))]
        while G:
            min = self.distance_tab[G[0]]
            index_of_min = G[0]
            for x in G:
                if (self.distance_tab[x] < min):
                    min = self.distance_tab[x]
                    index_of_min = x
            u = index_of_min
            S.append(u)
            G.remove(u)

            for v in G:
                if self.adj_matrix[u][v] != 0:
                    self.relaxation(u, v)

    def all_shortest_paths(self, source_node):
        print("Distances from node: {}".format(source_node))
        self.find_shortest_path(source_node)
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

    def create_distance_matrix(self):
        distance_matrix = []
        for i in range(len(self.adj_matrix)):
            self.find_shortest_path(i)
            distance_matrix.append(self.distance_tab.copy())

        return distance_matrix.copy()



