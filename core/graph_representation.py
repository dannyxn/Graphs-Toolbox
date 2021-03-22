from enum import Enum
from converters.type_conversions import (convert_adj_list_to_adj_matrix, convert_adj_matrix_to_adj_list,
                                         convert_adj_list_to_inc_matrix, convert_inc_matrix_to_adj_list)


class GraphRepresentationType(Enum):
    ADJACENCY_MATRIX = 1
    ADJACENCY_LIST = 2
    GRAPHIC_SEQUENCE = 3
    INCIDENCE_MATRIX = 4


class GraphRepresentation:
    def __init__(self, repr_type: GraphRepresentationType, math_repr):
        self.repr_type = repr_type
        self.math_repr = math_repr

    def __len__(self) -> int:
        return len(self.math_repr)

    def convert(self, destination_type: GraphRepresentationType) -> bool:
        if destination_type == GraphRepresentationType.ADJACENCY_MATRIX:
            if self.repr_type == GraphRepresentationType.ADJACENCY_MATRIX:
                return False
            else:
                if self.repr_type == GraphRepresentationType.ADJACENCY_LIST:
                    self.math_repr = convert_adj_list_to_adj_matrix(self.math_repr)
                elif self.repr_type == GraphRepresentationType.INCIDENCE_MATRIX:
                    self.math_repr = convert_adj_list_to_adj_matrix(convert_inc_matrix_to_adj_list(self.math_repr))
                else:
                    raise ValueError("Conversion to this type is not supported")

                self.repr_type = GraphRepresentationType.ADJACENCY_MATRIX
                return True

        elif destination_type == GraphRepresentationType.ADJACENCY_LIST:
            if self.repr_type == GraphRepresentationType.ADJACENCY_LIST:
                return False
            else:
                if self.repr_type == GraphRepresentationType.ADJACENCY_MATRIX:
                    self.math_repr = convert_adj_matrix_to_adj_list(self.math_repr)
                elif self.repr_type == GraphRepresentationType.INCIDENCE_MATRIX:
                    self.math_repr = convert_inc_matrix_to_adj_list(self.math_repr)
                else:
                    raise ValueError("Conversion to this type is not supported")

                self.repr_type = GraphRepresentationType.ADJACENCY_LIST
                return True

        elif destination_type == GraphRepresentationType.INCIDENCE_MATRIX:
            if self.repr_type == GraphRepresentationType.INCIDENCE_MATRIX:
                return False
            else:
                if self.repr_type == GraphRepresentationType.ADJACENCY_MATRIX:
                    self.math_repr = convert_adj_list_to_inc_matrix(convert_adj_matrix_to_adj_list(self.math_repr))
                elif self.repr_type == GraphRepresentationType.ADJACENCY_LIST:
                    self.math_repr = convert_adj_list_to_inc_matrix(self.math_repr)
                else:
                    raise ValueError("Conversion to this type is not supported")

                self.repr_type = GraphRepresentationType.INCIDENCE_MATRIX
                return True




