__author__ = "Segev Gershon"
__date__ = "5/1/2017"
__version__ = "1"

import random
import math


class Matrix(object):
    """
    matrix object which handles the matrices
    :type rows: int
    :type cols: int
    :type table: list[int]
    """

    def __init__(self, rows=0, cols=0, value=None):
        super(Matrix, self).__init__()
        self.rows = rows
        self.cols = cols
        self.table = [[value for j in xrange(cols)] for i in xrange(rows)]

    def __getitem__(self, item):
        """
        :param item: index
        :return: list
        :rtype: list
        """
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
            nmt.set_matrix([[self[i][j] * other for j in xrange(
                self.cols)] for i in xrange(self.rows)])
        return nmt

    def get_print(self):
        mat = ""
        row_format = "{:>5} |" * (self.cols + 1)
        mat += row_format.format("", *range(0, self.cols)) + "\n"
        mat += len(row_format) * "-" + "\n"
        for index, row in zip(range(0, self.rows), self.table):
            mat += row_format.format(index, *row) + "\n"
            mat += len(row_format) * "-" + "\n"
        return mat

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
        :rtype: Matrix
        """
        table = [[arr[i]] for i in xrange(len(arr))]
        mat = Matrix()
        mat.set_matrix(table)
        return mat

    @staticmethod
    def mat_to_arr(mat):
        """
        the function transfer an array to a matrix
        like a matrix as [[1, 4], [2, 5], [3, 6]] changes to [1, 2, 3, 4, 5, 6]
        [1, 2, 3
         4, 5, 6]
        :param mat: the array to convert
        :type mat: Matrix
        :return: new matrix Matrix
        :rtype: list
        """
        return [mat[i][j] for i in xrange(mat.rows) for j in xrange(mat.cols)]

    @staticmethod
    def transpose(mat):
        """
        the function returns a rotated matrix of the send matrix
        :param mat: the matrix to rotate
        :type mat: Matrix
        :return: rotated matrix
        :rtype: Matrix
        """
        new = Matrix(mat.cols, mat.rows)
        new.set_matrix([[mat[j][i] for j in xrange(mat.rows)] for i in
                        xrange(mat.cols)])
        return new

    @staticmethod
    def hadamard(mat1, mat2):
        """
        calculates the hadamard product of two matrices
        :param mat1: first matrix
        :type mat1: Matrix
        :param mat2: second matrix
        :type mat2: Matrix
        :return: the hadamard product
        :rtype: Matrix
        """
        if (mat1.cols != mat2.cols) or (mat1.rows != mat2.rows):
            raise Exception("Matrices must have the same dimensions")
        new = Matrix(mat1.rows, mat1.cols)
        new.set_matrix([[mat1[i][j] * mat2[i][j] for j in xrange(mat1.cols)]
                        for i in xrange(mat1.rows)])
        return new


def mean(vec):
    """
    the function finds the mean of a given vector
    :param vec: the vector to find the mean in
    :type vec: list
    :return: the mean of the given vector
    :rtype: float
    """
    return sum(vec)/float(len(vec))


def sigmoid(x):
    """
    the function does the sigmoid function the input
    :param x: the number to operate on
    :type x: float
    :return: the sigmoid of the given number
    :rtype: float
    """
    return 1 / (1 + math.exp(-x))


def sigmoid_derivative(x):
    """
    the function calculates the derivative of the sent x in the sigmoid function
    :param x: the x to calculate on
    :type x: float
    :return: the sigmoid derivative
    :rtype: float
    """
    sig = sigmoid(x)
    return sig * (1 - sig)


if __name__ == '__main__':
    mt1 = Matrix()
    mt1.set_matrix([[1, 2, 3],
                    [4, 5, 6]])
    mt2 = Matrix.arr_to_mat([1, 2, 3])
    mt3 = mt1 * mt2
    print mt1
    print Matrix.transpose(mt1)
    print mt2
    print mt3
    print Matrix.mat_to_arr(mt1)

    # printing in same line example
    import time

    for i in xrange(0, 101, 1):
        print "\r>> You have finished %d%%" % i,
        time.sleep(0.01)

    print "\rDone"
