# Regla del Trapecio

## Definición
Es un método de integración numérica que aproxima
el área bajo una curva usando trapecios en lugar de rectángulos. Conecta
los puntos extremos de la función con una línea recta y calcula el área
del trapecio resultante. Es el método más simple de integración numérica
pero su precisión depende de qué tan lineal sea la función en el intervalo.



## Fórmula

∫[a,b] f(x) dx ≈ ((b-a)/2) * (f(a) + f(b))

Donde:
- a      →  límite inferior del intervalo
- b      →  límite superior del intervalo
- f(a)   →  valor de la función en el extremo izquierdo
- f(b)   →  valor de la función en el extremo derecho
- (b-a)  →  ancho del intervalo



## Algoritmo

Tener f(x),a,b,n
Calcular h=(b−a)/n
Generar puntos desde x0 hasta xn
Evaluar la función en cada punto
Sumar extremos: f(x0)+f(xn)
Sumar intermedios y multiplicar por 2
Multiplicar todo por h/2
Retornar resultado


## Ejemplo y Caso de Prueba

**Integral:** ∫[0,4] (x² + 2x) dx

| Punto | x   | f(x) = x² + 2x |
|-------|-----|-----------------|
| a     | 0.0 | 0.0             |
| b     | 4.0 | 24.0            |

resultado = ((4-0)/2) * (0.0 + 24.0) = 2 * 24 = **40.0000**

**Resultado:** `Trapecio = 40.0000`

> Valor exacto: ∫[0,4] (x² + 2x) dx = 42.6667
> El error es de 2.6667 porque la función no es lineal.
