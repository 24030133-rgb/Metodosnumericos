from numpy import *
import time

A = array([[5.0, 2.0, -3.0],
           [2.0, 10.0, -8.0],
           [3.0, 8.0, 13.0]])

b = array([1.0, 4.0, 7.0])

n = len(A)

x0 = array([1.0, 1.0, 1.0])
x = array([1.0, 1.0, 1.0])

nmax = 100
eps = 1e-10
k = 1

inicio = time.perf_counter()

while (k <= nmax):

    for i in range(n):
        suma = 0.0
        for j in range(n):
            if j != i:
                suma = suma + A[i, j] * x0[j]

        x[i] = (b[i] - suma) / A[i, i]

    error = max(abs(x - x0))

    if error < eps:
        fin = time.perf_counter()   # ← aquí estaba el error
        tiempo = fin - inicio

        print("MÉTODO DE JACOBI")
        print(" 1) La solución es =", [float(f"{v:.4g}") for v in x])
        print(" 2) Iteraciones =", k)
        print(" 3) Error =", float(f"{error:.4g}"))
        print(f" 4) Tiempo de ejecución = {tiempo:.4g} segundos")
        break

    for i in range(n):
        x0[i] = x[i]

    k = k + 1

if k > nmax:
    print("No converge")