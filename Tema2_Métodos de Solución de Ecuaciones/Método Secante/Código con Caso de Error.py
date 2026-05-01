# Método de la Secante con caso de error

def secante(f, x0, x1, tolerancia=1e-6, max_iter=10):
    print(f"{'Iteración':<12} {'x':<15} {'Error':<15}")
    print("-" * 45)

    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)

        # Caso de error
        if fx1 - fx0 == 0:
            print("\nError: división entre cero (fx1 - fx0 = 0)")
            return None

        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        error = abs(x2 - x1)

        print(f"{i+1:<12} {round(x2,5):<15} {round(error,5):<15}")

        if error < tolerancia:
            print("\nRaíz encontrada:", round(x2,5))
            return x2

        x0 = x1
        x1 = x2

    print("\nNo convergió")
    return None


# ERROR
def f(x):
    return x**2 - 4

print("=== Caso con ERROR ===")
# Aquí provocamos el error porque f(2) = 0 y f(-2) = 0 → fx1 - fx0 = 0
secante(f, 2, -2)