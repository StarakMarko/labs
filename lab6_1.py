matrix_ = [
    [31, 65, -83, -2, -85],
    [9, -2, 11, -4, 70],
    [52, 73, -8, -1, 60],
    [57, 83, -1, 82, 50],
    [1, -3, -2, 78, -9],
]


def sort_decorator(func):
    def wrapper(self):
        new_matrix = self.insertion_sort()
        self.matrix = new_matrix
        return func(self)

    return wrapper


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def insertion_sort(self):
        """
        function for insertion sort
        """

        new_matrix = [row[:] for row in self.matrix]
        for row in new_matrix:
            for i in range(1, len(row)):
                x = row[i]
                j = i - 1
                while x < row[j] and j >= 0:
                    row[j + 1] = row[j]
                    j -= 1
                row[j + 1] = x
        return new_matrix

    @sort_decorator
    def sum_above_diagonal(self):
        """
        function for finding the sum of elements above the diagonal
        """
        all_sum = []
        for i, row in enumerate(self.matrix):
            sum_ = 0
            for j, value in enumerate(row):
                if j > i:
                    sum_ += value
            all_sum.append(sum_)
        return all_sum

    def geometric_mean(self):
        """
        function for finding the geometric mean
        """
        sums = self.sum_above_diagonal()
        number = 0
        product = 1
        for sum_ in sums:
            if sum_ != 0:
                number += 1
                product = product * abs(sum_)
        return product ** (1 / number)

    def __add__(self, other):
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[i])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)
        return Matrix(result)

    def __str__(self):
        for row in self.matrix:
            print(row)
        return ""


matrix_1 = Matrix(matrix_)
print(matrix_1)
matrix_2 = matrix_1 + matrix_1
print(matrix_2)
print(matrix_1.sum_above_diagonal())
print(matrix_1.geometric_mean())
