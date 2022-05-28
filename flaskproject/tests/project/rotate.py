"""
Author: Leon Schuijtvlot
Studentno.: 14291584
This program rotates a matrix
"""

class NonSquareMatrixError(Exception):
    pass

def rotate(matrix:list[list[int]]):
    for row in matrix:
        if not row:
            return [[]]

        if len(row) != len(matrix):
            raise NonSquareMatrixError

    new_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    for row in new_matrix:
        row.reverse()

    return new_matrix

def print_matrix(matrix:list[list[int]]):
    for row in matrix:
        print(row)
    print()

if __name__ == "__main__":


    matrix = [
    [0, 1],
    [2, 3]
    ]

    matrix = [
    [ 5, 1, 9,11],
    [ 2, 4, 8,10],
    [13, 3, 6, 7],
    [15,14,12,16]
    ]

    rotated_matrix = rotate([[]])
    print_matrix(matrix)
    # prints
    # [0, 1]
    # [2, 3]

    print_matrix(rotated_matrix)
    # prints
    # [2, 0]
    # [3, 1]