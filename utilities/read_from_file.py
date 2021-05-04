from collections import defaultdict


"""
    adjacency_matrix_from_file method reads adjacency matrix from file 
    operated file format is:
    each lines contains one row with values separated by empty spaces
"""
def adjacency_matrix_from_file(file_name: str) -> list:
    matrix = []
    with open(file_name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            new_list = line.split(" ")
            new_list = [int(i) for i in new_list]
            matrix.append(new_list)

    file.close()

    return matrix


"""
    incidence_matrix_from_file method reads incidence matrix from file 
    operated file format is:
    each lines contains one row with values separated by empty spaces
"""
def incidence_matrix_from_file(file_name: str) -> list:
    return adjacency_matrix_from_file(file_name)


"""
    adjacency_list_from_file method reads adjacency list from file 
    operated file format is:
    each lines contains node numbers that have connection with node signed with row number
    values are separated by empyt spaces
    
    example: 
    
    for adjacency list: 
    0: 1, 2
    1: 0, 2
    2: 0, 1
    
    file format:
    1 2
    0 2
    0 1
"""
def adjacency_list_from_file(file_name: str) -> list:
    adj_list = defaultdict(list)
    count = 0
    with open(file_name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            new_list = line.split(" ")
            new_list = [int(i) - 1 for i in new_list]
            adj_list[count] = new_list
            count += 1

    file.close()

    return adj_list

