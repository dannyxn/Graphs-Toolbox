from core.graph_representation import GraphRepresentation, GraphRepresentationType
from algorithms.checkers import check_if_seq_is_graphic
from algorithms.coherent_component import CoherentComponentFinder
import random


def generate_random_euler_graph(nodes: int) -> GraphRepresentation:
    even_numbers_up_to_nodes = [number * 2 for number in range(1, nodes - 1)]
    graph = GraphRepresentation(GraphRepresentationType.GRAPHIC_SEQUENCE, [])
    is_graph_connected = False
    graphic_seq = []
    finder = CoherentComponentFinder()

    while not (is_graph_connected and check_if_seq_is_graphic(graphic_seq)):
        graphic_seq = []
        for _ in range(nodes):
            graphic_seq.append(random.choice(even_numbers_up_to_nodes))
        graph = GraphRepresentation(GraphRepresentationType.GRAPHIC_SEQUENCE, graphic_seq.copy())

        graph.convert(GraphRepresentationType.ADJACENCY_MATRIX)
        is_graph_connected = finder.check_if_graph_is_connected(graph)

    graph.convert(GraphRepresentationType.ADJACENCY_LIST)
    return graph







