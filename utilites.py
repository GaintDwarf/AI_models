__author__ = "Segev Gershon"
__date__ = "5/1/2017"
__version__ = "1"

import random


class Matrix(object):
    """
    matrix object which handles the matrix
    """

    def __init__(self, rows=0, cols=0):
        super(Matrix, self).__init__()
        self.rows = rows
        self.cols = cols
        self.table = [[None for j in xrange(cols)] for i in xrange(rows)]

    def __getitem__(self, item):
        return self.table[item]

    def __add__(self, other):
        nmt = Matrix(self.rows, self.cols)
        if isinstance(other, Matrix):
            # by another matrix
            if other.rows != self.rows or other.cols != self.cols:
                raise Exception("matrix must be in the same size")
            else:
                nmt.set_matrix([[self[i][j] + other[i][j] for j in xrange(
                    self.cols)] for i in xrange(self.rows)])
        else:
            # by scalars
            nmt.set_matrix([[self[i][j] + other for j in xrange(self.cols)]
                            for i in xrange(self.rows)])
        return nmt

    def __sub__(self, other):
        nmt = Matrix(self.rows, self.cols)
        if isinstance(other, Matrix):
            # by another matrix
            if other.rows != self.rows or other.cols != self.cols:
                raise Exception("matrix must be in the same size")
            else:
                nmt.set_matrix([[self[i][j] - other[i][j] for j in xrange(
                    self.cols)] for i in xrange(self.rows)])
        else:
            # by scalar
            nmt.set_matrix([[self[i][j] - other for j in xrange(self.cols)]
                            for i in xrange(self.rows)])
        return nmt

    def __mul__(self, other):
        nmt = Matrix(self.rows, self.cols)
        if isinstance(other, Matrix):
            if other.rows != self.cols:
                raise Exception("matrix must be perpendicular")
            else:
                # by another matrix
                nmt = Matrix(self.rows, other.cols)
                for other_col in xrange(other.cols):
                    for row in xrange(self.rows):
                        summ = 0
                        for index in xrange(self.cols):
                            summ += self[row][index] * other[index][other_col]
                        nmt[row][other_col] = summ
        else:
            # by scalar
            nmt.set_matrix([[self.table[i][j] * other for j in xrange(
                self.cols)] for i in xrange(self.rows)])
        return nmt

    def init_rand(self):
        """
        the function initializes random numbers in all the matrix
        the numbers are between 0 and 1
        """
        self.table = [[random.random() for j in xrange(self.cols)]
                      for i in xrange(self.rows)]

    def set_matrix(self, table):
        """
        the function sets the matrix according to the sent matrix
        :param table: the table to set in the matrix
        :type table: list[list[flout]]
        """
        self.table = table
        self.rows = len(table)
        self.cols = len(table[0])

    def __repr__(self):
        mat = ""
        row_format = "{:>5} |" * (self.cols + 1)
        mat += row_format.format("", *range(0, self.cols)) + "\n"
        mat += len(row_format) * "-" + "\n"
        for index, row in zip(range(0, self.rows), self.table):
            mat += row_format.format(index, *row) + "\n"
            mat += len(row_format) * "-" + "\n"
        return mat

    def map(self, func):
        """
        the function maps all the units in the matrix
        :param func: the function to use
        :type func: function(float)
        """
        self.table = [[func(self[i][j]) for j in xrange(self.cols)]
                      for i in xrange(self.rows)]

    @staticmethod
    def arr_to_mat(arr):
        """
        the function transfer an array to a matrix
        like [1, 2, 3] changes to a matrix as [[1], [2], [3]]
        :param arr: the array to convert
        :type arr: list
        :return: new matrix Matrix
        :rtype:Matrix
        """
        table = [[arr[i]] for i in xrange(len(arr))]
        mat = Matrix()
        mat.set_matrix(table)
        return mat


def mean(vec):
    """
    the function finds the mean of a given vector
    :param vec: the vector to find the mean in
    :type vec: list
    :return: the mean of the given vector
    :rtype: float
    """
    return sum(vec)/float(len(vec))


if __name__ == '__main__':
    mt1 = Matrix()
    mt1.set_matrix([[1, 2, 3],
                    [4, 5, 6]])
    mt2 = Matrix.arr_to_mat([1, 2, 3])
    mt3 = mt1 * mt2

    print mt1
    print mt2
    print mt3
