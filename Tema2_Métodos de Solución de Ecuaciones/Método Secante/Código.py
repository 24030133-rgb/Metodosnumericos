# Método de la Secante

def secante(f, x0, x1, tolerancia=1e-6, max_iter=100):
    print(f"{'Iteración':<12} {'x':<20} {'f(x)':<20} {'Error':<20}")
    print("-" * 70)

    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)

        # Evitar división entre cero
        if abs(fx1 - fx0) < 1e-12:
            print("Error: división entre cero")
            return None

        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        error = abs(x2 - x1)

        print(f"{i+1:<12} {round(x2, 6):<20} {round(f(x2), 6):<20} {round(error, 6):<20}")

        if error < tolerancia:
            print(f"\nRaíz encontrada: {round(x2, 6)}")
            return x2

        x0, x1 = x1, x2

    print("No convergió")
    return None


# Caso 1
print("=== Secante: f(x) = x² - 2 ===")
def f1(x):
    return x**2 - 2

secante(f1, 1.0, 2.0)


# Caso 2 (Ejercicio)
print("\n=== Ejercicio: f(x) = x³ - x - 2 ===")
def f2(x):
    return x**3 - x - 2

secante(f2, 1.0, 2.0)