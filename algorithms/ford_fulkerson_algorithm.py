import networkx as nx


class FordFulkersonAlgorithm:
    def __init__(self, graph: nx.DiGraph):
        self.graph = nx.to_numpy_array(graph)
        self.number_of_nodes = len(graph)

    def BFS(self, s, t, parent):
        visited = [False] * self.number_of_nodes
        queue = [s]
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if not visited[ind] and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    def find_max_flow(self) -> int:
        """
        Find maximum flow between first node and last
        :return int: Maximum flow
        """
        parent = [-1] * self.number_of_nodes
        source, sink, max_flow = 0, self.number_of_nodes - 1, 0

        while self.BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow
