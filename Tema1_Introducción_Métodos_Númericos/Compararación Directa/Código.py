# Comparación Directa con ==

# 1. El Problema: Error de redondeo en punto flotante
a = 0.1 + 0.1 + 0.1
b = 0.3

print(f"Valor de a (0.1 * 3): {a:.17f}")
print(f"Valor de b:            {b:.17f}")

# 2. Comparación directa con == (FALLARÁ)
print("\n--- Comparación con '==' ---")
if a == b:
    print("Resultado: Son iguales")
else:
    print("Resultado: SON DIFERENTES (Error esperado)")

# 3. Solución: Comparación con Epsilon
epsilon = 0.00001
print(f"\nComparación con Epsilon ({epsilon})")
if abs(a - b) < epsilon:
    print("Resultado: Son iguales (dentro del margen de error)")
else:
    print("Resultado: Son diferentes")