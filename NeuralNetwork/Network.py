from utilites import Matrix, sigmoid, sigmoid_derivative
import random


class Network(object):
    """
    the neural network class
    :type wights: list[Matrix]
    :type biases: list[float]
    """

    def __init__(self, input_neurons, output_neurons, *args):
        """
        the initiate function
        :param input_neurons: how many input neurons there are
        :type input_neurons: int
        :param output_neurons: how many output input there are
        :type output_neurons: int
        :param args: how many hidden layers and there sizes
        """
        # TODO solve bias
        super(Network, self).__init__()
        self.wights = []
        self.biases = []

        # only input and output
        if len(args) == 0:
            self.wights.append(Matrix(output_neurons, input_neurons + 1))
            self.biases.append(1)
        else:
            prev = input_neurons
            # setup all the hidden layer
            for hidden in args:
                self.wights.append(Matrix(hidden, prev))
                self.biases.append(1)
                prev = hidden
            # set up the last layer wights
            self.wights.append(Matrix(output_neurons, prev))
            self.biases.append(1)

    def initiate_wights(self):
        """
        the function initiates all the wights to a random value
        """
        for i in xrange(len(self.wights)):
            self.wights[i].init_rand()
            self.biases[i] = random.random()

    def feed_network(self, inputs):
        """
        the function get input to feed the neural network
        :param inputs: the inputs to feed the net
        :type inputs: list[float]
        :return: a list of the the last output layer
        :rtype: list[flout]
        """
        # check the inputs match
        if len(inputs) != self.wights[0].cols:
            raise Exception("the sizes of the inputs ant the created network "
                            "don't match")
        # copy to the input layer
        curr_mat = Matrix.arr_to_mat(inputs)

        # for all the layers
        for i in xrange(len(self.wights)):
            # calculate the next layer {Current_i = sum(W_ij * L_i) + b_i}
            curr_mat = self.wights[i] * curr_mat + self.biases[i]
            # sigmoid the outcome
            curr_mat.map(sigmoid)

        # convert to array and return
        return Matrix.mat_to_arr(curr_mat)

    @staticmethod
    def calculate_cost(actual_result, expected):
        """
        the function calculates the cost of the result
        :param actual_result: the final result from the run
        :type actual_result: list[float]
        :param expected: the expected result
        :type expected: list[float]
        :return: a list of the cost
        """
        return [(y - x) for x, y in zip(actual_result, expected)]

    @staticmethod
    def cost_derivative(actual_result, expected):
        """
        the function calculates the cost derivative
        :param actual_result: the final result from the run
        :type actual_result: Matrix
        :param expected: the expected result
        :type expected: Matrix
        :return: the cost derivative
        :rtype: Matrix
        """
        return actual_result - expected

    def backprop_result(self, x, y):
        """
        the function calculates the delta of the results according to the data
        :param x: the input to the network
        :type x: list[float]
        :param y: the out put of the network
        :type y: list[float]
        :return: the delta to change the wights and biases
        :rtype: tuple(list[Matrix], list[Matrix])
        """
        # TODO backprop result
        # create delta wights and bias
        delta_wights = [None for w in self.wights]
        """ :type : list[Matrix]"""
        delta_biases = [None for b in self.biases]
        """ :type : list[Matrix]"""
        # create an layers temp array
        z_vectors = []
        """ :type : list[Matrix]"""
        # feed foreword and save results in the layers array

        # copy to the input layer
        activation = Matrix.arr_to_mat(x)
        activations = [activation]

        # for all the layers
        for i in xrange(len(self.wights)):
            # calculate the next layer {Current_i = sum(W_ij * L_i) + b_i}
            z_vectors.append(self.wights[i] * activation + self.biases[i])
            activation = z_vectors[-1]
            # sigmoid the outcome
            activation.map(sigmoid)
            activations.append(activation)

        # backwards pass through the layers to calculate the errors and the
        delta = self.cost_derivative(activation, Matrix.arr_to_mat(y))
        z_vectors[-1].map(sigmoid_derivative)
        delta = Matrix.hadamard(delta, z_vectors[-1])

        delta_biases[-1] = delta
        delta_wights[-1] = delta * Matrix.transpose(activations[-2])

        #  changes to the array when each fixed layer functions as the output of
        #  the next layer
        for l in xrange(2, len(self.wights) + 1):
            z = z_vectors[-l]
            z.map(sigmoid_derivative)
            delta = Matrix.transpose(self.wights[-l+1]) * delta
            delta = Matrix.hadamard(delta, z)
            delta_biases[-l] = delta
            delta_wights[-l] = delta * Matrix.transpose(activations[-1-1])

        # return the delta
        return delta_wights, delta_biases

    def update(self, delta, learning_rate):
        """
        the function which updates the wights of the network
        :param delta: changing according to the delta
        :type delta: list[Matrix]
        :param learning_rate: the learning rate, range of 0 - 5 recommended
        :type learning_rate: float
        """
        # TODO update
        # go throw the list and update the wights and the bias in the matching
        # order
        pass

    def train_batch(self, data, learning_rate):
        """
        the function trains a batch
        :param data: the data to test the unit by
        :type data: tuple(list[float], list[float])
        :param learning_rate: the learning rate, range of 0 - 5 recommended
        :type learning_rate: float
        """
        # TODO train batch
        # for every part in the batch
        #   call the backpropagation function
        #   average the results
        # call the update function
        pass

    def train_network(self, training_data, batch_size, learning_rate):
        """
        the function trains the network according to the training data
        :param training_data: the whole training data
        :type training_data: list[tuple(list[float], list[float])]
        :param batch_size: the size of  each training batch
        :type batch_size: int
        :param learning_rate: the learning rate, range of 0 - 5 recommended
        :type learning_rate: float
        """
        # TODO train network
        # split the training data add send to train batch
        pass


if __name__ == '__main__':
    net = Network(2, 3, 2, 2)
    net.initiate_wights()
    out = net.feed_network([1, 0])
    backprop = net.backprop_result([1, 0], [1, 1, 1])
    print net.wights
