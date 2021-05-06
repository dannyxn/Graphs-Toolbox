from collections import defaultdict, OrderedDict


def convert_adj_matrix_to_adj_list(adjacency_matrix: list) -> defaultdict:
    """
        convert_adj_matrix_to_adj_list method converts given adjacency
        matrix to adjacency list
    """
    adj_list = defaultdict(list, {degree: [] for degree in range(len(adjacency_matrix))})
    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix[i])):
            if adjacency_matrix[i][j]:
                adj_list[i].append(j)

    return adj_list


def convert_adj_list_to_adj_matrix(adjacency_list: defaultdict) -> list:
    """
        convert_adj_list_to_adj_matrix method converts given adjacency list
        to adjacency matrix
    """
    list_len = len(adjacency_list)

    adjacency_matrix = [[0 for _ in range(list_len)] for _ in range(list_len)]
    for i in range(list_len):
        for j in adjacency_list[i]:
            adjacency_matrix[i][j] = 1

    return adjacency_matrix



def convert_adj_list_to_inc_matrix(adjacency_list: defaultdict) -> list:
    """
        convert_adj_list_to_inc_matrix method converts given adjacency list
        to incidence matrix
    """
    edges = 0
    list_len = 0
    for i in adjacency_list:
        list_len += 1
        for _ in adjacency_list[i]:
            edges += 1

    edges = int(edges / 2)
    incidence_matrix = [[0] * edges for _ in range(list_len)]

    current_col = 0
    for first_node in range(list_len):
        for second_node in adjacency_list[first_node]:
            if second_node < first_node:
                continue
            incidence_matrix[first_node][current_col] = 1
            incidence_matrix[second_node][current_col] = 1
            current_col += 1
    return incidence_matrix


def convert_inc_matrix_to_adj_list(incidence_matrix: list) -> OrderedDict:
    """
        convert_inc_matrix_to_adj_list method converts given incidence
        matrix to adjacency list
    """
    adjacency_list = defaultdict(list)
    list_len = len(incidence_matrix)
    for row in range(list_len):
        for col in range(len(incidence_matrix[row])):
            if incidence_matrix[row][col] == 1:
                for row2 in range(row + 1, list_len):
                    if incidence_matrix[row2][col] == 1:
                        adjacency_list[row].append(row2)
                        adjacency_list[row2].append(row)

    return OrderedDict(sorted(adjacency_list.items()))


def convert_graph_seq_to_adj_matrix(graph_sequence: list) -> list:
    """
        convert_graph_seq_to_adj_matrix method uses given
        graphic sequence to generate adjacency matrix
    """
    seq_len = len(graph_sequence)
    adj_matrix = [[0 for j in range(seq_len)] for i in range(seq_len)]
    graph_sequence = list(sorted(graph_sequence, reverse=True))
    od = OrderedDict()
    for i in range(len(graph_sequence)):
        od[i] = graph_sequence[i]
    graph_sequence = od
    while True:
        node, y = graph_sequence.popitem(last=False)
        x = 0
        for key, value in graph_sequence.items():
            if x < y:
                graph_sequence[key] -= 1
                adj_matrix[key][node] = 1
                adj_matrix[node][key] = 1
            x += 1
        graph_sequence = OrderedDict(sorted(graph_sequence.items(), key=lambda kv: kv[1], reverse=True))
        if sum(graph_sequence.values()) == 0:
            break
    return adj_matrix


def convert_adj_matrix_to_graph_seq(adjacency_matrix: list) -> list:
    """
        convert_adj_matrix_to_graph_seq method generates
        graphic sequence based on adjacency matrix
    """
    graph_seq = [0 for _ in range(len(adjacency_matrix))]
    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix[i])):
            if adjacency_matrix[i][j] == 1:
                graph_seq[i] += 1

    graph_seq.sort()
    graph_seq = graph_seq[::-1]
    return graph_seq
