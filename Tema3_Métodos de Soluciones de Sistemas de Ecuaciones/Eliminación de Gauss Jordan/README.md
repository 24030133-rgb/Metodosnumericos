# Método de Eliminación Gauss-Jordan

## Definición
Es una extensión de la Eliminación Gaussiana que
no solo reduce la matriz a forma triangular superior, sino que la lleva hasta
la **forma escalonada reducida por filas (RREF)**. Elimina los elementos tanto
por debajo como por encima de cada pivote, y normaliza cada fila pivote para
que el pivote valga 1. El resultado es la solución directa **sin necesidad de
sustitución hacia atrás**. Su complejidad es **O(n³)** pero con mayor constante
que Gaussiana simple.


## Fórmula

**Normalización del pivote** (hacer A[k][k] = 1):

  A[k][j] = A[k][j] / A[k][k]     para todo j = 0 ... n
  b[k]    = b[k]    / A[k][k]

**Eliminación hacia arriba y abajo** (para toda fila i ≠ k):

  factor  = A[i][k]
  A[i][j] = A[i][j] - factor * A[k][j]     para todo j = 0 ... n
  b[i]    = b[i]    - factor * b[k]

Donde:
- A       = matriz de coeficientes n×n
- b       = vector de términos independientes
- x       = vector solución (leído directamente de b al finalizar)
- A[k][k] = elemento pivote en la iteración k
- Criterio de fallo: |A[k][k]| ≈ 0 → el sistema es singular o mal condicionado


## Algoritmo
Matriz Aumentada: Escribe el sistema de ecuaciones en forma de matriz
combinando la matriz de coeficientes A y el vector de resultados B.
Pivoteo: En la primera columna, selecciona el elemento de la diagonal principal
(el pivote). Si es cero, intercambia la fila con una inferior que no tenga un cero en
esa posición.
Normalización: Divide toda la fila del pivote por el valor del propio pivote para
convertirlo en 1.
Eliminación: Suma o resta múltiplos de la fila del pivote a todas las demás filas
(tanto arriba como abajo) para que los demás elementos de esa columna se
conviertan en 0.
Repetición: Repite el proceso para la siguiente columna, desplazándote por la
diagonal principal hasta llegar a la última fila.

## Ejemplo

Sistema 3×3:

  2x +  y −  z =  8
 −3x −  y + 2z = −11
 −2x +  y + 2z = −3

Matriz aumentada inicial [A|b]:

  [  2   1  -1 |   8 ]
  [ -3  -1   2 | -11 ]
  [ -2   1   2 |  -3 ]

Paso 1 — Pivote k=0: normalizar fila 0 ÷ 2:

  [  1   0.5  -0.5 |   4 ]
  [ -3  -1    2   | -11 ]
  [ -2   1    2   |  -3 ]

  Eliminar columna 0 en filas 1 y 2:

  [  1   0.5  -0.5 |  4 ]
  [  0   0.5   0.5 |  1 ]
  [  0   2     1   |  5 ]

Paso 2 — Pivote k=1: normalizar fila 1 ÷ 0.5:

  [  1   0.5  -0.5 |  4 ]
  [  0   1     1   |  2 ]
  [  0   2     1   |  5 ]

  Eliminar columna 1 en filas 0 y 2:

  [  1   0    -1   |  3 ]
  [  0   1     1   |  2 ]
  [  0   0    -1   |  1 ]

Paso 3 — Pivote k=2: normalizar fila 2 ÷ (−1):

  [  1   0    -1   |  3 ]
  [  0   1     1   |  2 ]
  [  0   0     1   | -1 ]

  Eliminar columna 2 en filas 0 y 1:

  [  1   0    0   |  2 ]
  [  0   1    0   |  3 ]
  [  0   0    1   | -1 ]

Solución exacta: x = 2,  y = 3,  z = −1


## Ejemplo y Caso de Prueba

**Caso de prueba:** Sistema 3×3 con solución conocida, tolerancia pivote = 1e-10

| Paso | Pivote k | Operación                    | Fila modificada         |
|------|----------|------------------------------|-------------------------|
| 1    | k=0      | Fila 0 ÷ 2                   | [ 1,  0.5, −0.5 \|  4] |
| 2    | k=0      | Fila 1 − (−3)×Fila 0         | [ 0,  0.5,  0.5 \|  1] |
| 3    | k=0      | Fila 2 − (−2)×Fila 0         | [ 0,  2.0,  1.0 \|  5] |
| 4    | k=1      | Fila 1 ÷ 0.5                 | [ 0,  1.0,  1.0 \|  2] |
| 5    | k=1      | Fila 0 − (0.5)×Fila 1        | [ 1,  0.0, −1.0 \|  3] |
| 6    | k=1      | Fila 2 − (2.0)×Fila 1        | [ 0,  0.0, −1.0 \|  1] |
| 7    | k=2      | Fila 2 ÷ (−1)                | [ 0,  0.0,  1.0 \| −1] |
| 8    | k=2      | Fila 0 − (−1)×Fila 2         | [ 1,  0.0,  0.0 \|  2] |
| 9    | k=2      | Fila 1 − (1.0)×Fila 2        | [ 0,  1.0,  0.0 \|  3] |

**Resultado:**
- Entrada: sistema 3×3, tolerancia pivote = 1e-10
- Resultado esperado: x = [2, 3, −1]
- Resultado float:    x = [2.0000000000, 3.0000000000, −1.0000000000]
- Operaciones de fila: n² eliminaciones + n normalizaciones
- Error acumulado:    < 1e-14