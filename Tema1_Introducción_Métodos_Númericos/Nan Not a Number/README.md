# NaN (Not a Number)

## Definición
`NaN` es un valor especial del estándar **IEEE 754** que representa un resultado
matemáticamente indefinido o imposible. A diferencia del overflow, no indica un
número demasiado grande sino una operación **sin resultado válido**. Su característica
más peligrosa es que se **propaga silenciosamente**: cualquier operación con NaN
devuelve NaN, y además `NaN != NaN` es siempre `True`, lo que hace que las
comparaciones directas fallen.


## Fórmula

Operaciones que generan NaN:

0.0 / 0.0   →  NaN
sqrt(−1)    →  NaN
inf − inf   →  NaN
inf × 0     →  NaN

Propiedad única de NaN:

NaN == NaN  →  False  (es el único valor que no es igual a sí mismo)

Detección correcta:

math.isnan(valor)  →  True si el valor es NaN


## Algoritmo
Realizar una operación matemáticamente inválida
Observar que el resultado es `nan`
Intentar comparar con `==` y observar que falla
Detectar correctamente con `math.isnan()`
Identificar el origen del NaN
Aplicar validación previa o manejo de excepción


## Ejemplo y Caso de Prueba

**Caso 1:** operaciones que producen NaN

| Operación         | Resultado | ¿isnan()? | Causa                        |
|-------------------|-----------|-----------|------------------------------|
| 0.0 / 0.0         | nan       | True      | Indeterminación 0/0          |
| sqrt(−1)          | nan       | True      | Raíz de número negativo      |
| inf − inf         | nan       | True      | Indeterminación ∞ − ∞        |
| inf × 0           | nan       | True      | Indeterminación ∞ × 0        |

**Caso 2:** propagación y comparación de NaN

| Operación           | Resultado | Observación                   |
|---------------------|-----------|-------------------------------|
| nan + 5.0           | nan       | Se propaga en suma            |
| nan * 100           | nan       | Se propaga en multiplicación  |
| nan == nan          | False     | No se puede comparar con ==   |
| math.isnan(nan)     | True      | Única forma correcta          |

**Resultado del caso principal:**
- Entrada: `math.sqrt(-1)`
- Resultado: `nan`
- ¿Es NaN?: `True`
- `nan == nan` devuelve `False`: nunca comparar NaN con `==`