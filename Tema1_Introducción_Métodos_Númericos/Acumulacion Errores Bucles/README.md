# Acumulación de Errores en Bucles

## Definición
Es el fenómeno que ocurre cuando se realiza una operación de **punto flotante**
repetidamente en un bucle. Cada iteración introduce un pequeño error de redondeo
que se va sumando al anterior, hasta generar una desviación significativa en el
resultado final respecto al valor matemáticamente esperado.


## Fórmula

Error acumulado:

Error = |Resultado_float - Resultado_esperado|

El error crece aproximadamente proporcional al número de iteraciones:

Error ≈ n × ε_máquina × valor_incremento

Donde **n** es el número de iteraciones y **ε_máquina ≈ 2.2×10⁻¹⁶** para double.

Solución: usar `Decimal` con precisión arbitraria en lugar de `float`.


## Algoritmo
Definir un incremento y un número de iteraciones
Sumar el incremento repetidamente usando `float`
Calcular el valor esperado exacto (incremento × iteraciones)
Calcular el error acumulado: `|resultado_float - esperado|`
Repetir los pasos 2–4 usando `Decimal`
Comparar el error de ambos métodos
Observar cómo crece el error al aumentar las iteraciones


## Ejemplo y Caso de Prueba

**Operación:** sumar `0.1` repetidamente en un bucle

| Iteraciones | Esperado   | Resultado float        | Error float     | Resultado Decimal | Error Decimal |
|-------------|------------|------------------------|-----------------|-------------------|---------------|
| 1,000       | 100.0      | 100.00000000000009     | 9.0 × 10⁻¹⁴    | 100.0             | 0.0           |
| 10,000      | 1,000.0    | 1000.0000000000159     | 1.59 × 10⁻¹¹   | 1000.0            | 0.0           |
| 1,000,000   | 100,000.0  | 100000.00000001328     | 1.33 × 10⁻⁵    | 100000.0          | 0.0           |

**Resultado del caso principal:**
- Entrada: incremento = `0.1`, iteraciones = `1,000,000`
- Esperado: `100000.0`
- Resultado float: `100000.00000001328`
- Error acumulado: `1.3328 × 10⁻⁵`
- Resultado Decimal: `100000.0`
- Error Decimal: `0.0`