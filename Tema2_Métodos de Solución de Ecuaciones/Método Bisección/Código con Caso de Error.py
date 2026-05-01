# Método de Bisección con caso de error

def biseccion(f, a, b, tolerancia=1e-6, max_iter=50):
    # Caso de error
    if f(a) * f(b) > 0:
        print("Error: f(a) y f(b) tienen el mismo signo")
        print(f"f(a) = {f(a)}, f(b) = {f(b)}")
        return None

    print(f"{'Iteración':<10} {'a':<12} {'b':<12} {'c':<12} {'Error':<12}")
    print("-" * 60)

    for i in range(max_iter):
        c = (a + b) / 2
        error = abs(b - a) / 2

        print(f"{i+1:<10} {round(a,4):<12} {round(b,4):<12} {round(c,4):<12} {round(error,4):<12}")

        if error < tolerancia:
            print(f"\nRaíz encontrada: {round(c,4)}")
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("No convergió")
    return None


# FUNCIÓN
def f(x):
    return x**2 + 1   # Esta función NO cruza el eje (siempre positiva)

print("=== Caso con ERROR ===")
biseccion(f, -1, 1)