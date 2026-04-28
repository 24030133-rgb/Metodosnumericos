# 3 PUNTOS - CASO DE ERROR


def tres_puntos_seguro(f, x, h):
    fxh = f(x + h)
    fxmh = f(x - h)
    if fxh != fxh or fxmh != fxmh:  # NaN check
        raise ValueError(f"Función no definida en x-h={x-h}")
    return (fxh - fxmh) / (2 * h)

try:
    f_err4 = lambda x: (x - 1)**0.5 if x >= 1 else float('nan')
    tres_puntos_seguro(f_err4, 1, 0.5)
except ValueError as e:
    print(f"Error 3 Puntos: {e}")