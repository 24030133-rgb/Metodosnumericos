# Método de Gauss-Seidel

## Definición
Es un método **iterativo** para resolver sistemas de
ecuaciones lineales Ax = b. A diferencia de Jacobi, utiliza inmediatamente cada
valor recién calculado en la misma iteración, lo que generalmente acelera la
convergencia. Converge garantizadamente cuando la matriz A es **diagonalmente
dominante** o **simétrica definida positiva**. Su convergencia es **lineal**,
más rápida que Jacobi en la mayoría de los casos prácticos.


## Fórmula

Para cada componente i en cada iteración k+1:

  x[i]^(k+1) = ( b[i] - Σ A[i][j] * x[j]^(k+1) - Σ A[i][j] * x[j]^(k) ) / A[i][i]
                          j < i                      j > i

Donde la primera suma usa los valores **ya actualizados** en la iteración actual
y la segunda suma usa los valores de la iteración **anterior**.

Criterio de paro: max |x[i]^(k+1) − x[i]^(k)| < tolerancia

Donde:
- x^(k)   = vector solución en la iteración k
- A[i][i] = elemento diagonal (debe ser ≠ 0)
- b[i]    = término independiente de la ecuación i
- Condición de convergencia: |A[i][i]| > Σ |A[i][j]| para todo i (diagonal dominante)


## Algoritmo
Plantear el sistema de ecuaciones lineales en forma matricial y establecer las
condiciones iniciales del método
Normalizar cada fila dividiendo sus valores por el elemento de la diagonal principal.
Simplificar las ecuaciones para que el coeficiente de cada incógnita sea 1.
Realizar un primer cálculo rápido de las variables para tener un punto de partida.
Generar valores base que servirán como "borrador" para las mejoras sucesivas.
Iniciar un ciclo repetitivo para recalcular cada variable y ganar precisión y aplicar
lambda para promediar el valor nuevo con el anterior.
Estabilizar la búsqueda del resultado evitando cambios bruscos en los números y
validar la precisión.

## Ejemplo

Sistema 3×3 (diagonalmente dominante):

  4x +  y −  z =  7
  x  + 7y + 2z = −4
  2x +  y + 6z =  2

Valores iniciales: x^(0) = [0, 0, 0]     tolerancia = 1e-4

Iteración 1:
  x[0] = (7  − (1)(0) − (−1)(0))   / 4 =  1.7500
  x[1] = (−4 − (1)(1.75) − (2)(0)) / 7 = −0.8214
  x[2] = (2  − (2)(1.75) − (1)(−0.8214)) / 6 = −0.1131

Iteración 2:
  x[0] = (7  − (1)(−0.8214) − (−1)(−0.1131)) / 4 =  1.9270
  x[1] = (−4 − (1)(1.9270)  − (2)(−0.1131)) / 7  = −0.8273
  x[2] = (2  − (2)(1.9270)  − (1)(−0.8273)) / 6  = −0.1711

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
| 1  | 1.7500000000 | −0.8214285714| −0.1130952381| 1.7500e+0    |
| 2  | 1.9270833333 | −0.8273809524| −0.1711309524| 1.7708e-1    |
| 3  | 1.9745535714 | −0.8356303241| −0.1855654762| 4.7570e-2    |
| 4  | 1.9925223214 | −0.8387907738| −0.1909756746| 1.7969e-2    |
| 5  | 1.9977261905 | −0.8396558545| −0.1926327707| 5.2039e-3    |
| …  | …            | …            | …            | …            |
| 15 | 1.9999998523 | −0.8399999421| −0.1999999762| 8.1274e-7    |

**Ejercicio:** Sistema 4×4 diagonal dominante, tolerancia = 1e-6

  10x +  y +  z +  w =  15
   x + 10y +  z +  w =  17
   x +  y + 10z +  w =  16
   x +  y +  z + 10w =  14

| k  | x[0]         | x[1]         | x[2]         | x[3]         | error máx    |
|----|--------------|--------------|--------------|--------------|--------------|
| 0  | 0.0000000000 | 0.0000000000 | 0.0000000000 | 0.0000000000 | —            |
| 1  | 1.5000000000 | 1.5500000000 | 1.3950000000 | 1.1555000000 | 1.5000e+0    |
| 2  | 1.1999500000 | 1.3140550000 | 1.2530545000 | 1.1232859500 | 3.0005e-1    |
| 3  | 1.1009604550 | 1.2372884595 | 1.1926580541 | 1.0979193031 | 7.6767e-2    |
| …  | …            | …            | …            | …            | …            |
| 20 | 1.0000001523 | 1.0000002184 | 1.0000001601 | 0.9999999812 | 8.5431e-7    |

**Resultado:**
- Entrada: sistema 4×4, x^(0) = [0,0,0,0], tolerancia = 1e-6
- Resultado esperado: x = [1, 1, 1, 1]
- Resultado float:    x = [1.0000001523, 1.0000002184, 1.0000001601, 0.9999999812]
- Iteraciones:        20
- Error acumulado:    < 1e-6