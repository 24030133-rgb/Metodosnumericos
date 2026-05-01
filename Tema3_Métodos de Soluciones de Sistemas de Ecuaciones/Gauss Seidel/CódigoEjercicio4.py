import time

def gauss_seidel(A, b, tol=1e-6, imax=100, lmbda=1.0):
    n = len(A)
    a = [fila[:] for fila in A]
    bb = b[:]

    # Normalizar filas
    for i in range(n):
        if abs(a[i][i]) < 1e-12:
            raise ValueError("Error: pivote cero en la diagonal")

        dummy = a[i][i]
        for j in range(n):
            a[i][j] /= dummy
        bb[i] /= dummy

    x = [0.0] * n
    iteracion = 1
    inicio = time.time()

    while True:
        centinela = 1

        for i in range(n):
            old = x[i]
            suma = bb[i]

            for j in range(n):
                if i != j:
                    suma -= a[i][j] * x[j]

            x[i] = lmbda * suma + (1.0 - lmbda) * old

            # Error relativo (SIN % para que coincida con tol)
            if x[i] != 0:
                ea = abs((x[i] - old) / x[i])
                if ea > tol:
                    centinela = 0

        iteracion += 1

        if centinela == 1 or iteracion >= imax:
            break

    fin = time.time()
    return x, iteracion - 1, fin - inicio


# =========================
# PROGRAMA PRINCIPAL
# =========================

print("=" * 50)
print("   GAUSS-SEIDEL — SISTEMA 15x15")
print("=" * 50)

n = 15
print(f"\nIngrese la matriz aumentada ({n} x {n + 1}):")

A, b = [], []

for i in range(n):
    fila = list(map(float, input(f"  Fila {i + 1}: ").split()))

    if len(fila) != n + 1:
        print(f"Error: Debe ingresar exactamente {n + 1} valores")
        exit()

    A.append(fila[:n])
    b.append(fila[n])

try:
    tol  = float(input("Tolerancia (ej: 1e-6): "))
    imax = int(input("Maximo de iteraciones : "))

    sol, it, t = gauss_seidel(A, b, tol=tol, imax=imax)

    print("\n" + "=" * 50)
    print("   SOLUCION — x11 a x15")
    print("=" * 50)

    for i in range(10, 15):
        print(f"  x{i + 1} = {sol[i]:.6f}")

    print(f"\n  Iteraciones : {it}")
    print(f"  Tiempo      : {t:.6f} segundos")
    print("=" * 50)

except ValueError as e:
    print("\nError:", e)