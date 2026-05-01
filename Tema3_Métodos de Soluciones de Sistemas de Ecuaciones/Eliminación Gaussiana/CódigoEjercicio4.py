def eliminacion_gaussiana(matriz_aumentada):
    n = len(matriz_aumentada)
    A = [fila[:] for fila in matriz_aumentada]

    for k in range(n):
        # Evitar pivote cero (intercambio de filas)
        if abs(A[k][k]) < 1e-10:
            for i in range(k + 1, n):
                if abs(A[i][k]) > 1e-10:
                    A[k], A[i] = A[i], A[k]
                    break
            else:
                raise ValueError("Pivote cero, sistema singular.")

        for i in range(k + 1, n):
            factor = A[i][k] / A[k][k]
            for j in range(n + 1):
                A[i][j] -= factor * A[k][j]

    # Sustitución hacia atrás
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        if abs(A[i][i]) < 1e-10:
            raise ValueError("División entre cero.")

        x[i] = A[i][n]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]

    return x


def main():
    try:
        n = int(input("Ingrese el tamaño del sistema (n): "))
        print(f"Ingrese la matriz aumentada ({n} x {n + 1}):")

        matriz = []
        for i in range(n):
            fila = list(map(float, input(f"Fila {i + 1}: ").split()))

            # Validación
            if len(fila) != n + 1:
                print("Error: número incorrecto de datos")
                return

            matriz.append(fila)

        solucion = eliminacion_gaussiana(matriz)

        print("\nSolución:")
        for i, xi in enumerate(solucion):
            print(f"x{i + 1} = {xi:.6f}")

    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()