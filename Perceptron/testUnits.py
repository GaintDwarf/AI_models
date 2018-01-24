import random
import pygame


class TestUnit1(object):

    def __init__(self, min_val, max_val, func, f):
        """
        the building function of test units
        :param min_val: the minimum value of the random generator
        :param max_val: the maximum value of the random generator
        :param func: the activation function of the unit
        """
        super(TestUnit1, self).__init__()
        self.X = random.randrange(min_val, max_val)
        self.Y = random.randrange(min_val, max_val)
        self.bias = 1

        self.target_result = func(self.X, self.Y)

        self.f_of_x = f

    def get_neurons(self):
        return [self.X, self.Y, self.bias]

    def draw_unit(self, canvas):
        if self.f_of_x(self.X) > self.Y:
            pygame.draw.circle(canvas, (0, 0, 0), (self.X, self.Y), 5)
        else:
            pygame.draw.circle(canvas, (0, 0, 0), (self.X, self.Y), 5, 1)

