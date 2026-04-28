# Regla de Simpson 1/3

## Definición
La Regla de Simpson 1/3 es un método de integración numérica que aproxima 
la integral de una función usando polinomios de segundo grado (parábolas).

## Fórmula
∫[a,b] f(x) dx ≈ (h/3) [f(x₀) + 4f(x₁) + 2f(x₂) + ... + 4f(xₙ₋₁) + f(xₙ)]

Donde:
- h = (b - a) / n
- n debe ser un número par

## Ejemplo
∫[0,2] √(1 + x²/4) dx, n = 8

## Requisitos
- Python 3.x
- NumPy

## Uso
```bash
python codigo.py
```