# Regla de los 3 Puntos

## Definición
Es un método de diferenciación numérica que 
aproxima la derivada de una función en un punto usando tres valores 
de la función. Utiliza diferencias centradas, lo que significa que 
toma un punto a la izquierda y uno a la derecha del punto de interés,
logrando mayor precisión que las diferencias simples hacia adelante o atrás.


## Fórmula

**Fórmula de diferencia centrada:**

f'(x) ≈ (f(x+h) - f(x-h)) / (2h)

Donde:
- f'(x)  →  derivada aproximada en el punto x
- h      →  tamaño del paso debe ser pequeño
- f(x+h) →  valor de la función en x+h
- f(x-h) →  valor de la función en x-h



## Algoritmo
Definir la funcion (fx)
El punto donde quiero derivar x
El tamaño del paso h
Tomar 3 puntos uno antes x- h el punto x y uno despues x+h
Evaluar la funcion en esos puntos f (x-h), x, (x+h)
Aplicar la formula f'(X) = f(x+h)-f(x-h)/2h
Realizar las operaciones de f´(X)
Obtener el valor 


## Ejemplo y Caso de Prueba

**Función:** f(x) = x²,  en x = 2,  con h = 1

| Punto | x     | f(x) |
|-------|-------|------|
| x-h   | 1.0   | 1.0  |
| x     | 2.0   | 4.0  |
| x+h   | 3.0   | 9.0  |

f'(2) ≈ (9.0 - 1.0) / (2*1) = 8/2 = **4.0000**

La derivada exacta de x² es 2x → f'(2) = 4 ✓

**Resultado:** `3 Puntos f'(2) = 4.0000`
