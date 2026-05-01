import numpy as np

x = np.zeros(8)

for k in range(35):
    x_new = np.zeros(8)

    x_new[0] = (20 - x[1] - x[2] - x[3] - x[4] - x[5] - x[6] - x[7]) / 16
    x_new[1] = (25 - x[0] - x[2] - x[3] - x[4] - x[5] - x[6] - x[7]) / 17
    x_new[2] = (30 - x[0] - x[1] - x[3] - x[4] - x[5] - x[6] - x[7]) / 18
    x_new[3] = (22 - x[0] - x[1] - x[2] - x[4] - x[5] - x[6] - x[7]) / 19
    x_new[4] = (27 - x[0] - x[1] - x[2] - x[3] - x[5] - x[6] - x[7]) / 20
    x_new[5] = (24 - x[0] - x[1] - x[2] - x[3] - x[4] - x[6] - x[7]) / 21
    x_new[6] = (28 - x[0] - x[1] - x[2] - x[3] - x[4] - x[5] - x[7]) / 22
    x_new[7] = (26 - x[0] - x[1] - x[2] - x[3] - x[4] - x[5] - x[6]) / 23

    x = x_new

print("Solución aproximada:", x)