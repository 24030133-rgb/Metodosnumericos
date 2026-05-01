# Método de Falsa Posición (Regula Falsi)

def falsa_posicion(f, a, b, tolerancia=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        print("Error: f(a) y f(b) deben tener signos opuestos")
        return None

    print(f"{'Iteración':<12} {'a':<12} {'b':<12} {'c':<12} {'f(c)':<12} {'Error':<12}")
    print("-" * 70)

    for i in range(max_iter):
        fa = f(a)
        fb = f(b)

        c = b - fb * (b - a) / (fb - fa)
        fc = f(c)
        error = abs(fc)

        print(f"{i+1:<12} {round(a,4):<12} {round(b,4):<12} {round(c,4):<12} {round(fc,4):<12} {round(error,4):<12}")

        if error < tolerancia:
            print(f"\nRaíz encontrada: {round(c,4)}")
            return c

        if fa * fc < 0:
            b = c
        else:
            a = c

    print("No convergió")
    return None


# Caso 1
print("=== Falsa Posición: f(x) = x² - 2 ===")
def f1(x):
    return x**2 - 2

falsa_posicion(f1, 1.0, 2.0)


# Caso 2 (Ejercicio)
print("\n=== Ejercicio: f(x) = x³ - x - 2 ===")
def f2(x):
    return x**3 - x - 2

falsa_posicion(f2, 1.0, 2.0)