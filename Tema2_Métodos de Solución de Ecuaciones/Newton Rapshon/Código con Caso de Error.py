# Método de Newton-Raphson con manejo de errores

def newton_raphson(f, f_prima, x0, tolerancia=1e-6, max_iter=100):
    x = x0
    print(f"{'Iteración':<12} {'x':<20} {'f(x)':<20} {'Error':<20}")
    print("-" * 75)

    for i in range(max_iter):
        fx = f(x)
        fpx = f_prima(x)

        # CASO DE ERROR: División por cero
        if abs(fpx) < 1e-12: # Usamos un umbral pequeño para mayor seguridad
            print(f"\n[ERROR]: La derivada en x = {x} es casi cero.")
            print("No se puede continuar: La recta tangente es horizontal.")
            return None

        x_nuevo = x - fx / fpx
        error = abs(x_nuevo - x)

        print(f"{i+1:<12} {round(x_nuevo, 6):<20} {round(f(x_nuevo), 6):<20} {round(error, 6):<20}")

        if error < tolerancia:
            print(f"\nRaíz encontrada: {round(x_nuevo, 6)}")
            return round(x_nuevo, 6)

        x = x_nuevo

    print("\n[ERROR]: No convergió en el número máximo de iteraciones.")
    return None

# --- Caso de Error: Curva con Máximo/Mínimo ---
# f(x) = x³ - 3x + 2
# f'(x) = 3x² - 3
# Si x = 1, f'(1) = 0.
print("=== Caso de Error: Derivada igual a cero ===")

def f_error(x): return x**3 - 3*x + 2
def f_prima_error(x): return 3*x**2 - 3

# Si empezamos en x0 = 1.0, f'(1) es 0 y el código detectará el error.
newton_raphson(f_error, f_prima_error, x0=1.0)