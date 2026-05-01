# Método de Bisección

## Definición
Es uno de los métodos más simples para
encontrar raíces de ecuaciones continuas. Divide repetidamente un intervalo
[a, b] a la mitad y selecciona el subintervalo donde existe la raíz (donde
f cambia de signo), hasta converger a ella. Su convergencia es **lineal**:
gana aproximadamente un bit de precisión por iteración. Requiere que f(a)
y f(b) tengan signos opuestos (teorema del valor intermedio).


## Fórmula

c = (a + b) / 2

Error máximo garantizado tras n iteraciones:

|error| ≤ (b - a) / 2ⁿ

Donde:
- a = extremo izquierdo del intervalo
- b = extremo derecho del intervalo
- c = punto medio (candidato a raíz)
- Criterio de paro: |b - a| < tolerancia


## Algoritmo
Verificar que f(a) * f(b) < 0 (cambio de signo en el intervalo)
Calcular punto medio c = (a + b) / 2
Si |b - a| < tolerancia → retornar c como raíz
Si f(a) * f(c) < 0 → la raíz está en [a, c], hacer b = c
Si f(b) * f(c) < 0 → la raíz está en [c, b], hacer a = c
Repetir desde el paso 2


## Ejemplo

f(x) = x² - 2     Intervalo [1, 2]     f(1) = -1 < 0     f(2) = 2 > 0

iter 1: c = 1.5,     f(1.5) = 0.25  > 0  → b = 1.5  → [1.0, 1.5]
iter 2: c = 1.25,    f(1.25) = -0.4375 < 0 → a = 1.25 → [1.25, 1.5]
iter 3: c = 1.375,   f(1.375) = -0.1094 < 0 → a = 1.375 → [1.375, 1.5]
iter 4: c = 1.4375,  f(1.4375) = 0.0664 > 0 → b = 1.4375 → [1.375, 1.4375]
...
Raíz exacta: √2 = 1.41421356237309504...


## Ejemplo y Caso de Prueba

**Caso de prueba:** f(x) = x² - 2, a = 1, b = 2, tolerancia = 1e-6

| n  | a            | b            | c            | f(c)         | |b - a|      |
|----|--------------|--------------|--------------|--------------|-------------|
| 1  | 1.0000000000 | 2.0000000000 | 1.5000000000 |  2.500e-1    | 1.0000e+0   |
| 2  | 1.0000000000 | 1.5000000000 | 1.2500000000 | -4.375e-1    | 5.0000e-1   |
| 3  | 1.2500000000 | 1.5000000000 | 1.3750000000 | -1.094e-1    | 2.5000e-1   |
| 4  | 1.3750000000 | 1.5000000000 | 1.4375000000 |  6.641e-2    | 1.2500e-1   |
| 5  | 1.3750000000 | 1.4375000000 | 1.4062500000 | -2.246e-2    | 6.2500e-2   |
| …  | …            | …            | …            | …            | …           |
| 20 | 1.4142131805 | 1.4142141342 | 1.4142136574 |  4.842e-7    | 9.5367e-7   |
| 21 | 1.4142131805 | 1.4142136574 | 1.4142134190 | -2.179e-7    | 4.7684e-7   |

**Ejercicio:** f(x) = x³ - x - 2, intervalo [1, 2], tolerancia = 1e-6

| n  | a            | b            | c            | f(c)         | |b - a|      |
|----|--------------|--------------|--------------|--------------|-------------|
| 1  | 1.0000000000 | 2.0000000000 | 1.5000000000 | -8.750e-1    | 1.0000e+0   |
| 2  | 1.5000000000 | 2.0000000000 | 1.7500000000 |  1.859e+0    | 5.0000e-1   |
| 3  | 1.5000000000 | 1.7500000000 | 1.6250000000 |  4.121e-1    | 2.5000e-1   |
| 4  | 1.5000000000 | 1.6250000000 | 1.5625000000 | -2.588e-1    | 1.2500e-1   |
| 5  | 1.5625000000 | 1.6250000000 | 1.5937500000 |  7.202e-2    | 6.2500e-2   |
| …  | …            | …            | …            | …            | …           |
| 21 | 1.5213794708 | 1.5213797092 | 1.5213797092 |  2.381e-7    | 4.7684e-7   |

**Resultado:**
- Entrada: f(x) = x³ - x - 2, a = 1, b = 2, tolerancia = 1e-6
- Resultado esperado: 1.5213797068045676
- Resultado float:    1.5213797092437744
- Iteraciones:        21
- Error acumulado:    2.44e-9