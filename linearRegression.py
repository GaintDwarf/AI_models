import matplotlib.pyplot as plt
import utilites

__author__ = "Segev Gershon"
__date__ = "5/1/2017"
__version__ = "1"


class LinearGraph(object):

    def __init__(self, y_cross=0, slope=1):
        super(LinearGraph, self).__init__()
        self.y_cross = y_cross
        self.slope = slope

    def get_value(self, x):
        """
        the function returns the y value of the given x
        :param x: the x value to search
        :type x: float
        :return: the y value
        :rtype: float
        """
        return self.slope * x + self.y_cross

    def get_values(self, x):
        """
        the function returns the y value of the given x
        :param x: the x value to search
        :type x: list
        :return: the y value
        :rtype: list
        """
        return [(self.slope * val + self.y_cross) for val in x]

    def find_slope(self, x_values, y_values, set_graph=True):
        """
        the function return the slope of a function (m in y = mx + b)
        :param x_values: the x values
        :type x_values: list
        :param y_values: the y values
        :type y_values: list
        :param set_graph: whether or not to save the result in the object
        :type set_graph: bool
        :return: the slope of a function
        :rtype: float
        """
        if len(x_values) != len(y_values):
            print "the length of the given values don't match"
        else:
            x_mean = utilites.mean(x_values)
            y_mean = utilites.mean(y_values)
            numerator = sum([((x_values[i] - x_mean)*(y_values[i] - y_mean))for i in
                            xrange(len(x_values))])
            denominator = sum([((val - x_mean)**2) for val in x_values])
            if denominator == 0:
                print "the slope can't be calculated"
            else:
                if set_graph:
                    self.slope = float(numerator)/denominator
                    return self.slope
                else:
                    return float(numerator)/denominator
        return None

    def find_y_cross(self, x_values, y_values, slope=1, set_graph=True):
        """
        the function calculates the y cross of the function (b in y = mx + b)
        :param x_values: the x values
        :type x_values: list
        :param y_values: the y values
        :type y_values: list
        :param slope: the slope of the function
        :type slope: float
        :param set_graph: whether or not to save the result in the object
        :type set_graph: bool
        :return: the y cross of the function
        :rtype: float
        """
        if slope == 1:
            slope = self.slope
        if len(x_values) != len(y_values):
            print "the length of the given values don't match"
        else:
            x_mean = utilites.mean(x_values)
            y_mean = utilites.mean(y_values)
            if set_graph:
                self.y_cross = y_mean - x_mean * slope
                return self.y_cross
            else:
                return y_mean - x_mean * slope
        return None

    def print_graph_function(self):
        print "y = {m}x + {b}".format(m=self.slope, b=self.y_cross)

    def set_graph(self, max_x=10):
        """
        the function prints the graph
        :param max_x: the maximum x value
        :type max_x: int
        :return: Nothing
        """
        x = range(max_x)
        y = self.get_values(x)
        plt.plot(x, y)


def main():
    y_vals = [5, 3, 9, 17, 13]
    x_vals = [1, 2, 3, 4, 5]

    plt.scatter(x_vals, y_vals, c='red')

    graph = LinearGraph()
    graph.find_slope(x_vals, y_vals)
    graph.find_y_cross(x_vals, y_vals)

    graph.print_graph_function()

    print "the prediction for x = 100 is {}".format(graph.get_value(100))
    graph.set_graph()

    plt.show()


if __name__ == '__main__':
    main()
