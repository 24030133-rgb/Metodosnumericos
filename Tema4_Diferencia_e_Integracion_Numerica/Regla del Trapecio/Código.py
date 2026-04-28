# REGLA DEL TRAPECIO 
def trapecio(f, a, b):
    return ((b - a) / 2) * (f(a) + f(b))

f2 = lambda x: x**2 + 2*x
resultado2 = trapecio(f2, 0, 4)
print(f"Trapecio: {resultado2:.4f}")