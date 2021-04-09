from core.graph_representation import GraphRepresentationType, GraphRepresentation
from collections import defaultdict
from copy import deepcopy


class EulerCycleFinder:
    def __init__(self):
        self.no_nodes = 0
        self.adjacency_list = defaultdict(list)
        self.result = []

    def find(self, graph: GraphRepresentation) -> list:
        graph.convert(GraphRepresentationType.ADJACENCY_LIST)
        self.adjacency_list = deepcopy(graph.math_repr)
        self.no_nodes = len(self.adjacency_list)
        cur_node = 0
        for node_idx in range(self.no_nodes):
            if len(self.adjacency_list[node_idx]):
                cur_node = node_idx
                break

        self._find_util(cur_node)

        string_repr = "->".join(str(first) for first, second in self.result)
        print(string_repr)
        return self.result

    def _find_util(self, cur_node):
        for other_node in self.adjacency_list[cur_node]:
            if self._is_next_edge_valid(cur_node, other_node):
                self.result.append((cur_node, other_node))
                self._remove_edge(cur_node, other_node)
                self._find_util(other_node)

    def _remove_edge(self, cur_node, other_node):
        for index, key in enumerate(self.adjacency_list[cur_node]):
            if key == other_node:
                self.adjacency_list[cur_node].pop(index)
        for index, key in enumerate(self.adjacency_list[other_node]):
            if key == cur_node:
                self.adjacency_list[other_node].pop(index)

    def _dfs_count(self, other_node, visited):
        count = 1
        visited[other_node] = True
        for i in self.adjacency_list[other_node]:
            if visited[i]:
                count = count + self._dfs_count(i, visited)
        return count

    def _is_next_edge_valid(self, cur_node, other_node):
        if len(self.adjacency_list[cur_node]) == 1:
            return True
        else:
            visited = [False] * self.no_nodes
            count1 = self._dfs_count(cur_node, visited)

            self._remove_edge(cur_node, other_node)
            visited = [False] * self.no_nodes
            count2 = self._dfs_count(cur_node, visited)

            self.adjacency_list[cur_node].append(other_node)
            self.adjacency_list[other_node].append(cur_node)

            return not count1 > count2
