from enum import Enum
import networkx as nx

from converters.type_conversions import (convert_adj_list_to_adj_matrix, convert_adj_matrix_to_adj_list,
                                         convert_adj_list_to_inc_matrix, convert_inc_matrix_to_adj_list,
                                         convert_adj_matrix_to_graph_seq, convert_graph_seq_to_adj_matrix)
from visualization.circle_representation import CircleRepresentation


class GraphRepresentationType(Enum):
    ADJACENCY_MATRIX = 1
    ADJACENCY_LIST = 2
    GRAPHIC_SEQUENCE = 3
    INCIDENCE_MATRIX = 4


class GraphRepresentation:
    def __init__(self, repr_type: GraphRepresentationType, math_repr):
        self.repr_type = repr_type
        self.math_repr = math_repr
        self.graphic_repr = CircleRepresentation()

    def __len__(self) -> int:
        return len(self.math_repr)

    def __str__(self):
        string_repr = ""
        if self.repr_type == GraphRepresentationType.ADJACENCY_MATRIX:
            string_repr += "Adjacency Matrix:\n"
        elif self.repr_type == GraphRepresentationType.ADJACENCY_LIST:
            string_repr += "Adjacency List:\n"
        elif self.repr_type == GraphRepresentationType.GRAPHIC_SEQUENCE:
            string_repr += "Graphic Sequence:\n"
        elif self.repr_type == GraphRepresentationType.INCIDENCE_MATRIX:
            string_repr += "Incidence matrix:\n"
        else:
            string_repr += "Unknown type:\n"

        string_repr += str(self.math_repr)
        return string_repr

    def display(self) -> None:
        if self.repr_type != GraphRepresentationType.ADJACENCY_LIST:
            raise NotImplementedError("Displaying only provided for ADJACENCY LIST")
        self.graphic_repr.display(self.math_repr)

    def convert(self, destination_type: GraphRepresentationType) -> bool:
        if destination_type == GraphRepresentationType.ADJACENCY_MATRIX:
            return self._convert_to_adjacency_matrix()

        elif destination_type == GraphRepresentationType.ADJACENCY_LIST:
            return self._convert_to_adjacency_list()

        elif destination_type == GraphRepresentationType.GRAPHIC_SEQUENCE:
            return self._convert_to_graphic_sequence()

        elif destination_type == GraphRepresentationType.INCIDENCE_MATRIX:
            return self._convert_to_incidence_matrix()
        else:
            return False

    def _convert_to_adjacency_matrix(self) -> bool:
        if self.repr_type == GraphRepresentationType.ADJACENCY_MATRIX:
            return False
        else:
            if self.repr_type == GraphRepresentationType.ADJACENCY_LIST:
                self.math_repr = convert_adj_list_to_adj_matrix(self.math_repr)
            elif self.repr_type == GraphRepresentationType.INCIDENCE_MATRIX:
                self.math_repr = convert_adj_list_to_adj_matrix(convert_inc_matrix_to_adj_list(self.math_repr))
            elif self.repr_type == GraphRepresentationType.GRAPHIC_SEQUENCE:
                self.math_repr = convert_graph_seq_to_adj_matrix(self.math_repr)
            else:
                raise ValueError("Conversion to this type is not supported")

            self.repr_type = GraphRepresentationType.ADJACENCY_MATRIX
            return True

    def _convert_to_adjacency_list(self) -> bool:
        if self.repr_type == GraphRepresentationType.ADJACENCY_LIST:
            return False
        else:
            if self.repr_type == GraphRepresentationType.ADJACENCY_MATRIX:
                self.math_repr = convert_adj_matrix_to_adj_list(self.math_repr)
            elif self.repr_type == GraphRepresentationType.INCIDENCE_MATRIX:
                self.math_repr = convert_inc_matrix_to_adj_list(self.math_repr)
            elif self.repr_type == GraphRepresentationType.GRAPHIC_SEQUENCE:
                self.math_repr = convert_adj_matrix_to_adj_list(convert_graph_seq_to_adj_matrix(self.math_repr))
            else:
                raise ValueError("Conversion to this type is not supported")

            self.repr_type = GraphRepresentationType.ADJACENCY_LIST
            return True

    def _convert_to_graphic_sequence(self) -> bool:
        if self.repr_type == GraphRepresentationType.GRAPHIC_SEQUENCE:
            return False
        else:
            if self.repr_type == GraphRepresentationType.ADJACENCY_MATRIX:
                self.math_repr = convert_adj_matrix_to_graph_seq(self.math_repr)
            elif self.repr_type == GraphRepresentationType.ADJACENCY_LIST:
                self.math_repr = convert_adj_matrix_to_graph_seq(convert_adj_list_to_adj_matrix(self.math_repr))
            elif self.repr_type == GraphRepresentationType.INCIDENCE_MATRIX:
                self.math_repr = convert_adj_matrix_to_graph_seq(
                    convert_inc_matrix_to_adj_list(convert_adj_list_to_adj_matrix(self.math_repr)))
            else:
                raise ValueError("Conversion to this type is not supported")

            self.repr_type = GraphRepresentationType.GRAPHIC_SEQUENCE
            return True

    def _convert_to_incidence_matrix(self) -> bool:
        if self.repr_type == GraphRepresentationType.INCIDENCE_MATRIX:
            return False
        else:
            if self.repr_type == GraphRepresentationType.ADJACENCY_MATRIX:
                self.math_repr = convert_adj_list_to_inc_matrix(convert_adj_matrix_to_adj_list(self.math_repr))
            elif self.repr_type == GraphRepresentationType.ADJACENCY_LIST:
                self.math_repr = convert_adj_list_to_inc_matrix(self.math_repr)
            elif self.repr_type == GraphRepresentationType.GRAPHIC_SEQUENCE:
                self.math_repr = convert_adj_list_to_inc_matrix(
                    convert_adj_matrix_to_adj_list(convert_graph_seq_to_adj_matrix(self.math_repr)))
            else:
                raise ValueError("Conversion to this type is not supported")

            self.repr_type = GraphRepresentationType.INCIDENCE_MATRIX
            return True
