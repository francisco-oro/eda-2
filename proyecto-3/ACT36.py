def representacion_matricial(matriz_coeficientes, matriz_terminos_independientes):
    for i in range(3):
        print(f"Ingresa los datos de la ecuacion {i+1}: ")

        matriz_coeficientes[i][0] = int(input("Ingresa el coeficiente de x: "))
        matriz_coeficientes[i][1] = int(input("Ingresa el coeficiente de y: "))
        matriz_coeficientes[i][2] = int(input("Ingresa el coeficiente de z: "))

        matriz_terminos_independientes[i][0] = int(input("Ingresa el termino independiente: "))
        print("\n")
    
def calcular_determinante(M):
    pt1 = M["a"] * ((M["e"] * M["i"]) - (M["h"] * M["f"]))
    pt2 = M["b"] * ((M["i"] * M["d"]) - (M["g"] * M["f"]))
    pt3 = M["c"] * ((M["d"] * M["h"]) - (M["g"] * M["e"]))
    return pt1 - pt2 + pt3

def obtener_matriz_cofactores(M):
    C11 = (M["e"] * M["i"]) - (M["h"] * M["f"])
    C12 = -1*((M["d"] * M["i"]) - (M["g"] * M["f"]))
    C13 = (M["d"] * M["h"]) - (M["g"] * M["e"])

    C21 = -1*((M["b"] * M["i"]) - (M["h"] * M["c"]))
    C22 = (M["a"] * M["i"]) - (M["g"] * M["c"]) 
    C23 = -1*((M["a"] * M["h"]) - (M["g"] * M["b"]))

    C31 = (M["b"] * M["f"]) - (M["e"] * M["c"])
    C32 = -1*((M["a"] * M["f"]) - (M["d" ] * M["c"]))
    C33 = (M["a"] * M["e"]) - (M["d"] * M["b"])

    return [[C11, C12, C13],[C21, C22, C23],[C31,C32, C33]]

def obtener_adjunta(matriz_cofactores):
    matriz_adjunta = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            matriz_adjunta[i][j] = matriz_cofactores[j][i]

    return matriz_adjunta

def obtener_inversa(matriz_adjunta, det):
    if det > 0:
        for i in range(3):
            for j in range(3):
                matriz_adjunta[i][j] *= (1/det)
        
        return matriz_adjunta
    else:
        print("La matriz no tiene inversa.")
        print("Por lo tanto no se puede resolver con este metodo.\n")

def multiplicar_matrices(matriz1, matriz2):
    resultado = [[0], [0], [0]]
    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    
    return resultado



def main():
    #Matriz de coeficientes y termiinos independientes vacias
    matriz_coeficientes = [[0,0,0],[0,0,0],[0,0,0]]
    matriz_terminos_independientes = [[0],[0],[0]]  

    #Paso 1 (Representacion matricial del sistema de ecuaciones)
    representacion_matricial(matriz_coeficientes, matriz_terminos_independientes)
    elementos_matriz = {
        "a": matriz_coeficientes[0][0],
        "b": matriz_coeficientes[0][1],
        "c": matriz_coeficientes[0][2],
        "d": matriz_coeficientes[1][0],
        "e": matriz_coeficientes[1][1],
        "f": matriz_coeficientes[1][2],
        "g": matriz_coeficientes[2][0],
        "h": matriz_coeficientes[2][1],
        "i": matriz_coeficientes[2][2]
    }

    #Paso 2 (Calcular determinante)
    det = calcular_determinante(elementos_matriz)

    #Paso 3(Obetner matriz)
    matriz_cofactores = obtener_matriz_cofactores(elementos_matriz)

    #Paso 4(Obtener matriz adjunta)
    matriz_adjunta = obtener_adjunta(matriz_cofactores)

    #Paso 5(Obtener matriz inversa)
    matriz_inversa = obtener_inversa(matriz_adjunta, det)

    #Paso 6(Muntiplicar A^-1 * X)
    resultado = multiplicar_matrices(matriz_inversa, matriz_terminos_independientes)

    print("Resultados:")
    print(f"x = {resultado[0][0]}")
    print(f"y = {resultado[1][0]}")
    print(f"z = {resultado[2][0]}")

    print("\n")