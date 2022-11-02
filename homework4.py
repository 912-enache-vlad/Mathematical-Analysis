import matplotlib.pyplot as plt
import numpy as np

n = int(input("Enter a number:"))

ax = plt.subplot()
x = [i for i in range(0, n)]
y = [((-1) ** (i + 1) / i) for i in range(1, 10 * n)]
sumy = [0]
j = 1
for i in range(0, n, 2):
    sumy.append(sumy[j-1] + y[i])
    j += 1
    sumy.append(sumy[j-1] + y[(i+1) * 2 - 1])
    j += 1
    sumy.append(sumy[j-1] + y[(i+1) * 2 + 1])
    j += 1

ax.plot(sumy, marker = ".", linestyle = "--", color = "r")
ax.grid(True)
plt.show()