from algorithms.coherent_component import GraphRepresentationType, GraphRepresentation, CoherentComponentFinder
from random_generation.graph_generators import generate_connected_graph, generate_with_edges

if __name__ == "__main__":
    graph = generate_connected_graph(7, 8)
    print(graph.math_repr)
    graph.convert(GraphRepresentationType.ADJACENCY_LIST)
    graph.display()
    graph.convert(GraphRepresentationType.ADJACENCY_MATRIX)