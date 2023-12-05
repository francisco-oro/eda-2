def traspuesta():
    print("\nMatriz Transpuesta")
    print("==================")
    print("\n-Orden de la matriz-")
    n = int(input("Ingrese el número de Filas: "))
    m = int(input("Ingrese el número de columnas: "))

    if(n > 0 and m > 0):
        print("\n-Llene la matriz-")
        matriz = []
        for i in range(n):
            fila = []
            for j in range(m):
                elemento = int(input(f"Ingresa el elemento [{i+1},{j+1}]: "))
                fila.append(elemento)
            matriz.append(fila)
        
        print("\nMatriz original:")
        for fila in matriz:
            print(fila)
        
        matrizTranspuesta = []
        for i in range(len(matriz[0])):
            matrizTranspuesta.append([])
            for j in range(len(matriz)):
                matrizTranspuesta[i].append(matriz[j][i])

        print("\nMatriz Transpuesta:")
        for fila in matrizTranspuesta:
            print(fila)
        print("\n")

    else:
        print("Orden de la matriz no válido")
