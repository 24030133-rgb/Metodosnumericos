import numpy as np 

def gauss_jordan_corto(A, B): 
    Ab = np.hstack([A.astype(float), B.reshape(-1, 1).astype(float)]) 
    n = len(B) 

    for i in range(n): 
        idx_max = i + np.argmax(np.abs(Ab[i:, i]))

        if abs(Ab[idx_max, i]) < 1e-10:
            raise ValueError("El sistema no tiene solución única")

        if idx_max != i:
            Ab[[i, idx_max]] = Ab[[idx_max, i]]

        Ab[i] = Ab[i] / Ab[i, i] 

        for j in range(n): 
            if i != j: 
                Ab[j] -= Ab[j, i] * Ab[i] 

    return Ab[:, -1] 


# PRUEBA
A = np.array([[2, -1, 1], 
              [1,  1, 2], 
              [3, -1, -1]]) 

B = np.array([2, 9, -2]) 

try:
    sol = gauss_jordan_corto(A, B)

    print("\nResultado del sistema:")
    print(f"x ≈ {sol[0]:.3f}")
    print(f"y ≈ {sol[1]:.3f}")
    print(f"z ≈ {sol[2]:.3f}")

    print("\n(Valores aproximados)")

except ValueError as e:
    print("Error:", e)