from utilites import Matrix, sigmoid


class Network(object):
    """
    the neural network class
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
        self.wights = []  # type : list[Matrix]

        # only input and output
        if len(args) == 0:
            self.wights.append(Matrix(output_neurons, input_neurons + 1))
        else:
            prev = input_neurons
            # setup all the hidden layer
            for hidden in args:
                self.wights.append(Matrix(hidden, prev))
                prev = hidden
            # set up the last layer wights
            self.wights.append(Matrix(output_neurons, prev))

    def initiate_wights(self):
        """
        the function initiates all the wights to a random value
        """
        for wight in self.wights:
            wight.init_rand()

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
            # calculate the next layer {Current_i = sum(W_ij * L_i)}
            curr_mat = self.wights[i] * curr_mat
            # sigmoid the outcome
            curr_mat.map(sigmoid)

        # convert to array and return
        return Matrix.mat_to_arr(curr_mat)


if __name__ == '__main__':
    net = Network(2, 1, 3, 3)
    net.initiate_wights()
    out = net.feed_network([1, 0])
    print net.wights
