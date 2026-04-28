# Regla de los 5 Puntos

## Definición
La Regla de los 5 Puntos es un método de diferenciación numérica que
aproxima la derivada de una función usando cinco valores de la función.
Al usar más puntos que la regla de 3 puntos, logra mayor precisión en
la aproximación. Toma dos puntos a la izquierda y dos a la derecha del
punto de interés, lo que reduce significativamente el error de aproximación.

---

## Fórmula

f'(x) ≈ (-f(x+2h) + 8f(x+h) - 8f(x-h) + f(x-2h)) / (12h)

Donde:
- f'(x)    →  derivada aproximada en el punto x
- h        →  tamaño del paso
- f(x+2h)  →  valor de la función dos pasos a la derecha
- f(x+h)   →  valor de la función un paso a la derecha
- f(x-h)   →  valor de la función un paso a la izquierda
- f(x-2h)  →  valor de la función dos pasos a la izquierda

---

## Algoritmo

Definir funcion f(x)
Punto donde se va a derivar 
Definir el tamaño del paso h
Ubicar los 5 puntos necesarios x−2h, x−h, x x+h, x+2h
Evaluar la función en esos puntos x−2h, x−h, x x+h, x+2h
Sustituir en la formula f'(x) ≈ (-f(x+2h) + 8f(x+h) - 8f(x-h) + f(x-2h)) / (12h)
Realizar las operaciones
Obtener resultado

## Ejemplo y Caso de Prueba

**Función:** f(x) = x²,  en x = 2,  con h = 1

| Punto  | x   | f(x) | Coeficiente |
|--------|-----|------|-------------|
| x-2h   | 0.0 | 0.0  | +1          |
| x-h    | 1.0 | 1.0  | -8          |
| x+h    | 3.0 | 9.0  | +8          |
| x+2h   | 4.0 | 16.0 | -1          |

f'(2) ≈ (-16 + 8*9 - 8*1 + 0) / (12*1) = 48/12 = **4.0000**

La derivada exacta de x² es 2x → f'(2) = 4 ✓

**Resultado:** `5 Puntos f'(2) = 4.0000`

