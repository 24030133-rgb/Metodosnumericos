# 5 PUNTOS - CASO DE ERROR
# f(x) = ln(x-2) en x=2, h=0.5 → puntos inválidos
import numpy as np

def cinco_puntos_seguro(f, x, h):
    puntos = [x+2*h, x+h, x-h, x-2*h]
    valores = []
    for p in puntos:
        v = f(p)
        if v != v or np.isinf(v):
            raise ValueError(f"Función no definida en x={p:.2f}")
        valores.append(v)
    return (-valores[0] + 8*valores[1] - 8*valores[2] + valores[3]) / (12*h)

try:
    f_err5 = lambda x: np.log(x - 2) if x > 2 else float('nan')
    cinco_puntos_seguro(f_err5, 2, 0.5)
except ValueError as e:
    print(f"Error 5 Puntos: {e}")
