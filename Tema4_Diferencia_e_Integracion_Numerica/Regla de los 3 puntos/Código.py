# REGLA DE 3 PUNTOS - Ejercicio 1


def tres_puntos(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

f4 = lambda x: x**2
resultado4 = tres_puntos(f4, 2, 1)
print(f"3 Puntos f'(2): {resultado4:.4f}")