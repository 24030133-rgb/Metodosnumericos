import numpy as np

def eliminacion_gaussiana(matriz_aumentada):
    n = len(matriz_aumentada)
    A = [fila[:] for fila in matriz_aumentada]

    for k in range(n):
        max_fila = k
        for i in range(k + 1, n):
            if abs(A[i][k]) > abs(A[max_fila][k]):
                max_fila = i
        A[k], A[max_fila] = A[max_fila], A[k]

        if abs(A[k][k]) < 1e-10:
            raise ValueError("Error: La matriz es singular o casi singular.")

        for i in range(k + 1, n):
            factor = A[i][k] / A[k][k]
            for j in range(n + 1):
                A[i][j] -= factor * A[k][j]

    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = A[i][n]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]

    return x


def main():
    n = int(input("Ingrese el tamaño del sistema (n): "))
    print(f"Ingrese la matriz aumentada ({n} x {n + 1}):")

    matriz = []
    for i in range(n):
        fila = list(map(float, input(f"Fila {i + 1}: ").split()))
        matriz.append(fila)

    try:
        solucion = eliminacion_gaussiana(matriz)
        print("\nSolucion:")
        for i, xi in enumerate(solucion):
            print(f"x{i + 1} = {xi:.6f}")
    except ValueError as e:
        print(f"\n{e}")
        print("Intentando solucion por minimos cuadrados...")
        A = np.array([fila[:-1] for fila in matriz], dtype=float)
        b = np.array([fila[-1]  for fila in matriz], dtype=float)
        x, _, rango, _ = np.linalg.lstsq(A, b, rcond=None)
        print("\nSolucion aproximada (minimos cuadrados):")
        for i, xi in enumerate(x):
            print(f"x{i + 1} = {xi:.6f}")
        print(f"\nRango de la matriz: {rango} de {len(x)}")
        print(f"Residuo: {np.linalg.norm(A @ x - b):.2e}")


if __name__ == "__main__":
    main()