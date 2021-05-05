from algorithms.graph_randomization import randomize_graph
from core.graph_representation import GraphRepresentationType
from random_generation.graph_generators import k_regular_graph

if __name__ == "__main__":
    graph = k_regular_graph(6, 3)

    #graph.display()

    randomized_graph = randomize_graph(graph, 100)
    randomized_graph.convert(GraphRepresentationType.ADJACENCY_LIST)
    randomized_graph.display()
    print(randomized_graph)
