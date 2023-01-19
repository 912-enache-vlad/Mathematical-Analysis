import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

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
    x_vals, y_vals, z_vals = [x], [y], [f(x, y, b)]
    for i in range(num_iterations):
        grad_x, grad_y = grad_f(x, y, b)
        x -= step_size * grad_x
        y -= step_size * grad_y
        x_vals.append(x)
        y_vals.append(y)
        z_vals.append(f(x, y, b))
    return x_vals, y_vals, z_vals

def plot_gradient_descent_3d(b):
    # Plot the function and the gradient descent iterations in 3D
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y, b)

    x0, y0 = (5, 5)
    step_size = 0.1
    num_iterations = 10
    x_vals, y_vals, z_vals = gradient_descent(x0, y0, b, step_size, num_iterations)

    ax.plot_surface(X, Y, Z, cmap='plasma')
    ax.scatter3D(x_vals, y_vals, z_vals, c='blue')  # Plot the points of the gradient descent algorithm
    ax.set_title(f'b = {b}')

    plt.show()

# Plot gradient descent iterations for different values of b
plot_gradient_descent_3d(1)
plot_gradient_descent_3d(1/2)
plot_gradient_descent_3d(1/5)
plot_gradient_descent_3d(1/10)
