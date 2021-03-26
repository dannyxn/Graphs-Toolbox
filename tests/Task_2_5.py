from algorithms.coherent_component import GraphRepresentationType, GraphRepresentation
from random_generation.regular_graph import k_regular_graph


if __name__ == "__main__":
    graph = k_regular_graph(7, 2)
    graph.display()
