# Cuadratura Gaussiana

## Definición
Es un método de integración numérica que elige 
de forma inteligente los puntos donde evalúa la función, a diferencia 
de otros métodos que usan puntos igualmente espaciados. Estos puntos 
se llaman **nodos de Gauss** y tienen pesos asociados que maximizan 
la precisión del resultado.

Con solo 2 puntos puede integrar exactamente polinomios de hasta grado 3,
lo que la hace muy eficiente.


## Fórmula

Para 2 puntos en el intervalo [-1, 1]:

∫[-1,1] f(x) dx ≈ f(-1/√3) + f(1/√3)

Para un intervalo general [a, b] se hace un cambio de variable:

∫[a,b] f(x) dx ≈ ((b-a)/2) * [f(x₁) + f(x₂)]

Donde los nodos transformados son:
- x₁ = ((b-a)/2) * (-1/√3) + (a+b)/2
- x₂ = ((b-a)/2) * (1/√3)  + (a+b)/2



## Algoritmo
Definir la función f(x)
Definir el limite inferior a
Definir el limite inferior b
Realizar cambio de variable
Definir puntos
Definir peso
Sustituir cada t en la formula del cambio
Evaluar la funcion en los puntos f(x1), f(x2)
Aplicar la fórmula de Gauss
Obtener el resultado 


---

## Ejemplo y Caso de Prueba

**Integral:** ∫[-1,1] (x² + 3x + 2) dx,  con 2 puntos de Gauss

| Nodo | t      | x (transformado) | f(x)   | Peso |
|------|--------|------------------|--------|------|
| 1    | -0.5774 | -0.5774         | 0.6667 | 1    |
| 2    |  0.5774 |  0.5774         | 4.0000 | 1    |

**Resultado:** `Cuadratura Gaussiana ≈ 4.6667`


