import prettytable
from prettytable import PrettyTable
import numpy as np


def format_float(num):
    return np.format_float_positional(num, precision=20)


def get_nth_iteration_convex(n, x1, learning_rate):
    a = x1
    for i in range(n):
        b = a - learning_rate * 2 * a
        a = b

    return a


def get_nth_iteration_concave(n, x1, learning_rate):
    # f(x) = x * sin(x), f'(x) = sin(x) + x*cos(x)
    a = x1
    for i in range(n):
        b = a - learning_rate * 2 * a
        a = b

    return a


def solution_a(x1, learning_rate, iteration_step):
    """
    f(x) = x^2, f'(x) = 2x
    :param x1: first term
    :param learning_rate: positive real number
    :return: table showing the iterations
    """

    table = PrettyTable(["Iteration", "Value"])
    table.title = "Problem a: " + "x1 = " + str(x1) + ", learning rate = " + str(format_float(learning_rate))
    table.hrules = prettytable.ALL

    for item in iteration_step:
        table.add_row([str(item), format_float(get_nth_iteration_convex(item, x1, learning_rate))])

    return table


def solution_b(x1, learning_rate, iteration_step):
    """
    f(x) = x^2, f'(x) = 2x
    :param x1: first term
    :param learning_rate: positive real number
    :return: table showing the iterations
    """

    table = PrettyTable(["Iteration", "Value"])
    table.title = "Problem b: " "x1 = " + str(x1) + ", learning rate = " + str(format_float(learning_rate))
    table.hrules = prettytable.ALL

    for item in iteration_step:
        table.add_row([str(item), format_float(get_nth_iteration_convex(item, x1, learning_rate))])

    return table


def solution_c(x1, learning_rate, iteration_step):
    """
    f(x) = x^2, f'(x) = 2x
    :param x1: first term
    :param learning_rate: positive real number
    :return: table showing the iterations
    """

    table = PrettyTable(["Iteration", "Value"])
    table.title = "Problem c: " + "x1 = " + str(x1) + ", learning rate = " + str(format_float(learning_rate))
    table.hrules = prettytable.ALL

    for item in iteration_step:
        table.add_row([str(item), format_float(get_nth_iteration_convex(item, x1, learning_rate))])

    return table


def solution_d(x1, learning_rate, iteration_step):
    """
    f(x) = x^2, f'(x) = 2x
    :param x1: first term
    :param learning_rate: positive real number
    :return: table showing the iterations
    """

    table = PrettyTable(["Iteration", "Value"])
    table.title = "Problem d: " + "x1 = " + str(x1) + ", learning rate = " + str(format_float(learning_rate))
    table.hrules = prettytable.ALL

    for item in iteration_step:
        table.add_row([str(item), format_float(get_nth_iteration_concave(item, x1, learning_rate))])

    return table


iteration_step_a = [1000, 2000, 5000, 10000, 50000, 100000, 200000, 500000]
iteration_step_b = [1, 2, 5, 10, 20, 30, 40, 50]
iteration_step_c = [1, 2, 5, 10, 15, 20, 25, 30]

print(solution_a(2, 0.00001, iteration_step_a))

print("\n\n")
print(solution_b(100, 0.1, iteration_step_b))

print("\n\n")
print(solution_c(2, 2, iteration_step_c))

print("\n\n")
print(solution_d(2, 0.00001, iteration_step_a))