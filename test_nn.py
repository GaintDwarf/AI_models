from NeuralNetwork import Network
import mnist_opener

training_data, validation_data, test_data = mnist_opener.load_data_wrapper()

nn = Network.Network(783, 10, 30)
nn.train_network(training_data, 30, 10, 3, test_data)
