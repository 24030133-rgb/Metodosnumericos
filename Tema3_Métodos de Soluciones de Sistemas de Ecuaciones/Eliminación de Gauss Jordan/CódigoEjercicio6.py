import numpy as np

np.set_printoptions(precision=2, suppress=True)

def gauss_jordan_10x10():
    n = 10

    # 🔹 Matriz A (diagonal dominante)
    A = np.ones((n, n))
    np.fill_diagonal(A, 10)

    # 🔹 Vector B
    B = np.arange(10, 110, 10, dtype=float)

    # 🔹 Matriz aumentada
    Ab = np.hstack((A, B.reshape(-1, 1)))

    print("Matriz inicial:")
    print(Ab)

    # 🔹 Gauss-Jordan
    for i in range(n):

        # Pivoteo
        max_fila = np.argmax(np.abs(Ab[i:, i])) + i
        if abs(Ab[max_fila, i]) < 1e-10:
            print("No tiene solución única")
            return

        Ab[[i, max_fila]] = Ab[[max_fila, i]]

        # Normalizar
        Ab[i] /= Ab[i, i]

        # Eliminar
        for j in range(n):
            if j != i:
                Ab[j] -= Ab[j, i] * Ab[i]

    print("\nMatriz final:")
    print(Ab)

    # 🔹 Soluciones
    soluciones = Ab[:, -1]

    print("\nSolución:")
    for i, val in enumerate(soluciones):
        print(f"x{i+1} = {val:.4f}")

    return soluciones


# Ejecutar
gauss_jordan_10x10()