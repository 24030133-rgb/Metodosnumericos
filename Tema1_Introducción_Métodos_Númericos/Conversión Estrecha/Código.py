# Conversión Estrecha (Narrowing Primitive Conversion)

import numpy as np

# Un número muy grande en double
valor_double = 3.14159e10

# Conversión a int (truncamiento)
valor_int = int(valor_double)

print("--- Conversión double a int ---")
print(f"Valor Original (double): {valor_double}")
print(f"Valor Truncado (int):    {valor_int}")
print(f"Pérdida de información:  {valor_double - valor_int}")

# Conversión double a float32 (menor precisión)
valor_float32 = np.float32(valor_double)

print("\n--- Conversión double a float32 ---")
print(f"Valor double:  {valor_double:.20f}")
print(f"Valor float32: {valor_float32:.20f}")
print(f"Error:         {abs(valor_double - valor_float32)}")