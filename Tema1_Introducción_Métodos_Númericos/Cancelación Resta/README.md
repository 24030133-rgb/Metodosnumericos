# Cancelación por Resta (Loss of Significance)

## Definición
Ocurre cuando se restan dos números de punto flotante **muy cercanos entre sí**.
Los dígitos significativos del resultado se cancelan mutuamente, dejando solo los
bits menos significativos (más ruidosos) y amplificando el **error relativo** de
forma drástica. El resultado puede perder varios dígitos de precisión o volverse
completamente incorrecto.


## Fórmula

Si `a ≈ b`, la resta directa es inestable:

a - b  →  pérdida de dígitos significativos

El error relativo se amplifica según:

Error_relativo(a - b) ≈ Error_absoluto / |a - b|

Cuando `|a - b|` es muy pequeño, el error relativo crece sin límite.

**Solución:** reformular algebraicamente para evitar la resta directa.

Ejemplo con la fórmula cuadrática:

Forma inestable:  x = (-b + sqrt(b² - 4ac)) / 2a

Forma estable:    x = -2c / (b + sqrt(b² - 4ac))


## Algoritmo
Tomar dos números muy cercanos entre sí
Restarlos directamente con `float`
Calcular el resultado esperado con `Decimal`
Calcular el error absoluto y relativo entre ambos
Reformular la expresión algebraicamente para evitar la resta
Evaluar la forma estable y comparar con la inestable
Observar la recuperación de dígitos significativos


## Ejemplo y Caso de Prueba

**Caso 1:** resta directa de números cercanos

| Operación                    | Esperado    | float       | Decimal     |
|------------------------------|-------------|-------------|-------------|
| 1234567890.1234567 − 1234567890.1234560    | 7×10⁻⁷ | 0.0    | 7×10⁻⁷     |
| 1.000000001 − 1.000000000    | 1.0×10⁻⁹    | 9.99×10⁻¹⁰ | 1.0×10⁻⁹   |
| 1.0000001 − 1.0000000        | 1.0×10⁻⁷    | 1.0×10⁻⁷   | 1.0×10⁻⁷   |

**Caso 2:** raíces de `x² - 10000x + 1 = 0`

| Raíz | Forma inestable  | Forma estable    | Error inestable |
|------|------------------|------------------|-----------------|
| x₁   | 9999.9999        | 9999.9999000100  | ≈ 0%            |
| x₂   | 0.0              | 0.00010000000100 | ≈ 100%          |

**Resultado del caso principal:**
- Entrada: `a = 1234567890.1234567`, `b = 1234567890.1234560`
- Resultado float: `0.0` (cancelación total)
- Resultado Decimal: `0.0000007` (exacto)
- La raíz x₂ con forma inestable da `0.0`, con forma estable se recupera correctamente