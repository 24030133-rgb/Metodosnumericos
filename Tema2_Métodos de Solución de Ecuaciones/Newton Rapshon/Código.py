# Método de Newton-Raphson

def newton_raphson(f, f_prima, x0, tolerancia=1e-6, max_iter=100):
    x = x0
    print(f"{'Iteración':<12} {'x':<20} {'f(x)':<20} {'Error':<20}")
    print("-" * 70)

    for i in range(max_iter):
        fx = f(x)
        fpx = f_prima(x)

        if fpx == 0:
            print("Error: derivada igual a cero")
            return None

        x_nuevo = x - fx / fpx
        error = abs(x_nuevo - x)

        print(f"{i+1:<12} {round(x_nuevo, 4):<20} {round(f(x_nuevo), 4):<20} {round(error, 4):<20}")

        if error < tolerancia:
            print(f"\nRaíz encontrada: {round(x_nuevo, 6)}")
            return round(x_nuevo, 6)

        x = x_nuevo

    print("No convergió en el número máximo de iteraciones")
    return None


# --- Caso de prueba ---
print("=== Newton-Raphson: f(x) = x² - 2 ===")

def f1(x): return x**2 - 2
def f1_prima(x): return 2 * x

newton_raphson(f1, f1_prima, x0=1.0)


# --- Ejercicio ---
print("\n=== Ejercicio: f(x) = x³ - x - 2 ===")

def f2(x): return x**3 - x - 2
def f2_prima(x): return 3 * x**2 - 1

newton_raphson(f2, f2_prima, x0=1.5)