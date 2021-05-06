"""
This file contains methods to find center node and center node minimax
"""


def center_node(weights_matrix: list) -> list:
    center = 0
    for row in range(len(weights_matrix)):
        if sum(weights_matrix[row]) < sum(weights_matrix[center]):
            center = row
    min = sum(weights_matrix[center])
    result = []
    for row in range(len(weights_matrix)):
        if sum(weights_matrix[row]) == min:
            result.append(row)
    return result


def center_node_minimax(weights_matrix: list) -> list:
    center = 0
    for row in range(len(weights_matrix)):
        if max(weights_matrix[row]) < max(weights_matrix[center]):
            center = row
    min = max(weights_matrix[center])
    result = []
    for row in range(len(weights_matrix)):
        if max(weights_matrix[row]) == min:
            result.append(row)
    return result
