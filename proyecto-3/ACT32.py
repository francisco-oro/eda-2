def ingresar_matriz():
    filas = int(input("\nNúmero de filas: "))
    columnas = int(input("Número de columnas: "))
    matriz = []

    print("\n")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = int(input(f"Ingrese el elemento en la posición [{i}, {j}]: "))
            fila.append(elemento)
        matriz.append(fila)

    return matriz

def calcular_determinante(matriz):
    n = len(matriz)
    # Cuando se trata de una Matriz 1x1
    if n == 1:
        return matriz[0][0]
    # En el caso de una Matriz 2x2
    if n == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    # Matriz de 3x3 en adelante (regla de Laplace)    
    determinante = 0
    for j in range(n):
        cofactor = matriz[0][j] * (-1) ** j * calcular_determinante(obtener_submatriz(matriz, 0, j))
        determinante += cofactor

    return determinante

def obtener_submatriz(matriz, fila, columna):
    return [fila[:columna] + fila[columna+1:] for fila in (matriz[:fila] + matriz[fila+1:])]
    
def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")
        print()