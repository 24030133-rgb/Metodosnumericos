# CUADRATURA GAUSSIANA 
import numpy as np

def gauss_2puntos(f, a=-1, b=1):
    t1, t2 = -1/np.sqrt(3), 1/np.sqrt(3)
    factor = (b - a) / 2
    mid = (a + b) / 2
    x1 = factor * t1 + mid
    x2 = factor * t2 + mid
    return factor * (f(x1) + f(x2))

f3 = lambda x: x**2 + 3*x + 2
resultado3 = gauss_2puntos(f3)
print(f"Cuadratura Gaussiana: {resultado3:.4f}")