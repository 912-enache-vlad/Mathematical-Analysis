import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Matrix A1:
A1 = np.array([[2, 0], [0, 2]])

# Matrix A2:
A2 = np.array([[3, 0], [0, 1]])

# Matrix A3:
A3 = np.array([[-2, 0], [0, -2]])

# Matrix A4:
A4 = np.array([[-3, 0], [0, -1]])

# Matrix A5:
A5 = np.array([[1, 0], [0, -1]])

# Matrix A6:
A6 = np.array([[0, 1], [1, 0]])

# Generate values for x and y:
x = np.linspace(-2, 2, 50)  # 100 linearly spaced numbers
y = np.linspace(-2, 2, 50)  # 100 linearly spaced numbers
X, Y = np.meshgrid(x, y)  # grid of point

# Compute the quadratic function for each matrix:
Z1 = X**2*A1[0,0] + Y**2*A1[1,1] + 2*X*Y*A1[0,1]
Z2 = X**2*A2[0,0] + Y**2*A2[1,1] + 2*X*Y*A2[0,1]
Z3 = X**2*A3[0,0] + Y**2*A3[1,1] + 2*X*Y*A3[0,1]
Z4 = X**2*A4[0,0] + Y**2*A4[1,1] + 2*X*Y*A4[0,1]
Z5 = X**2*A5[0,0] + Y**2*A5[1,1] + 2*X*Y*A5[0,1]
Z6 = X**2*A6[0,0] + Y**2*A6[1,1] + 2*X*Y*A6[0,1]

# Plot the 3D surface for each matrix:
fig = plt.figure(figsize=(12, 4))

ax1 = fig.add_subplot(1, 3, 1, projection='3d')
ax1.plot_surface(X, Y, Z1)
ax1.set_title("Matrix A1")

ax2 = fig.add_subplot(1, 3, 2, projection='3d')
ax2.plot_surface(X, Y, Z2)
ax2.set_title("Matrix A2")

ax3 = fig.add_subplot(1, 3, 3, projection='3d')
ax3.plot_surface(X, Y, Z3)
ax3.set_title("Matrix A3")

fig = plt.figure(figsize=(12, 4))

ax4 = fig.add_subplot(1, 3, 1, projection='3d')
ax4.plot_surface(X, Y, Z4)
ax4.set_title("Matrix A4")

ax5 = fig.add_subplot(1, 3, 2, projection='3d')
ax5.plot_surface(X, Y, Z5)
ax5.set_title("Matrix A5")

ax6 = fig.add_subplot(1, 3, 3, projection='3d')
ax6.plot_surface(X, Y, Z6)
ax6.set_title("Matrix A6")

plt.show()
