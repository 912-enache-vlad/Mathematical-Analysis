import numpy as np
import matplotlib.pyplot as plt

def grad_f(x, y, b):
    # Compute the gradient of f at (x, y)
    grad_x = x
    grad_y = b * y
    return grad_x, grad_y

def f(x, y, b):
    # Compute the value of f at (x, y)
    return 0.5 * (x**2 + b * y**2)

def gradient_descent(x0, y0, b, step_size, num_iterations):
    # Perform gradient descent to minimize f
    x, y = x0, y0
    x_vals, y_vals = [x], [y]
    for i in range(num_iterations):
        grad_x, grad_y = grad_f(x, y, b)
        x -= step_size * grad_x
        y -= step_size * grad_y
        x_vals.append(x)
        y_vals.append(y)
    return x_vals, y_vals

def plot_gradient_descent(b):
    # Plot the function and the gradient descent iterations
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y, b)

    x0, y0 = (5, 5)
    step_size = 0.1
    num_iterations = 10
    x_vals, y_vals = gradient_descent(x0, y0, b, step_size, num_iterations)

    plt.contour(X, Y, Z, levels=np.logspace(-1, 3, 10))
    plt.plot(x_vals, y_vals, '-o')
    plt.title(f'b = {b}')
    plt.show()

# Plot gradient descent iterations for different values of b
plot_gradient_descent(1)
plot_gradient_descent(1/2)
plot_gradient_descent(1/5)
plot_gradient_descent(1/10)
