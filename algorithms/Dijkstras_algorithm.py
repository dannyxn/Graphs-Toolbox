import sys


class DijkstraAlgorithm:
    def __init__(self, adj_matrix: list, branch_matrix: list):
        self.distance_tab = [0 for j in range(len(adj_matrix))]
        self.previous_node_tab = [0 for j in range(len(adj_matrix))]
        self.adj_matrix = adj_matrix
        self.branch_matrix = branch_matrix

    def distances_init(self, source_node: int):
        for i in range(len(self.adj_matrix)):
            self.distance_tab[i] = sys.maxsize
            self.previous_node_tab[i] = None
        self.distance_tab[source_node] = 0

    def relaxation(self, u: int, v: int):
        if self.distance_tab[v] > (self.distance_tab[u] + self.adj_matrix[u][v]):
            self.distance_tab[v] = self.distance_tab[u] + self.adj_matrix[u][v]
            self.previous_node_tab[v] = u

    def find_shortest_path(self, source_node: int):
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
                if self.branch_matrix[u][v]:
                    self.relaxation(u, v)


    def all_shortest_paths(self, source_node: int):
        """
            all_shortest_paths method prints all
            shortest paths from given node to others
        """
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
        """
            create_distance_matrix method calculates and returns
            distance_matrix between each node in graph
        """
        distance_matrix = []
        for i in range(len(self.adj_matrix)):
            self.find_shortest_path(i)
            distance_matrix.append(self.distance_tab.copy())

        return distance_matrix.copy()

    def get_distance_list(self):
        return self.distance_tab.copy()


def generate_branch_matrix(adj_matrix):
    """
        method generates matrix of bools representing
        whether there is a branch between two nodes
    """
    G = [j for j in range(len(adj_matrix))]
    branch_matrix = [[] for _ in G]
    for i in range(len(adj_matrix)):
        branch_matrix[i] = [False for _ in G]
    for i in range(len(branch_matrix)):
        for j in range(len(branch_matrix)):
            if adj_matrix[i][j] != 0:
                branch_matrix[i][j] = True

    return branch_matrix
