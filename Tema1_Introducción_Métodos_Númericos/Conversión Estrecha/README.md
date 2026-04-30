# Conversión Estrecha (Narrowing Primitive Conversion)

## Definición
Ocurre cuando se convierte un valor de un tipo de dato de **mayor precisión a uno
de menor precisión**. Al reducir el tamaño del tipo, se pierden bits y por lo tanto
información, generando errores, truncamientos o desbordamientos inesperados en el
resultado.


## Fórmula

Pérdida de datos:

Pérdida = |valor_original - valor_convertido|

Rangos de precisión por tipo:

| Tipo   | Bits | Rango aproximado               | Dígitos decimales |
|--------|------|--------------------------------|-------------------|
| double | 64   | ±1.7 × 10³⁰⁸                   | 15–17             |
| float  | 32   | ±3.4 × 10³⁸                    | 6–7               |
| int    | 32   | −2,147,483,648 a 2,147,483,647 | exacto            |
| byte   | 8    | −128 a 127                     | exacto            |


## Algoritmo
Definir un número con alta precisión (double o float)
Convertirlo explícitamente a un tipo de menor precisión
Observar la pérdida de dígitos o el desbordamiento
Calcular la pérdida: `|valor_original - valor_convertido|`
Calcular el error relativo respecto al valor original
Comparar resultados entre tipos


## Ejemplo y Caso de Prueba

**Caso 1:** pérdida de dígitos por reducción de tipo

| Conversión       | Valor original            | Valor convertido    | Pérdida            |
|------------------|---------------------------|---------------------|--------------------|
| double → float   | 1234567890.123456789      | 1234567936.0        | ≈ 45.876           |
| double → float   | 3.141592653589793         | 3.1415927           | ≈ 3.2 × 10⁻⁸       |
| double → float   | 0.000000123456789         | 0.00000012345679    | ≈ 1.0 × 10⁻¹⁷      |

**Caso 2:** desbordamiento por conversión a tipo entero

| Conversión   | Valor original | Valor convertido | Resultado   |
|--------------|----------------|------------------|-------------|
| int → byte   | 130            | (byte) 130       | -126        |
| int → byte   | 200            | (byte) 200       | -56         |
| float → int  | 9.99           | (int) 9.99       | 9 (trunca)  |

**Resultado del caso principal:**
- Entrada: `1234567890.123456789` (double)
- Convertido a float: `1234567936.0`
- Pérdida absoluta: `≈ 45.876`
- Los últimos dígitos se distorsionan porque float solo tiene 7 dígitos de precisión