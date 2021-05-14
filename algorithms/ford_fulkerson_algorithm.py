import networkx as nx


class FordFulkersonAlgorithm:

    def __init__(self, graph: nx.DiGraph):
        self.graph = graph
        self.number_of_nodes = len(graph)

    def FordFulkerson(self, source: int, sink: int) -> int:
        max_flow = 0
        # TO DO
        return max_flow

    def BFS(self, source: int, sink: int, parent: list) -> bool:
        visited = [False for _ in range(self.number_of_nodes)]

        queue = [source]
        visited[source] = True

        print(self.graph[0])
        while queue:
            node = queue.pop(0)

            for neighbour in self.graph[node]:
                if not visited[neighbour]:

                    if neighbour == sink:
                        visited[neighbour] = True
                        return True

                    queue.append(neighbour)
                    visited[neighbour] = True
                    parent[neighbour] = node

        return False
