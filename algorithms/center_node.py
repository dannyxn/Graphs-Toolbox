def center_node(weights_matrix) -> int:
    center = 1
    for row in range(len(weights_matrix)):
        if sum(weights_matrix[row]) < sum(weights_matrix[center]):
            center = row
    return center


def center_node_minimax(weights_matrix) -> int:
    center = 1
    for row in range(len(weights_matrix)):
        if max(weights_matrix[row]) < max(weights_matrix[center]):
            center = row
    return center
