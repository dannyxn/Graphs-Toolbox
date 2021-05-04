import networkx as nx
from core.graph_representation import GraphRepresentationType
from random_generation.graph_generators import generate_random_euler_graph
from visualization.nx_graph import display_nx_graph
from algorithms.euler_cycle import EulerCycleFinder


if __name__ == "__main__":
    graph = generate_random_euler_graph(10)
    graph.convert(GraphRepresentationType.ADJACENCY_LIST)
    print(graph)

    finder = EulerCycleFinder()
    finder.find_euler_cycle(graph)

    graph.convert(GraphRepresentationType.ADJACENCY_LIST)
    graph = nx.Graph(graph.math_repr)
    display_nx_graph(graph)
