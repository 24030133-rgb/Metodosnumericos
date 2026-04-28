# Regla de Simpson 1/3

## Definición
Es un método de integración numérica que aproxima 
el valor de una integral definida. En lugar de usar líneas rectas como el 
método del trapecio, utiliza parábolas polinomios de grado 2 para 
aproximar la función entre cada par de subintervalos.

Para que funcione correctamente, el número de subintervalos **n debe ser par**.


## Fórmula

∫[a,b] f(x) dx ≈ (h/3) * [f(x₀) + 4f(x₁) + 2f(x₂) + 4f(x₃) + ... + 4f(xₙ₋₁) + f(xₙ)]

Donde:
- h = (b - a) / n  →  tamaño del subintervalo
- n  →  número de subintervalos debe ser PAR
- xᵢ = a + i·h  →  puntos de evaluación

Patrón de coeficientes: 1, 4, 2, 4, 2, ..., 4, 1

## Algoritmo

Definir la funcion f(x)
Definir el limite inferior a
Definir el límite superior b
Definir el número de subintervalos n
Verificar si se puede usar Simpson
Se hace una verificacion para ver si se puede usar la regla de Simpson 
Si n no es par, entonces no puedo aplicar el método
Calcular el tamaño de cada intervalo h
Generar los puntos en el eje x
Evaluar la función en cada punto
Sumar los extremos
Recorrer los puntos intermedios
Aplicar la fórmula final
Finalmente obtenemos el resultado 



## Ejemplo y Caso de Prueba

**Integral:** ∫[0,2] √(1 + x²/4) dx,  con n = 8

| i | xi   | f(xi)  | Coeficiente |
|---|------|--------|-------------|
| 0 | 0.00 | 1.0000 | 1           |
| 1 | 0.25 | 1.0078 | 4           |
| 2 | 0.50 | 1.0308 | 2           |
| 3 | 0.75 | 1.0680 | 4           |
| 4 | 1.00 | 1.1180 | 2           |
| 5 | 1.25 | 1.1792 | 4           |
| 6 | 1.50 | 1.2500 | 2           |
| 7 | 1.75 | 1.3292 | 4           |
| 8 | 2.00 | 1.4142 | 1           |

**Resultado:** `Simpson 1/3 ≈ 2.2956`





