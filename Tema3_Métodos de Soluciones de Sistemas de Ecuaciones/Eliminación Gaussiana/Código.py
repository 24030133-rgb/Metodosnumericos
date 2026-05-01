def eliminacion_gaussiana(matriz):
    n = len(matriz)

    # Eliminación hacia adelante (con pivoteo parcial)
    for i in range(n):
        # Buscar pivote máximo
        max_fila = i
        for k in range(i + 1, n):
            if abs(matriz[k][i]) > abs(matriz[max_fila][i]):
                max_fila = k

        # Intercambiar filas
        matriz[i], matriz[max_fila] = matriz[max_fila], matriz[i]

        # Verificar pivote
        if abs(matriz[i][i]) < 1e-10:
            raise ValueError("Error: La matriz es singular o casi singular.")

        # Eliminación
        for k in range(i + 1, n):
            factor = matriz[k][i] / matriz[i][i]
            for j in range(i, n + 1):
                matriz[k][j] -= factor * matriz[i][j]

    # Sustitución hacia atrás
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = matriz[i][n]
        for j in range(i + 1, n):
            x[i] -= matriz[i][j] * x[j]
        x[i] /= matriz[i][i]

    return x


# =========================
# PROGRAMA PRINCIPAL
# =========================

print("=" * 50)
print("   ELIMINACIÓN GAUSSIANA")
print("=" * 50)

n = int(input("Ingrese el tamaño del sistema (n): "))
print(f"\nIngrese la matriz aumentada ({n} x {n + 1}):")

matriz = []

for i in range(n):
    fila = list(map(float, input(f"Fila {i + 1}: ").split()))

    if len(fila) != n + 1:
        print(f"Error: Debe ingresar exactamente {n + 1} valores")
        exit()

    matriz.append(fila)

try:
    solucion = eliminacion_gaussiana(matriz)

    print("\nSolución:")
    for i, xi in enumerate(solucion):
        print(f"x{i + 1} = {xi:.6f}")

except ValueError as e:
    print("\nError:", e)