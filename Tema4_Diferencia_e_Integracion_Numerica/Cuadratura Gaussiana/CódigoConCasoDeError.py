# GAUSSIANA - CASO DE ERROR

import numpy as np

def gauss_seguro(f, a, b):
    t1, t2 = -1/np.sqrt(3), 1/np.sqrt(3)
    factor = (b - a) / 2
    mid = (a + b) / 2
    x1 = factor * t1 + mid
    x2 = factor * t2 + mid
    fx1 = f(x1)
    fx2 = f(x2)
    if np.isnan(fx1) or np.isnan(fx2):
        raise ValueError(f"Función no definida en x={x1:.4f} o x={x2:.4f}")
    return factor * (fx1 + fx2)

try:
    f_err3 = lambda x: np.sqrt(x - 2) if x >= 2 else float('nan')
    gauss_seguro(f_err3, 0, 4)
except ValueError as e:
    print(f"Error Gaussiana: {e}")