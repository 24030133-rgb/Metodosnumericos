import numpy as np 

# PASO 1: Definir matrices 
A = np.array([ 
    [1, 1, 1, 1], 
    [2, 3, 1, 5], 
    [-1, 1, -1, 1], 
    [3, 1, 2, 4] 
], dtype=float) 

B = np.array([10, 31, -2, 28], dtype=float) 

def resolver_gauss_jordan_4x4(A, B): 
    # 🔹 Copias para no modificar originales
    Ab = np.hstack((A.copy(), B.reshape(-1, 1).copy())) 
    n = len(B) 

    print("--- MATRIZ AUMENTADA INICIAL 4x4 ---") 
    print(Ab, "\n") 

    for i in range(n): 

        # 🔹 PIVOTEO (mejorado)
        max_row = np.argmax(np.abs(Ab[i:, i])) + i
        if abs(Ab[max_row, i]) < 1e-10:
            raise ValueError("El sistema no tiene solución única.")

        if max_row != i:
            Ab[[i, max_row]] = Ab[[max_row, i]]
            print(f"Intercambio fila {i+1} con fila {max_row+1}")
            print(Ab, "\n")

        # 🔹 NORMALIZACIÓN
        pivote = Ab[i, i]
        Ab[i] = Ab[i] / pivote 

        # 🔹 ELIMINACIÓN
        for j in range(n): 
            if i != j: 
                factor = Ab[j, i] 
                Ab[j] = Ab[j] - factor * Ab[i] 

        print(f"Columna {i+1} procesada:") 
        print(Ab.round(2), "\n") 

    return Ab[:, -1] 


# Ejecución 
soluciones = resolver_gauss_jordan_4x4(A, B) 

print("--- SOLUCIONES DIRECTAS ---") 
variables = ['x', 'y', 'z', 'w'] 
for var, val in zip(variables, soluciones): 
    print(f"{var} = {val:.4f}")