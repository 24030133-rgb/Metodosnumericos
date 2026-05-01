# Método de la Secante

## Definición
Es similar a Newton-Raphson pero no requiere calcular
la derivada analítica. En su lugar usa dos aproximaciones iniciales para estimar
la pendiente de la función mediante una línea secante y converger a la raíz.
Su convergencia es **superlineal** (orden ≈ 1.618, número áureo), más lenta que
Newton-Raphson pero más práctica cuando f′(x) es difícil de calcular.


## Fórmula

x_(n+1) = x_n - f(x_n) * (x_n - x_(n-1)) / (f(x_n) - f(x_(n-1)))

Donde:
- x_n     = aproximación actual
- x_(n-1) = aproximación anterior
- f(x)    = función evaluada en cada punto
- Criterio de paro: |x_(n+1) - x_n| < tolerancia


## Algoritmo
Definir f(x)
Elegir dos aproximaciones iniciales x0 y x1
Calcular x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
Repetir hasta que |x_(n+1) - x_n| < tolerancia
Si f(x_n) - f(x_(n-1)) ≈ 0 → el método falla (división por cero)
Retornar la raíz aproximada x_n


## Ejemplo

f(x) = x² - 2     x0 = 1.0     x1 = 2.0

x2 = 2.0 - (2.0) * (2.0 - 1.0) / (2.0 - (-1.0)) = 1.33333
x3 = 1.33333 - (-0.2222) * (1.33333 - 2.0) / (-0.2222 - 2.0) = 1.40000
x4 = 1.40000 - ...  = 1.41429
x5 = 1.41429 - ...  = 1.41421356...

Raíz exacta: √2 = 1.41421356237309504...


## Ejemplo y Caso de Prueba

**Caso de prueba:** f(x) = x² - 2, x0 = 1.0, x1 = 2.0, tolerancia = 1e-6

| n | xₙ           | f(xₙ)        | |xₙ₊₁ − xₙ|  |
|---|--------------|--------------|--------------|
| 0 | 1.0000000000 | -1.0000e+0   | —            |
| 1 | 2.0000000000 |  2.0000e+0   | 1.0000e+0    |
| 2 | 1.3333333333 | -2.2222e-1   | 6.6667e-1    |
| 3 | 1.4000000000 | -4.0000e-2   | 6.6667e-2    |
| 4 | 1.4142156863 |  6.0074e-6   | 1.4216e-2    |
| 5 | 1.4142135624 | -4.5107e-12  | 2.1239e-6    |
| 6 | 1.4142135624 |  0.0000e+0   | 8.8818e-16   |

**Ejercicio:** f(x) = x³ - x - 2, x0 = 1.0, x1 = 2.0, tolerancia = 1e-6

| n | xₙ           | f(xₙ)        | |xₙ₊₁ − xₙ|  |
|---|--------------|--------------|--------------|
| 0 | 1.0000000000 | -2.0000e+0   | —            |
| 1 | 2.0000000000 |  4.0000e+0   | 1.0000e+0    |
| 2 | 1.3333333333 | -1.0370e+0   | 6.6667e-1    |
| 3 | 1.4594594595 | -4.4547e-1   | 1.2612e-1    |
| 4 | 1.5310734464 |  8.5942e-2   | 7.1614e-2    |
| 5 | 1.5211252166 | -3.1847e-3   | 9.9482e-3    |
| 6 | 1.5213797068 |  1.5987e-7   | 2.5449e-4    |
| 7 | 1.5213797068 |  0.0000e+0   | 3.1746e-8    |

**Resultado:**
- Entrada: f(x) = x³ - x - 2, x0 = 1.0, x1 = 2.0, tolerancia = 1e-6
- Resultado esperado: 1.5213797068045676
- Resultado float:    1.5213797068045676
- Iteraciones:        7
- Error acumulado:    < 1e-15