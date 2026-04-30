# Desbordamiento (Overflow) en Punto Flotante

## Definición
Ocurre cuando el resultado de una operación **excede el valor máximo representable**
por el tipo de dato. En Python con `float64`, el resultado no genera una excepción
sino que se convierte en `inf` (infinito), un valor especial IEEE 754 que puede
propagarse silenciosamente en cálculos posteriores y corromper resultados sin avisar.


## Fórmula

Límites del tipo `float64`:

Máximo positivo:  +1.7976931348623157 × 10³⁰⁸
Mínimo negativo:  −1.7976931348623157 × 10³⁰⁸

Condición de overflow:

Si resultado >  máximo  →  +inf
Si resultado < -máximo  →  -inf

Detección:

import math
math.isinf(valor)  →  True si hay overflow


## Algoritmo
Definir un número muy grande cercano al límite de `float64`
Realizar operaciones que incrementen su magnitud progresivamente
Detectar en qué iteración el valor se convierte en `inf`
Verificar con `math.isinf()` o `numpy.isinf()`
Calcular el error: `inf - valor_esperado` es indefinido
Aplicar manejo del overflow (saturación, excepción o escala)


## Ejemplo y Caso de Prueba

**Caso 1:** valores que producen overflow directo

| Operación         | Valor ingresado | Resultado   | ¿Es inf? |
|-------------------|-----------------|-------------|----------|
| float(1.8e308)    | 1.8 × 10³⁰⁸    | inf         | True     |
| 1.8e308 * 2       | 3.6 × 10³⁰⁸    | inf         | True     |
| 1.7e308 * 1.0     | 1.7 × 10³⁰⁸    | 1.7e308     | False    |
| -1.8e308          | −1.8 × 10³⁰⁸   | -inf        | True     |

**Caso 2:** punto exacto de overflow por multiplicación progresiva

| Iteración | Operación          | Resultado        | ¿Overflow? |
|-----------|--------------------|------------------|------------|
| 1         | 1e300 × 10         | 1.0 × 10³⁰¹      | False      |
| 2         | 1e300 × 100        | 1.0 × 10³⁰²      | False      |
| 7         | 1e300 × 10⁷        | 1.0 × 10³⁰⁷      | False      |
| 8         | 1e300 × 10⁸        | 1.0 × 10³⁰⁸      | False      |
| 9         | 1e300 × 10⁹        | inf              | True       |

**Resultado del caso principal:**
- Entrada: `1.8e308`
- Resultado: `inf`
- ¿Es infinito?: `True`
- El overflow ocurre silenciosamente: no lanza excepción en Python