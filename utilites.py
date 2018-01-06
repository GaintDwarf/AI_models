__author__ = "Segev Gershon"
__date__ = "5/1/2017"
__version__ = "1"


def mean(vec):
    """
    the function finds the mean of a given vector
    :param vec: the vector to find the mean in
    :type vec: list
    :return: th mean of the given vector
    :rtype: float
    """
    return sum(vec)/float(len(vec))
