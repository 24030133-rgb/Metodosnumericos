# REGLA DE SIMPSON 1/3 
import numpy as np

def simpson_13(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n debe ser par para Simpson 1/3")
    dx = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    coef = np.ones(n + 1)
    coef[1:-1:2] = 4
    coef[2:-2:2] = 2
    return (dx / 3) * np.sum(coef * y)

f1 = lambda x: np.sqrt(1 + x**2 / 4)
resultado = simpson_13(f1, 0, 2, 8)
print(f"Simpson 1/3: {resultado:.4f}")