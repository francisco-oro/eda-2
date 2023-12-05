def imprimir_matriz35(matriz):
    for fila in matriz:
        print(fila)

def calcular_transpuesta35(matriz):
    # Calcular la transpuesta de la matriz
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

def calcular_adjunta35(matriz):
    # Calcular la matriz adjunta
    transpuesta = calcular_transpuesta35(matriz)
    cofactores = []

    for i in range(len(matriz)):
        fila_cofactores = []
        for j in range(len(transpuesta[0])):
            submatriz = [fila[:j] + fila[j + 1:] for fila in (matriz[:i] + matriz[i + 1:])]
            signo = (-1) ** (i + j)
            cofactor = signo * calcular_determinante35(submatriz)
            fila_cofactores.append(cofactor)
        cofactores.append(fila_cofactores)

    return calcular_transpuesta35(cofactores)

def calcular_determinante35(matriz):
    # Calcular el determinante de una matriz recursivamente
            
    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    determinante = 0
    for c in range(len(matriz)):
        submatriz = [fila[1:] for fila in (matriz[:c] + matriz[c + 1:])]
        signo = (-1) ** c
        determinante += signo * matriz[c][0] * calcular_determinante35(submatriz)
    return determinante

def calcular_inversa35(matriz,n):
    determinante = calcular_determinante35(matriz)
    if determinante == 0:
        return None  # La matriz no tiene inversa
    if(n==2):
        inversa = [[matriz[1][1] / determinante, -matriz[0][1] / determinante],
                   [-matriz[1][0] / determinante, matriz[0][0] / determinante]]
        return inversa
    adjunta = calcular_adjunta35(matriz)
    inversa = [[elemento / determinante for elemento in fila] for fila in adjunta]
    return inversa


