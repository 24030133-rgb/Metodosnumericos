# Pérdida de Precisión por Magnitud (IEEE 754)

## Definición
Es el fenómeno que ocurre bajo el estándar **IEEE 754** cuando se operan números de
magnitudes muy diferentes en punto flotante de 64 bits. El número de menor magnitud
puede perder dígitos significativos o **desaparecer completamente**, porque la mantisa
no tiene suficientes bits para representar ambos valores al mismo tiempo.


## Fórmula

Un número flotante de 64 bits (double) se compone de:

- 1 bit de signo
- 11 bits de exponente
- 52 bits de mantisa

Precisión máxima ≈ 15–17 dígitos decimales significativos

El límite de representación exacta de enteros es:

2⁵³ = 9,007,199,254,740,992 ≈ 9 × 10¹⁵

A partir de ese umbral, no todos los enteros consecutivos son representables.


## Algoritmo
Tomar dos números de magnitudes muy diferentes (ej. A = 1×10¹⁶, B = 1.0)
Alinear los exponentes para realizar la operación
Observar que los bits de B quedan fuera de la mantisa de 52 bits
El resultado se redondea y B se pierde
Calcular el error absoluto: |valor_esperado - valor_obtenido|
Calcular el error relativo: |valor_esperado - valor_obtenido| / |valor_esperado|
Obtener los resultados


## Ejemplo y Caso de Prueba

**Operación:** `1e16 + 1.0` en punto flotante de 64 bits

| Operación      | Valor esperado          | Resultado real          | Error absoluto | Error relativo |
|----------------|-------------------------|-------------------------|----------------|----------------|
| 1e16 + 1.0     | 10000000000000001.0     | 10000000000000000.0     | 1.0            | 1 × 10⁻¹⁶     |
| 1e16 + 0.5     | 10000000000000000.5     | 10000000000000000.0     | 0.5            | 5 × 10⁻¹⁷     |
| 1e16 + 100.0   | 10000000000000100.0     | 10000000000000000.0     | 100.0          | 1 × 10⁻¹⁴     |

**Resultado del caso principal:**
- Entrada: `1e16 + 1.0`
- Esperado: `10000000000000001.0`
- Resultado real: `10000000000000000.0`
- El `1.0` **desaparece** porque está por debajo del épsilon de máquina a esa escala