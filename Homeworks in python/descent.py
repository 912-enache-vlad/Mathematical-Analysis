import matplotlib.pyplot as plt
import numpy as np
from math import sin
from math import cos

ok = True
while ok:
    simple = True
    opt = input("""
    Press x to stop
    Choose from 1 to 4 an option: """)

    if opt == '1':
        (x0, eta, n) = (10, 0.1, 20)
    elif opt == '2':
        (x0, eta, n) = (10, 0.33, 50)

    elif opt == '3':
        x0 = 1.5
        eta = 0.47
        n = 7
    elif opt == '4':
        simple = False
        eta = 0.02
        n = 50
    elif opt == 'x':
        ok = False

    if ok:
        if simple:
            x = np.linspace(0.05, 10, 500)
            y = x**2 + 1/x
            a = []
            b = [x0]
            for i in range(n - 1):
                b.append(b[-1] - eta * (2 * b[-1] - 1 / b[-1] ** 2))
            for i in range(n):
                a.append(b[i] ** 2 + 1 / b[i])
        else:  # for option (d)
            # 3000 linearly spaced numbers
            x = np.linspace(-15, 15, 3000)

            # the other function
            y = []
            for i in range(len(x)):
                y.append(x[i] * sin(x[i]))

            # constructing the sequences
            a = []
            b = [13]
            a1 = []
            b1 = [3]

            for i in range(n - 1):
                b.append(b[-1] - eta * ( sin( b[-1] ) + b[-1]*cos( b[-1] ) ))
                b1.append(b1[-1] - eta * (sin(b1[-1]) + b1[-1] * cos(b1[-1])))

            for i in range(n):
                a.append(b[i] * sin(b[i]))
                a1.append(b1[i] * sin(b1[i]))


        # setting the axes at the centre
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        # adding some info to the graph
        if simple:
            plt.title('f(x) = 1/x + x,   x0 = ' + str(x0) + ',   eta = ' + str(eta) + ',   n = ' + str(n))
        else:
            plt.title('f(x) = x * sin(x),   x0 = 13  or  x0 = 3,   eta = ' + str(eta) + ',   n = ' + str(n))

        # plot the function
        plt.plot(x,y, 'r')
        plt.plot(b, a, marker='o', markerfacecolor='green', markersize=5)
        if not simple:
            plt.plot(b1, a1, marker='o', markerfacecolor='green', markersize=5)

        # show the plot
        plt.show()