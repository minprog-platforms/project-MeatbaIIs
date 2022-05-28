"""
Author: Leon Schuijtvlot
Studentno.: 14291584
This program tests the rotate function
"""


from rotate import rotate, NonSquareMatrixError
import pytest


def test_evensize():
    matrix = [
    [0, 1],
    [2, 3]
    ]
    expected_matrix = [
    [2, 0],
    [3, 1]
    ]
    assert rotate(matrix) == expected_matrix

def test_unevensize():
    matrix = [
    [0, 1, 2],
    [2, 3, 4],
    [5, 6, 7]
    ]
    expected_matrix = [
    [5, 2, 0],
    [6, 3, 1],
    [7, 4, 2]
    ]
    assert rotate(matrix) == expected_matrix

def test_1x1():
    matrix = [[1]]
    expected_matrix = [[1]]
    assert rotate(matrix) == expected_matrix

def test_empty():
    matrix = [[]]
    expected_matrix = [[]]
    assert rotate(matrix) == expected_matrix

def test_nonsquare():
    matrix = [
    [2, 1]
    ]
    with pytest.raises(NonSquareMatrixError):
        rotate(matrix)

def test_original():
    matrix = [
    [0, 1],
    [2, 3]
    ]
    original_matrix = [
    [0, 1],
    [2, 3]
    ]
    rotate(matrix)
    assert matrix == original_matrix

def test_fourrotations():
    matrix = [
    [0, 1],
    [2, 3]
    ]
    original_matrix = [
    [0, 1],
    [2, 3]
    ]
    for _ in range(4):
        matrix = rotate(matrix)
    assert matrix == original_matrix
