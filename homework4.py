import matplotlib.pyplot as plt
import numpy as np

def the_normal_sum(n:int):

    ax = plt.subplot()
    y = [((-1) ** (i + 1) / i) for i in range(1, n)]                #creating the terms from (xn)
    sumy = [0, ]
    for i in range(0, n-1):
        sumy.append(sumy[i] + y[i])                                 #creating the sum with the terms from (xn)
    ax.plot(sumy, marker = ".", linestyle = "--", color = "r")
    ax.grid(True)                                                   #for the grid lines
    ax.set_title("The sum with the normal arrangement, which tends to ln2")
    plt.show()

def the_new_sum(n:int):
    import matplotlib.pyplot as plt

    ax = plt.subplot()
    y = [((-1) ** (i + 1) / i) for i in range(1, 10 * n)]  # creating the terms from (xn)
    sumy = [0]
    j = 1
    for i in range(0, n, 2):  # creating a new sum by rearranging the elements of the sum
        sumy.append(sumy[j - 1] + y[i])
        j += 1
        sumy.append(sumy[j - 1] + y[(i + 1) * 2 - 1])
        j += 1
        sumy.append(sumy[j - 1] + y[(i + 1) * 2 + 1])
        j += 1

    ax.plot(sumy, marker=".", linestyle="--", color="r")
    ax.grid(True)
    ax.set_title("The new sum with a different arrangement of the elements, which tends to 1/2 * ln2", fontsize=10)
    # ax.titlesize : small
    plt.show()

n = int(input("Enter a number:"))
the_normal_sum(n)
the_new_sum(n)