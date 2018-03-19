import pyNNetwork as net
import mnist_opener
import time


def timer(func):

    def wrapper(*args, **kwargs):
        d = time.time()
        func(*args, **kwargs)
        t = time.time()
        print t - d

    return wrapper


@timer
def gd(nn):
    print 1
    nn.SGradient_descent(tr_in, tr_out, 30, 3, 1, ts_in, ts_out)


if __name__ == '__main__':
    print "started"

    tr_in, tr_out, ts_in, ts_out = mnist_opener.load_data_wrapper()
    nn = net.NNetwork([784, 30, 10])

    gd(nn)
