# Método de Newton-Raphson

## Definición
Algoritmo iterativo para encontrar raíces de funciones no lineales f(x) = 0.
Parte de una aproximación inicial x₀ y usa la tangente a la curva en cada
punto para generar una mejor aproximación. Su convergencia es **cuadrática**:
los dígitos correctos se duplican en cada iteración cuando x₀ está cerca de
la raíz. Falla si f′(xₙ) ≈ 0 (punto crítico) o si x₀ está muy lejos de la raíz.


## Fórmula

x_(n+1) = x_n - f(x_n) / f'(x_n)

Donde:
- f(x)  = función original
- f'(x) = derivada de la función
- Criterio de paro: |x_(n+1) - x_n| < tolerancia


## Algoritmo
Definir f(x) y su derivada f'(x)
Elegir una aproximación inicial x0
Calcular x1 = x0 - f(x0) / f'(x0)
Repetir hasta que |x_(n+1) - x_n| < tolerancia
Si f'(x_n) ≈ 0 → el método falla (punto crítico)
Retornar la raíz aproximada x_n


## Ejemplo

f(x) = x² - 2     f'(x) = 2x     x0 = 1.0

x1 = 1.0   - (1.0 - 2) / (2·1.0)   = 1.5
x2 = 1.5   - (0.25)    / (3.0)      = 1.41667
x3 = 1.41667 - ...                  = 1.41421356...

Raíz exacta: √2 = 1.41421356237309504...


## Ejemplo y Caso de Prueba

**Caso de prueba:** f(x) = x² - 2, x0 = 1.0, tolerancia = 1e-6

| n | xₙ           | f(xₙ)       | f′(xₙ)  | \|xₙ₊₁ − xₙ\| |
|---|--------------|-------------|---------|----------------|
| 0 | 1.0000000000 | -1.000e+0   | 2.0000  | 5.000e-1       |
| 1 | 1.5000000000 | 2.500e-1    | 3.0000  | 8.333e-2       |
| 2 | 1.4166666667 | 6.944e-3    | 2.8333  | 2.451e-3       |
| 3 | 1.4142156863 | 6.007e-6    | 2.8284  | 2.123e-6       |
| 4 | 1.4142135624 | 4.511e-12   | 2.8284  | 1.595e-12      |

**Ejercicio:** f(x) = x³ - x - 2, x0 = 1.5, tolerancia = 1e-6

| n | xₙ           | f(xₙ)       | f′(xₙ)  | \|xₙ₊₁ − xₙ\| |
|---|--------------|-------------|---------|----------------|
| 0 | 1.5000000000 | -8.750e-1   | 5.7500  | 1.522e-1       |
| 1 | 1.6521739130 | 2.046e-1    | 7.1895  | 2.846e-2       |
| 2 | 1.5237482655 | 7.070e-3    | 6.9654  | 1.015e-3       |
| 3 | 1.5213930279 | 9.269e-6    | 6.9432  | 1.334e-6       |
| 4 | 1.5213797068 | 1.599e-11   | 6.9431  | 2.304e-12      |

**Resultado:**
- Entrada: f(x) = x³ - x - 2, x0 = 1.5, tolerancia = 1e-6
- Resultado esperado: 1.5213797068045676
- Resultado float:    1.5213797068045676
- Iteraciones:        4
- Error acumulado:    < 1e-15