import cPickle
import gzip

# Third-party library As
import numpy as np


def load_data():
    f = gzip.open('mnist.pkl.gz', 'rb')
    training_data, validation_data, test_data = cPickle.load(f)
    f.close()
    return training_data, validation_data, test_data


def load_data_wrapper():
    tr_d, va_d, te_d = load_data()
    training_inputs = [np.reshape(x, (784, 1)).tolist() for x in tr_d[0]]
    training_inputs = [[j[0] for j in i] for i in training_inputs]
    training_results = [vectorized_result(y) for y in tr_d[1]]
    test_inputs = [np.reshape(x, (784, 1)).tolist() for x in te_d[0]]
    test_inputs = [[j[0] for j in i] for i in test_inputs]
    test_data = [vectorized_result(y) for y in te_d[1]]
    return training_inputs, training_results, test_inputs, test_data


def vectorized_result(j):
    e = [0 for i in range(10)]
    e[j] = 1.0
    return e