# Pérdida de Precisión por Magnitud (IEEE 754)

import decimal

# --- Demostración de Pérdida de Precisión ---
numero_grande = 1.0e16
numero_pequeno = 1.0
resultado = numero_grande + numero_pequeno

print("--- Demostración de Pérdida de Precisión ---")
print(f"Número Grande: {numero_grande:.4f}")
print(f"Número Pequeño: {numero_pequeno:.4f}")
print(f"Suma Resultante: {resultado:.4f}")

if resultado == numero_grande:
    print("\nRESULTADO: El número pequeño 'desapareció'.")
    print("Faltan bits en la mantisa para representarlo.")

# --- Solución con Mayor Precisión ---
decimal.getcontext().prec = 20

bd_grande = decimal.Decimal("1.0e16")
bd_pequeno = decimal.Decimal("1.0")
bd_resultado = bd_grande + bd_pequeno

print("\n--- Solución con Mayor Precisión ---")
print(f"Suma Exacta: {float(bd_resultado):.4f}")