def gauss_jordan(A):
    n = len(A)

    for i in range(n):

        # 🔹 PIVOTEO (mejorado)
        if abs(A[i][i]) < 1e-10:
            for k in range(i + 1, n):
                if abs(A[k][i]) > 1e-10:
                    A[i], A[k] = A[k], A[i]
                    break

        pivote = A[i][i]

        if abs(pivote) < 1e-10:
            raise ValueError("El sistema no tiene solución única")

        # 🔹 NORMALIZACIÓN
        for j in range(n + 1):
            A[i][j] /= pivote

        # 🔹 ELIMINACIÓN
        for k in range(n):
            if k != i:
                factor = A[k][i]
                for j in range(n + 1):
                    A[k][j] -= factor * A[i][j]

    return A


# 🔹 MATRIZ AUMENTADA 5x5
A = [
    [1, 2, 1, 1, 1, 10],
    [2, 3, 1, 1, 1, 13],
    [1, 1, 2, 1, 1, 12],
    [1, 1, 1, 2, 1, 11],
    [1, 1, 1, 1, 2, 14]
]

# Ejecutar
resultado = gauss_jordan(A)

print("Matriz reducida:")
for fila in resultado:
    print([round(x, 4) for x in fila])

print("\nSolución del sistema:")
variables = ["x", "y", "z", "w", "v"]

for i in range(len(resultado)):
    print(f"{variables[i]} = {resultado[i][-1]:.4f}")