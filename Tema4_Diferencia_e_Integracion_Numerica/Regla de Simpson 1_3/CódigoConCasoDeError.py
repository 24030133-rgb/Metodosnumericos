# SIMPSON 1/3 - CASO DE ERROR 

def simpson_13(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n debe ser par para Simpson 1/3")
    
    h = (b - a) / n
    suma = f(a) + f(b)
    
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            suma += 2 * f(x)
        else:
            suma += 4 * f(x)
    
    return (h / 3) * suma



try:
    f_err = lambda x: x**2 + 1
    resultado = simpson_13(f_err, 0, 5, 3)
    print("Resultado:", resultado)
except ValueError as e:
    print(f"Error Simpson 1/3: {e}")