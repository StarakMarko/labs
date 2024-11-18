"""
№23 This module contains functions for matrix operations
"""

matrix_ = [
    [31, 65, -83, -2, -85],
    [9, -2, 11, -4, 70],
    [52, 73, -8, -1, 60],
    [57, 83, -1, 82, 50],
    [1, -3, -2, 78, -9],
]


def insertion_sort(matrix):
    """
    function for insertion sort
    """

    new_matrix = [row[:] for row in matrix]
    for row in new_matrix:
        for i in range(1, len(row)):
            x = row[i]
            j = i - 1
            while x < row[j] and j >= 0:
                row[j + 1] = row[j]
                j -= 1
            row[j + 1] = x
    return new_matrix


def sum_above_diagonal(matrix):
    """
    function for finding the sum of elements above the diagonal
    """
    all_sum = []
    for i, row in enumerate(matrix):
        sum_ = 0
        for j, value in enumerate(row):
            if j > i:
                sum_ += value
        all_sum.append(sum_)
    return all_sum


def geometric_mean(matrix):
    """
    function for finding the geometric mean
    """
    sums = sum_above_diagonal(matrix)
    number = 0
    product = 1
    for sum_ in sums:
        if sum_ > 0:
            number += 1
            product = product * sum_
    return product ** (1 / number)


print(insertion_sort(matrix_))
print(sum_above_diagonal(matrix_))
print(geometric_mean(matrix_))
print(matrix_)
