import numpy as np

x = np.zeros(3)

for k in range(25):
    x_new = np.zeros(3)

    x_new[0] = (5 - x[1] - x[2]) / 3
    x_new[1] = (5 - x[0] - x[2]) / 3
    x_new[2] = (5 - x[0] - x[1]) / 3

    x = x_new

print("Solución aproximada:", x)