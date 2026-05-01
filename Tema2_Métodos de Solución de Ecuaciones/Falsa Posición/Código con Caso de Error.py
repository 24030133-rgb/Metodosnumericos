# Método de Falsa Posición con ERROR

def falsa_posicion(f, a, b):
    if f(a) * f(b) > 0:
        print("Error: f(a) y f(b) tienen el mismo signo")
        print(f"f(a) = {f(a)}, f(b) = {f(b)}")
        return None

    print("Todo bien (no debería llegar aquí en este ejemplo)")



def f(x):
    return x**2 + 1  # Siempre positiva

print("=== Caso con ERROR ===")
falsa_posicion(f, -1, 1)