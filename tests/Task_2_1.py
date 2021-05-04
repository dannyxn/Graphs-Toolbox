from algorithms.checkers import check_if_seq_is_graphic
from algorithms.graph_randomization import randomize_graph
from core.graph_representation import GraphRepresentation, GraphRepresentationType

if __name__ == "__main__":
    abc = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
    if check_if_seq_is_graphic(abc):
        graph = GraphRepresentation(GraphRepresentationType.GRAPHIC_SEQUENCE, abc)
        graph = randomize_graph(graph, 10)
        graph.convert(GraphRepresentationType.ADJACENCY_LIST)
        graph.display()
