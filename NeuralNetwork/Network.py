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
            delta_biases[-l] = sum(delta.table)
            delta_wights[-l] = delta * Matrix.transpose(activations[-1-1])

        # return the delta
        return delta_wights, delta_biases

    def update(self, delta_wights, delta_biases, learning_rate):
        """
        the function which updates the wights of the network
        :param delta_wights: changing according to the delta
        :type delta_wights: list[Matrix]
        :param delta_biases: changing according to the delta
        :type delta_biases: list[float]
        :param learning_rate: the learning rate, range of 0 - 5 recommended
        :type learning_rate: float
        """
        # TODO update
        # go throw the list and update the wights and the bias in the matching
        # order
        lr = learning_rate / 100
        for i in xrange(len(delta_biases)):
            self.wights[i] = self.wights[i] - delta_wights[i] * lr
            self.biases[i] = self.biases[i] - delta_biases[i] * lr

    def train_batch(self, data, learning_rate):
        """
        the function trains a batch
        :param data: the data to test the unit by
        :type data: tuple(list[float], list[float])
        :param learning_rate: the learning rate, range of 0 - 5 recommended
        :type learning_rate: float
        """
        d_wights = [Matrix(w.rows, w.cols, 0) for w in self.wights]
        d_biases = [0 for b in self.biases]
        # for every part in the batch
        for in_p, out_p in data:
            # call the backpropagation function
            nd_wights, nd_biases = self.backprop_result(in_p, out_p)
            d_wights += nd_wights
            d_biases += nd_biases

        # call the update function
        self.update(d_wights, d_biases, learning_rate)
        pass

    def train_network(self, training_data, epochs ,batch_size, learning_rate,
                      test_data=None):
        """
        the function trains the network according to the training data
        :param training_data: the whole training data
        :type training_data: list[tuple(list[float], list[float])]
        :param epochs: how many time to repeat the process
        :type epochs: int
        :param batch_size: the size of  each training batch
        :type batch_size: int
        :param learning_rate: the learning rate, range of 0 - 5 recommended
        :type learning_rate: float
        :param test_data: the data to evaluate the nn by
        :type test_data: list[tuple(list[float], list[float])]
        """
        if test_data:
            n_test = len(test_data)
        n = len(training_data)
        for i in xrange(epochs):
            # split the training data add send to train batch
            random.shuffle(training_data)
            mini_batches = [training_data[k:k+batch_size]
                            for k in xrange(0, n, batch_size)]
            for batch in mini_batches:
                self.train_batch(batch, learning_rate)
            if test_data:
                print "epoch {}: {}/{}".format(i, self.evaluate_network(
                    test_data), n_test)
            else:
                print "epoch {}".format(i)

    def evaluate_network(self, test_data):
        """
        the function evaluates the network
        :param test_data: the test data
        :return: how many tries were successful
        """
        result = [(x.index(max(self.feed_network(x))), y.index(max(y)))
                  for x, y in test_data]
        return sum(x == y for x, y in result)


if __name__ == '__main__':
    net = Network(2, 1, 2, 2)
    net.initiate_wights()
    out = net.feed_network([1, 0])
    backprop = net.backprop_result([1, 0], [1, 1, 1])
    print net.wights
