# Acumulación de Errores en Bucles

from decimal import Decimal

iteraciones = 1000000
incremento = 0.1

# 1. Acumulación usando float
suma_float = 0.0
for i in range(iteraciones):
    suma_float += incremento

esperado = iteraciones * incremento

print("--- Acumulación en Bucle (1,000,000 de iteraciones) ---")
print(f"Resultado esperado: {esperado:.17f}")
print(f"Resultado float:    {suma_float:.17f}")
print(f"Diferencia (Error): {suma_float - esperado:.17f}")

# 2. Solución con Decimal
suma_decimal = Decimal("0.0")
incremento_decimal = Decimal("0.1")
for i in range(iteraciones):
    suma_decimal += incremento_decimal

print("\n--- Solución con Decimal (Alta Precisión) ---")
print(f"Resultado exacto: {suma_decimal}")

# 3. Verificación
if suma_float != esperado:
    print("\nNOTA: El error de float es notable tras un millón de sumas.")