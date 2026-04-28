# REGLA DE 5 PUNTOS - Ejercicio 1


def cinco_puntos(f, x, h):
    return (-f(x+2*h) + 8*f(x+h) - 8*f(x-h) + f(x-2*h)) / (12*h)

f5 = lambda x: x**2
resultado5 = cinco_puntos(f5, 2, 1)
print(f"5 Puntos f'(2): {resultado5:.4f}")