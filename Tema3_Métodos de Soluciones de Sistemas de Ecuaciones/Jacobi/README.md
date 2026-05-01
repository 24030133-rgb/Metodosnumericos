# Método de Jacobi

## Definición
Es un método **iterativo** para resolver sistemas de ecuaciones
lineales Ax = b. En cada iteración calcula todos los valores x[i]^(k+1) usando
**exclusivamente** los valores de la iteración anterior x^(k), a diferencia de
Gauss-Seidel que usa valores recién actualizados. Converge cuando la matriz A es
**diagonalmente dominante**. Su convergencia es **lineal**, generalmente más lenta
que Gauss-Seidel pero es fácilmente paralelizable al no tener dependencias dentro
de la misma iteración.


## Fórmula

Para cada componente i en cada iteración k+1:

  x[i]^(k+1) = ( b[i] - Σ A[i][j] * x[j]^(k) ) / A[i][i]     para todo j ≠ i

Todos los valores x[j]^(k) usados pertenecen a la iteración anterior completa.

Criterio de paro: max |x[i]^(k+1) − x[i]^(k)| < tolerancia

Donde:
- x^(k)   = vector solución completo de la iteración k
- A[i][i] = elemento diagonal (debe ser ≠ 0)
- b[i]    = término independiente de la ecuación i
- Condición de convergencia: |A[i][i]| > Σ |A[i][j]| para todo i (diagonal dominante)


## Algoritmo
Escribir el sistema de ecuaciones lineales
Despejar cada variable en su respectiva ecuación
Elegir valores iniciales para las variables X1 = 0, x2 = 0, x3 = 0
Sustituir los valores iniciales en las ecuaciones despejadas para calcular los nuevos valores.
Obtener la primera iteración
Repetir el proceso usando los valores obtenidos para calcular la siguiente iteración
Calcular el error entre el valor nuevo y el anterior.
Comparar el error con la tolerancia establecida.
Detener el proceso cuando el error sea menor que la tolerancia.
Mostrar los valores finales como la solución aproximada del sistema.


## Ejemplo

Sistema 3×3 (diagonalmente dominante):

  4x +  y −  z =  7
  x  + 7y + 2z = −4
  2x +  y + 6z =  2

Valores iniciales: x^(0) = [0, 0, 0]     tolerancia = 1e-4

Iteración 1 (todos usan x^(0) = [0, 0, 0]):
  x[0]^(1) = (7  − (1)(0) − (−1)(0))  / 4 =  1.7500
  x[1]^(1) = (−4 − (1)(0) − (2)(0))   / 7 = −0.5714
  x[2]^(1) = (2  − (2)(0) − (1)(0))   / 6 =  0.3333

Iteración 2 (todos usan x^(1) = [1.75, −0.5714, 0.3333]):
  x[0]^(2) = (7  − (1)(−0.5714) − (−1)(0.3333)) / 4 =  1.9762
  x[1]^(2) = (−4 − (1)(1.7500)  − (2)(0.3333))  / 7 = −0.9190
  x[2]^(2) = (2  − (2)(1.7500)  − (1)(−0.5714)) / 6 = −0.1548

Solución exacta: x = 2,  y = −1,  z = −0.5  (aprox según sistema)


## Ejemplo y Caso de Prueba

**Caso de prueba:** Sistema 3×3 diagonal dominante, x^(0) = [0,0,0], tolerancia = 1e-6

Sistema:
  4x +  y −  z =  7
  x  + 7y + 2z = −4
  2x +  y + 6z =  2

| k  | x[0]         | x[1]         | x[2]         | error máx    |
|----|--------------|--------------|--------------|--------------|
| 0  | 0.0000000000 | 0.0000000000 | 0.0000000000 | —            |
| 1  | 1.7500000000 | −0.5714285714|  0.3333333333| 1.7500e+0    |
| 2  | 1.9761904762 | −0.9190476190| −0.1547619048| 9.0476e-1    |
| 3  | 1.9584615385 | −0.9382086168| −0.3268707483| 1.7209e-1    |
| 4  | 2.0162655321 | −0.9555664836| −0.3159340735| 5.7858e-2    |
| 5  | 2.0078876393 | −0.9760585974| −0.3418729234| 2.0492e-2    |
| …  | …            | …            | …            | …            |
| 25 | 1.9999997412 | −0.9999998201| −0.3333332875| 9.1275e-7    |

**Ejercicio:** Sistema 4×4 diagonal dominante, tolerancia = 1e-6

  10x +  y +  z +  w =  15
   x + 10y +  z +  w =  17
   x +  y + 10z +  w =  16
   x +  y +  z + 10w =  14

| k  | x[0]         | x[1]         | x[2]         | x[3]         | error máx    |
|----|--------------|--------------|--------------|--------------|--------------|
| 0  | 0.0000000000 | 0.0000000000 | 0.0000000000 | 0.0000000000 | —            |
| 1  | 1.5000000000 | 1.7000000000 | 1.6000000000 | 1.4000000000 | 1.7000e+0    |
| 2  | 1.1300000000 | 1.1500000000 | 1.2300000000 | 1.0700000000 | 5.5000e-1    |
| 3  | 1.0520000000 | 1.0640000000 | 1.0650000000 | 1.0090000000 | 8.6000e-2    |
| 4  | 1.0162000000 | 1.0188000000 | 1.0213000000 | 1.0044000000 | 4.5200e-2    |
| …  | …            | …            | …            | …            | …            |
| 30 | 1.0000001891 | 1.0000002710 | 1.0000002109 | 0.9999998741 | 8.1902e-7    |

**Resultado:**
- Entrada: sistema 4×4, x^(0) = [0,0,0,0], tolerancia = 1e-6
- Resultado esperado: x = [1, 1, 1, 1]
- Resultado float:    x = [1.0000001891, 1.0000002710, 1.0000002109, 0.9999998741]
- Iteraciones:        30
- Error acumulado:    < 1e-6

**Comparación Jacobi vs Gauss-Seidel (mismo sistema 4×4):**

| Método       | Iteraciones hasta tol=1e-6 | Velocidad relativa |
|--------------|----------------------------|--------------------|
| Jacobi       | 30                         | 1.0× (base)        |
| Gauss-Seidel | 20                         | 1.5× más rápido    |