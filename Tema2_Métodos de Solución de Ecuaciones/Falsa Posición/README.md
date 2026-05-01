# Método de Falsa Posición (Regula Falsi)

## Definición
El método de Falsa Posición combina ideas de Bisección y la Secante. Mantiene
un intervalo [a, b] con cambio de signo (como Bisección) pero en lugar de
tomar el punto medio usa una línea secante entre (a, f(a)) y (b, f(b)) para
estimar la raíz. Converge más rápido que Bisección en la mayoría de los casos,
aunque puede ser **lento si un extremo queda fijo** muchas iteraciones seguidas.


## Fórmula

c = b - f(b) * (b - a) / (f(b) - f(a))

Error acotado en cada paso:

|f(c)| → 0  con  f(a)*f(b) < 0  garantizado

Donde:
- a = extremo izquierdo del intervalo
- b = extremo derecho del intervalo
- c = nueva aproximación de la raíz (intersección de la secante con el eje x)
- Criterio de paro: |f(c)| < tolerancia


## Algoritmo
Verificar que f(a) * f(b) < 0 (cambio de signo en el intervalo)
Calcular c = b - f(b) * (b - a) / (f(b) - f(a))
Si |f(c)| < tolerancia → retornar c como raíz
Si f(a) * f(c) < 0 → la raíz está en [a, c], hacer b = c
Si f(b) * f(c) < 0 → la raíz está en [c, b], hacer a = c
Repetir desde el paso 2


## Ejemplo

f(x) = x² - 2     Intervalo [1, 2]     f(1) = -1     f(2) = 2

iter 1: c = 2 - 2*(2-1)/(2-(-1))   = 1.33333   f(c) = -0.2222
iter 2: c = 2 - 2*(2-1.3333)/...   = 1.40000   f(c) = -0.0400
iter 3: c = 2 - 2*(2-1.4000)/...   = 1.41176   f(c) = -0.0069
iter 4: c = 2 - 2*(2-1.41176)/...  = 1.41379   f(c) = -0.0012
...
Raíz exacta: √2 = 1.41421356237309504...


## Ejemplo y Caso de Prueba

**Caso de prueba:** f(x) = x² - 2, a = 1, b = 2, tolerancia = 1e-6

| n  | a            | b            | c            | f(c)         | extremo fijo |
|----|--------------|--------------|--------------|--------------|--------------|
| 1  | 1.0000000000 | 2.0000000000 | 1.3333333333 | -2.2222e-1   | b fijo       |
| 2  | 1.3333333333 | 2.0000000000 | 1.4000000000 | -4.0000e-2   | b fijo       |
| 3  | 1.4000000000 | 2.0000000000 | 1.4117647059 | -6.9204e-3   | b fijo       |
| 4  | 1.4117647059 | 2.0000000000 | 1.4137931034 | -1.1890e-3   | b fijo       |
| 5  | 1.4137931034 | 2.0000000000 | 1.4141414141 | -2.0388e-4   | b fijo       |
| …  | …            | …            | …            | …            | b fijo       |
| 13 | 1.4142134534 | 2.0000000000 | 1.4142135534 | -6.0396e-8   | b fijo       |

**Ejercicio:** f(x) = x³ - x - 2, a = 1, b = 2, tolerancia = 1e-6

| n  | a            | b            | c            | f(c)         | extremo fijo |
|----|--------------|--------------|--------------|--------------|--------------|
| 1  | 1.0000000000 | 2.0000000000 | 1.3333333333 | -1.0370e+0   | b fijo       |
| 2  | 1.3333333333 | 2.0000000000 | 1.4594594595 | -4.4547e-1   | b fijo       |
| 3  | 1.4594594595 | 2.0000000000 | 1.5028653296 | -1.5532e-1   | b fijo       |
| 4  | 1.5028653296 | 2.0000000000 | 1.5160060580 | -5.0318e-2   | b fijo       |
| 5  | 1.5160060580 | 2.0000000000 | 1.5200073846 | -1.5957e-2   | b fijo       |
| …  | …            | …            | …            | …            | b fijo       |
| 14 | 1.5213796622 | 2.0000000000 | 1.5213797054 | -4.7576e-8   | b fijo       |

**Resultado:**
- Entrada: f(x) = x³ - x - 2, a = 1, b = 2, tolerancia = 1e-6
- Resultado esperado: 1.5213797068045676
- Resultado float:    1.5213797068320279
- Iteraciones:        14
- Error acumulado:    2.74e-11