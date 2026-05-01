def Gseid(a, b, n, x, imax, es, lmbda):
    # Normalizar cada fila
    for i in range(n):
        dummy = a[i][i]
        for j in range(n):
            a[i][j] = a[i][j] / dummy
        b[i] = b[i] / dummy

    # Estimación inicial
    for i in range(n):
        suma = b[i]
        for j in range(n):
            if i != j:
                suma = suma - a[i][j] * x[j]
        x[i] = suma

    iter = 1

    # Iteraciones
    while True:
        centinela = 1

        for i in range(n):
            old = x[i]
            suma = b[i]

            for j in range(n):
                if i != j:
                    suma = suma - a[i][j] * x[j]

            x[i] = lmbda * suma + (1.0 - lmbda) * old

            if centinela == 1 and x[i] != 0:
                ea = abs((x[i] - old) / x[i]) * 100
                if ea > es:
                    centinela = 0

        print(f"Iteración {iter}: {x}")  # 👈 AQUÍ IMPRIME

        iter += 1

        if centinela == 1 or iter >= imax:
            break

    return x, iter


# =========================
# 🔹 EJEMPLO (IMPORTANTE)
# =========================

A = [
    [4, 1, 2],
    [3, 5, 1],
    [1, 1, 3]
]

b = [4, 7, 3]

n = 3
x = [0.0, 0.0, 0.0]
imax = 50
es = 0.01
lmbda = 1.0

sol, it = Gseid(A, b, n, x, imax, es, lmbda)

print("\nResultado final:")
print("Solución:", sol)
print("Iteraciones:", it)