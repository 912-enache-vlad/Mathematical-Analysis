import numpy

def f(x:int):
    return numpy.e**(-x**2)


a = 10
n = 1000000
xk = -a
sum = a / n * f(xk)         # the first element of the sum
xk = xk + 2 * a / n

while xk < a:               # calculating the sum by adding to it the intermediary elements
    sum += 2 * a / n * f(xk)
    xk = xk + 2 * a / n

sum += 2 * a / n * f(a)         # the last element of the sum

print(sum)