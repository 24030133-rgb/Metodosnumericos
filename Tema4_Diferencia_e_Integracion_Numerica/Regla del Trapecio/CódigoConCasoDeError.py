# TRAPECIO - CASO DE ERROR

import numpy as np

def trapecio_seguro(f, a, b):
    fa = f(a)
    fb = f(b)
    if np.isnan(fa) or np.isnan(fb):
        raise ValueError("Función no definida en los extremos")
    return ((b - a) / 2) * (fa + fb)

try:
    f_err2 = lambda x: np.sqrt(x - 1) if x >= 1 else float('nan')
    trapecio_seguro(f_err2, 0, 2)
except ValueError as e:
    print(f"Error Trapecio: {e}")