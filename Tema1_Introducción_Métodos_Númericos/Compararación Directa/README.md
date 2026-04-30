# Comparación Directa con ==

## Definición
Es un error común en programación que ocurre al comparar números de **punto flotante**
usando el operador `==`. Debido al error de redondeo binario, dos valores que
matemáticamente deberían ser iguales pueden diferir en los últimos bits de su
representación IEEE 754, haciendo que `==` devuelva `False` de forma inesperada.


## Fórmula

Comparación incorrecta:

a == b

Comparación correcta con tolerancia epsilon:

|a - b| < ε

Donde **ε (epsilon)** es una tolerancia pequeña adecuada al contexto, por ejemplo:
- ε = 1×10⁻⁹  → uso general
- ε = 1×10⁻⁶  → cálculos científicos menos estrictos
- ε = 2.2×10⁻¹⁶ → epsilon de máquina (máxima precisión double)


## Algoritmo
Calcular dos valores que matemáticamente deberían ser iguales
Compararlos con `==` y registrar el resultado
Observar que el resultado es incorrecto (`False`)
Definir un valor de tolerancia epsilon adecuado
Aplicar la comparación `|a - b| < ε`
Verificar que el resultado ahora es correcto (`True`)
Calcular el error absoluto real entre ambos valores


## Ejemplo y Caso de Prueba

**Operación:** comparar `0.1 + 0.2` con `0.3`

| Operación             | Valor obtenido      | Comparación `==` | `\|a-b\|`      | `\|a-b\| < 1e-9` |
|-----------------------|---------------------|------------------|----------------|------------------|
| 0.1 + 0.2 vs 0.3      | 0.30000000000000004 | False            | 5.55 × 10⁻¹⁷   | True             |
| 0.1 * 3 vs 0.3        | 0.30000000000000004 | False            | 5.55 × 10⁻¹⁷   | True             |
| 1.0 / 3.0 * 3 vs 1.0  | 1.0                 | True             | 0.0            | True             |
| sqrt(2)**2 vs 2.0     | 2.0000000000000004  | False            | 4.44 × 10⁻¹⁶   | True             |

**Resultado del caso principal:**
- Entrada: `a = 0.1 + 0.2`, `b = 0.3`
- Comparación `==`: **False** (incorrecto)
- Error absoluto: `|a - b|` = `5.55 × 10⁻¹⁷`
- Comparación con epsilon (`1e-9`): **True** (correcto)