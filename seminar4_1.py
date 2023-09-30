

def print_matrix(input_matrix: [[int]]) -> None:
    for i in range(len(input_matrix)):
        for j in range(len(input_matrix[0])):
            print(input_matrix[i][j], end='\t')
        print()
    print()


def transpose_matrix(input_matrix: [[int]]) -> [[int]]:
    new_matrix = [[0] * len(input_matrix) for _ in range(len(input_matrix[0]))]
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[0])):
            new_matrix[i][j] = input_matrix[j][i]
    return new_matrix


my_array = ([11, 12, 13], [24, 25, 26])
print_matrix(my_array)
print_matrix(transpose_matrix(my_array))
