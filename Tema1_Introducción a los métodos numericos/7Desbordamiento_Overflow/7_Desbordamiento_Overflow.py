# Desbordamiento (Overflow) en Punto Flotante

import math
import sys

# Valor máximo de float64
maximo = sys.float_info.max

print(f"Valor máximo de float64: {maximo}")

# Operación que provoca overflow
resultado = maximo * 2

print(f"Resultado después del overflow: {resultado}")

# Verificación
if math.isinf(resultado):
    print("ERROR: Overflow detectado (infinito)")