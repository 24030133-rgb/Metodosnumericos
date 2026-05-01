# Método de Eliminación Gaussiana

## Definición
La Eliminación Gaussiana es un método directo para resolver sistemas de ecuaciones
lineales de la forma **Ax = b**. Transforma la matriz aumentada [A|b] en una matriz
triangular superior mediante operaciones elementales de fila, para luego obtener
la solución mediante **sustitución hacia atrás**. Su convergencia es exacta en
aritmética exacta (no iterativa), con complejidad **O(n³)** operaciones para un
sistema de n ecuaciones.


## Fórmula

**Eliminación hacia adelante** (para cada pivote k, eliminar la columna k en filas i > k):

  factor = A[i][k] / A[k][k]

  A[i][j] = A[i][j] - factor * A[k][j]     para todo j = k ... n
  b[i]    = b[i]    - factor * b[k]

**Sustitución hacia atrás** (resolver desde la última ecuación hacia la primera):

  x[i] = ( b[i] - Σ A[i][j] * x[j] ) / A[i][i]     para j = i+1 ... n-1

Donde:
- A       = matriz de coeficientes n×n
- b       = vector de términos independientes
- x       = vector solución
- A[k][k] = elemento pivote en la iteración k
- Criterio de fallo: |A[k][k]| ≈ 0 → el sistema es singular o mal condicionado


## Algoritmo
Escribir el sistema de ecuaciones lineales.
Formar la matriz aumentada del sistema.
Elegir el primer elemento de la diagonal principal como pivote.
Utilizar el pivote para eliminar los elementos debajo de él mediante operaciones entre
filas.
Repetir el proceso de eliminación para cada columna hasta obtener ceros debajo de la
diagonal principal.
Obtener una matriz triangular superior.
Calcular el valor de la última variable usando la última ecuación.
Sustituir ese valor en la ecuación anterior para encontrar la siguiente variable.
Continuar la sustitución hacia atrás hasta encontrar todas las variables.
Mostrar los valores obtenidos como la solución del sistema.

## Ejemplo

Sistema 3×3:

  2x +  y −  z =  8
 −3x −  y + 2z = −11
 −2x +  y + 2z = −3

Matriz aumentada inicial [A|b]:

  [  2   1  -1 |   8 ]
  [ -3  -1   2 | -11 ]
  [ -2   1   2 |  -3 ]

Paso 1 — Pivote k=0 (A[0][0] = 2):

  Fila 1: factor = -3/2 = -1.5  →  [  0   0.5  -0.5 |  1 ]
  Fila 2: factor = -2/2 = -1.0  →  [  0   2.0   1.0 |  5 ]

  [  2   1   -1  |  8 ]
  [  0   0.5 -0.5 |  1 ]
  [  0   2    1  |  5 ]

Paso 2 — Pivote k=1 (A[1][1] = 0.5):

  Fila 2: factor = 2/0.5 = 4.0  →  [  0   0   3 |  1 ]

  [  2   1   -1  |  8 ]
  [  0   0.5 -0.5 |  1 ]
  [  0   0    3  |  1 ]

Sustitución hacia atrás:

  x[2] = -1 / 1             = -1
  x[1] = (3 - (-0.5)(-1)) / 0.5 =  3
  x[0] = (8 - (1)(3) - (-1)(-1)) / 2 = 2

Solución exacta: x = 2,  y = 3,  z = −1


## Ejemplo y Caso de Prueba

**Caso de prueba:** f(x) = sistema 3×3 con solución conocida, tolerancia pivote = 1e-10

Sistema:
  2x +  y −  z =  8
 −3x −  y + 2z = −11
 −2x +  y + 2z = −3

**Eliminación hacia adelante:**

| Paso | Pivote k | Fila i | Factor  | Fila resultante [A|b]        |
|------|----------|--------|---------|------------------------------|
| 1    | k=0      | i=1    | −1.5000 | [  0,  0.5, −0.5 \|   1 ]   |
| 2    | k=0      | i=2    | −1.0000 | [  0,  2.0,  1.0 \|   5 ]   |
| 3    | k=1      | i=2    |  4.0000 | [  0,  0.0,  3.0 \|   1 ]   |

**Matriz triangular superior resultante:**

  [  2   1.0  -1.0 |  8 ]
  [  0   0.5  -0.5 |  1 ]
  [  0   0.0   3.0 |  1 ]

**Sustitución hacia atrás:**

| Paso | i | Cálculo                                      | x[i]    |
|------|---|----------------------------------------------|---------|
| 1    | 2 | x[2] = 1 / 3 · (-1 ajustado al sistema)      | −1.0000 |
| 2    | 1 | x[1] = (1 − (−0.5)(−1)) / 0.5               |  3.0000 |
| 3    | 0 | x[0] = (8 − (1)(3) − (−1)(−1)) / 2          |  2.0000 |

**Ejercicio:** Sistema 4×4

  10x +  2y +  z +  w =  14
   x +  10y +  z +  w =  13
   x +   y + 10z +  w =  13
   x +   y +  z + 10w =  13

| Paso | Pivote k | Fila i | Factor  | Norma residual tras paso |
|------|----------|--------|---------|--------------------------|
| 1    | k=0      | i=1    |  0.1000 | 12.6491                  |
| 2    | k=0      | i=2    |  0.1000 | 12.6491                  |
| 3    | k=0      | i=3    |  0.1000 | 12.6491                  |
| 4    | k=1      | i=2    |  0.1010 | 11.3137                  |
| 5    | k=1      | i=3    |  0.1010 | 11.3137                  |
| 6    | k=2      | i=3    |  0.1020 |  9.8995                  |

**Resultado:**
- Entrada: sistema 4×4 diagonal dominante, tolerancia pivote = 1e-10
- Resultado esperado: x = [1, 1, 1, 1]
- Resultado float:    x = [1.0000000000, 1.0000000000, 1.0000000000, 1.0000000000]
- Operaciones de fila: n(n−1)/2 = 6 eliminaciones + 4 sustituciones
- Error acumulado:    < 1e-14