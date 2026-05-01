import numpy as np 

def resolver_3x3_paso_a_paso(A, B): 
    # PASO 1: Matriz Aumentada 
    Ab = np.hstack((A.astype(float), B.reshape(-1, 1).astype(float))) 
    n = len(B) 

    print("--- MATRIZ AUMENTADA INICIAL ---") 
    print(Ab) 

    for i in range(n): 
        print(f"\n=== PROCESANDO COLUMNA {i+1} ===") 

        # PASO 2: Pivoteo (mejorado)
        max_row = i + np.argmax(np.abs(Ab[i:, i]))
        
        if abs(Ab[max_row, i]) < 1e-10:
            raise ValueError("El sistema no tiene solución única.")

        if max_row != i:
            Ab[[i, max_row]] = Ab[[max_row, i]]
            print(f"PASO 2: Intercambio de fila {i+1} con fila {max_row+1}") 
            print(Ab) 

        # PASO 3: Normalización 
        pivote = Ab[i, i]
        Ab[i] = Ab[i] / pivote 
        print(f"PASO 3: Fila {i+1} normalizada (Pivote = 1):") 
        print(Ab.round(2)) 

        # PASO 4: Eliminación 
        for j in range(n): 
            if i != j: 
                factor = Ab[j, i] 
                Ab[j] = Ab[j] - factor * Ab[i] 
                print(f"PASO 4: Eliminando elemento en [{j},{i}] (factor = {factor:.2f})") 
                print(Ab.round(2)) 

    # PASO 5: Resultado 
    return Ab[:, -1] 


# Datos del sistema 
A_3x3 = np.array([ 
    [3, 2, -1], 
    [2, -2, 4], 
    [-1, 0.5, -1] 
]) 

B_3x3 = np.array([1, -2, 0]) 

# Ejecución 
try:
    soluciones = resolver_3x3_paso_a_paso(A_3x3, B_3x3) 

    print("\n" + "="*35) 
    print("--- SOLUCIONES DIRECTAS (3x3) ---") 
    print(f"x = {soluciones[0]:.2f}") 
    print(f"y = {soluciones[1]:.2f}") 
    print(f"z = {soluciones[2]:.2f}") 
    print("="*35)

except ValueError as e:
    print("\nError:", e)