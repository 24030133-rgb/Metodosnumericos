import numpy as np 

def resolver_2x2_paso_a_paso(A, B): 
    # PASO 1: Matriz Aumentada 
    Ab = np.hstack((A.astype(float), B.reshape(-1, 1).astype(float))) 
    n = len(B) 

    print("--- PASO 1: Matriz Aumentada Inicial ---") 
    print(Ab) 

    for i in range(n): 

        # PASO 2: Pivoteo (mejorado)
        if abs(Ab[i, i]) < 1e-10: 
            print(f"Pivote en [{i},{i}] es cero. Buscando intercambio...") 
            max_row = np.argmax(np.abs(Ab[i:, i])) + i 

            if abs(Ab[max_row, i]) < 1e-10:
                raise ValueError("El sistema no tiene solución única.")

            Ab[[i, max_row]] = Ab[[max_row, i]] 

            print("Matriz después del intercambio de filas:") 
            print(Ab) 

        # Validar pivote
        pivote = Ab[i, i] 

        # PASO 3: Normalización 
        Ab[i] = Ab[i] / pivote 
        print(f"PASO 3: Fila {i+1} normalizada (Pivote = 1):") 
        print(Ab) 

        # PASO 4: Eliminación 
        for j in range(n): 
            if i != j: 
                factor = Ab[j, i] 
                Ab[j] = Ab[j] - factor * Ab[i] 

                print(f"PASO 4: Eliminando elemento en [{j},{i}] usando factor {factor:.4f}:") 
                print(Ab) 

    # PASO 5: Resultado 
    return Ab[:, -1] 


# Sistema: 2x + y = 5 | x + 3y = 10 
A_2x2 = np.array([[2, 1], 
                  [1, 3]]) 

B_2x2 = np.array([5, 10]) 

# Ejecución 
try:
    soluciones = resolver_2x2_paso_a_paso(A_2x2, B_2x2) 

    print("\n" + "="*30) 
    print("Resultado final:")
    print(f"x ≈ {soluciones[0]:.3f}") 
    print(f"y ≈ {soluciones[1]:.3f}") 
    print("="*30)

except ValueError as e:
    print("\nError:", e)