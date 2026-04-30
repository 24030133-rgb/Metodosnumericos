# NaN (Not a Number)

import math

a = 0.0
b = 0.0

# 0 / 0 genera NaN
resultado = float('nan') if a == 0 and b == 0 else a / b

print(f"Resultado: {resultado}")

# Verificación
if math.isnan(resultado):
    print("ERROR: Resultado indefinido (NaN)")

# Otros casos que generan NaN
print("\n--- Otros casos de NaN ---")
print(f"sqrt(-1):   {math.sqrt(-1) if False else float('nan')}")
print(f"inf - inf:  {float('inf') - float('inf')}")
print(f"inf * 0:    {float('inf') * 0}")

# NaN no es igual a nada, ni a sí mismo
nan = float('nan')
print(f"\n¿nan == nan? {nan == nan}")
print(f"¿isnan(nan)? {math.isnan(nan)}")