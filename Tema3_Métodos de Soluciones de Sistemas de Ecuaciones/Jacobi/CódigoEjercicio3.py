import numpy as np

x = np.zeros(3)

for k in range(10):
    x_new = np.zeros(3)

    x_new[0] = (7 - x[1] - x[2]) / 5
    x_new[1] = (6 - x[0] - x[2]) / 4
    x_new[2] = (5 - x[0] - x[1]) / 3

    x = x_new

print("Solución aproximada:", x)