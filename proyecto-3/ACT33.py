import numpy as np

def main33():
# Ingreso manual de la matriz
    n = int(input("Ingrese el tamaño de la matriz cuadrada: "))
    print("\n-----------------------------------------------------------------------")

    print("\n--> Ingrese los elementos de la matriz A:")
    a = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            a[i][j] = float(input(f"Elemento a[{i+1}][{j+1}]: "))

    # Ingreso manual del vector
    print("\n--> Ingrese los elementos del vector B:")
    b = np.zeros(n)
    for i in range(n):
        b[i] = float(input(f"Elemento b[{i+1}]: "))

    d = np.linalg.det(a)

    print("\n-----------------------------------------------------------------------")
    
    if d == 0:
        print("El determinante de la matriz es cero. No se puede resolver el sistema.")
    else:
        x = np.zeros(n)
        for i in range(n):
            ai = a.copy()
            ai[:, i] = b
            x[i] = np.linalg.det(ai) / d

        print("La solución del sistema de ecuaciones es:")
        print(x)

    print("\n-----------------------------------------------------------------------\n")

    