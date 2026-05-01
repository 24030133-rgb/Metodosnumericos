def eliminacion_gaussiana(matriz_aumentada):
    n = len(matriz_aumentada)
    A = [fila[:] for fila in matriz_aumentada]

    for k in range(n):
        if abs(A[k][k]) < 1e-10:
            raise ValueError("Pivote cero, sistema singular.")
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

    solucion = eliminacion_gaussiana(matriz)

    print("\nSolucion:")
    for i, xi in enumerate(solucion):
        print(f"x{i + 1} = {xi:.6f}")


if __name__ == "__main__":
    main()