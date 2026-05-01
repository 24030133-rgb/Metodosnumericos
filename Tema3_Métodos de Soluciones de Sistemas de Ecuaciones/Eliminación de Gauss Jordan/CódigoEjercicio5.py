import time

def gauss_jordan(matriz):
    inicio = time.time()

    n = len(matriz)
    m = [fila[:] for fila in matriz]

    for i in range(n):

        # 🔹 Pivoteo simple
        if abs(m[i][i]) < 1e-10:
            for k in range(i + 1, n):
                if abs(m[k][i]) > 1e-10:
                    m[i], m[k] = m[k], m[i]
                    break

        if abs(m[i][i]) < 1e-10:
            print("No tiene solución única")
            return

        # 🔹 Normalizar fila
        pivote = m[i][i]
        for j in range(n + 1):
            m[i][j] /= pivote

        # 🔹 Eliminar
        for k in range(n):
            if k != i:
                factor = m[k][i]
                for j in range(n + 1):
                    m[k][j] -= factor * m[i][j]

    # 🔹 Solución
    soluciones = [m[i][-1] for i in range(n)]

    print("\nSolución:")
    for i, val in enumerate(soluciones):
        print(f"x{i+1} = {val:.4f}")

    print(f"\nTiempo: {time.time() - inicio:.6f} s")

    return soluciones


# 🔹 MATRIZ 6x6
matriz = [
    [3, 6, 3, 4, 1, 6, 3],
    [3, 7, 4, 5, 3, 5, 9],
    [7, 4, 3, 3, 6, 9, 1],
    [2, 7, 5, 8, 8, 7, 5],
    [6, 8, 8, 3, 1, 7, 6],
    [3, 5, 2, 7, 6, 5, 6]
]

# Ejecutar
gauss_jordan(matriz)