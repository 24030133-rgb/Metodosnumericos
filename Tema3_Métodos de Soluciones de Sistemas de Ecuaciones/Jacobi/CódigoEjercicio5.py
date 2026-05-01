import numpy as np

x = np.zeros(6)

for k in range(30):
    x_new = np.zeros(6)

    x_new[0] = (18 - x[1] - x[2] - x[3] - x[4] - x[5]) / 10
    x_new[1] = (20 - x[0] - x[2] - x[3] - x[4] - x[5]) / 11
    x_new[2] = (16 - x[0] - x[1] - x[3] - x[4] - x[5]) / 12
    x_new[3] = (19 - x[0] - x[1] - x[2] - x[4] - x[5]) / 13
    x_new[4] = (17 - x[0] - x[1] - x[2] - x[3] - x[5]) / 14
    x_new[5] = (21 - x[0] - x[1] - x[2] - x[3] - x[4]) / 15

    x = x_new

print("Solución aproximada:", x)