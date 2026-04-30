# Error de Redondeo Binario

## Definición
Es el error que ocurre cuando un número decimal **no puede representarse exactamente**
en sistema binario (base 2), generando una pequeña diferencia entre el valor real
y el valor almacenado en memoria. Este fenómeno es inherente al estándar IEEE 754
de punto flotante usado por la mayoría de los lenguajes de programación.


## Fórmula

Error absoluto:

|valor_real - valor_aproximado|

Error relativo:

|valor_real - valor_aproximado| / |valor_real|


## Algoritmo
Tomar un número decimal
Convertirlo a representación binaria (float IEEE 754)
Reconvertir a decimal
Calcular la diferencia entre el valor original y el recuperado
Aplicar la fórmula de error absoluto
Aplicar la fórmula de error relativo
Obtener los resultados


## Ejemplo y Caso de Prueba

**Operación:** `0.1 + 0.2` en Python

| Número | Valor real | Valor en float       | Error absoluto         |
|--------|------------|----------------------|------------------------|
| 0.1    | 0.1        | 0.1000000000000000055| ≈ 5.55 × 10⁻¹⁸        |
| 0.2    | 0.2        | 0.2000000000000000111| ≈ 1.11 × 10⁻¹⁷        |
| 0.3    | 0.3        | 0.2999999999999999889| ≈ 1.11 × 10⁻¹⁷        |

**Resultado:**
- Esperado: `0.3`
- Resultado real: `0.30000000000000004`
- Error absoluto: `|0.3 - 0.30000000000000004|` = `4 × 10⁻¹⁷`