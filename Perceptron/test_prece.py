import pygame
import random
from testUnits import TestUnit1
from perceptron import Perceptron

HEIGHT = 600
WIDTH = 600


def f(x):
    return 1.25*x


def func(x, y):
    return 1 if y > f(x) else -1


def activation_func(x):
    if x > 0:
        return 1
    return -1


def generate_test_units(n, min_val, max_val):
    lst = []
    for i in xrange(n):
        lst.append(TestUnit1(min_val, max_val, func, f))
    return lst


def draw_unit(canvas, X, Y, Res, target):
    if Res == target:
        pygame.draw.circle(canvas, (0, 255, 0), (X, Y), 2)
    else:
        pygame.draw.circle(canvas, (255, 0, 0), (X, Y), 2)


def main():
    end = False
    units = generate_test_units(200, 0, HEIGHT)
    percept = Perceptron(len(units[0].get_neurons()), 0.1)

    percept.test_bunch(units, activation_func)

    pygame.init()
    canvas = pygame.display.set_mode((WIDTH, HEIGHT))
    canvas.fill((255, 255, 255))

    pygame.display.set_caption("X = Y")
    pygame.draw.line(canvas, (0, 0, 0), (0, f(0)), (WIDTH, f(WIDTH)))

    clock = pygame.time.Clock()
    for unit in units:
        unit.draw_unit(canvas)
        X = random.randrange(0, WIDTH)
        Y = random.randrange(0, HEIGHT)
        bias = 1

        draw_unit(canvas, X, Y, percept.guess((X, Y, bias), activation_func),
                  activation_func(func(X, Y)))

    while not end:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                end = True
        clock.tick(10000000)
    pygame.quit()


if __name__ == '__main__':
    main()


