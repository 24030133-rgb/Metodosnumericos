# Cancelación por Resta (Loss of Significance)

from decimal import Decimal

# Dos números muy grandes y muy cercanos
x = 1234567890.1234567
y = 1234567890.1234560

# El resultado esperado es 0.0000007
resultado = x - y

print("--- Cancelación por Resta ---")
print(f"Resultado float:    {resultado:.20f}")
print("Resultado esperado: 0.00000070000000000000")

# Solución con Decimal (alta precisión)
x_decimal = Decimal("1234567890.1234567")
y_decimal = Decimal("1234567890.1234560")
resultado_decimal = x_decimal - y_decimal

print("\n--- Solución con Decimal ---")
print(f"Resultado exacto: {resultado_decimal}")