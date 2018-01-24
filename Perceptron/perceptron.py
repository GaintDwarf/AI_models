import random
import pygame
from testUnits import TestUnit1


class Perceptron(object):

    def __init__(self, n, lr):
        """
        building function of a single perceptron
        :param n: the list size of the weights array
        :param lr: the learning rate
        """
        super(Perceptron, self).__init__()
        self.weights = [random.random() for i in xrange(n)]
        self.length = n
        self.lr = lr

    def __len__(self):
        return self.length

    def calculate_sum(self, neurons):
        """
        the function calculates the sum of all products of the connected
        neurons and the matching weight, must be matching.
        :param neurons: the neurons of the previous layer.
        :type neurons: list
        :return: the sum of the products
        """
        if self.length != len(neurons):
            return None
        return sum([neurons[i] * self.weights[i] for i in xrange(len(neurons))])

    def guess(self, neurons, activation_func):
        """
        the function return a guess for an outcome
        :param neurons: the input neurons
        :type neurons: list
        :param activation_func: the activation function for the result
        :type activation_func: function(list)
        :return: an estimation
        :rtype: float
        """
        return activation_func(self.calculate_sum(neurons))

    def test(self, neurons, target_result, activation_func):
        """
        the function fixes all the weights according to the test
        :param neurons: the input neurons
        :type neurons: list
        :param target_result: the targeted result of the neurons input
        :type target_result: float
        :param activation_func: the activation function for the result
        :type activation_func: function(list)
        :return: None
        """
        res = self.guess(neurons, activation_func)

        if res != target_result:
            error = target_result - res

            for i in xrange(len(self.weights)):
                self.weights[i] += neurons[i] * error * self.lr

    def test_bunch(self, units, activation_func):
        """
        the function test a bunch of test units
        :param units: the test units to test
        :type units: list
        :param activation_func: the activation function
        :type activation_func: function(flout)
        :return: Unit
        """
        for current_unit in units:
            self.test(current_unit.get_neurons(),
                      current_unit.target_result,
                      activation_func)

