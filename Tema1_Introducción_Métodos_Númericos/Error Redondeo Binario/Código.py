# Error de Redondeo Binario

a = 0.1
b = 0.2
resultado = a + b

print(f"0.1 + 0.2 = {resultado:.17f}")
print(f"¿Es igual a 0.3? {resultado == 0.3}")
print(f"Error: {abs(0.3 - resultado)}")