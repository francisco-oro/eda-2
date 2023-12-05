def sumarMatrices():
    print("\n")
    columnasMatriz1 = int(input("Ingresa la cantidad de columnas de la primer matriz: "))
    filasMatriz1 = int(input("Ingresa la cantidad de filas de la primer matriz: "))
    columnasMatriz2 = int(input("Ingresa la cantidad de columnas de la segunda matriz: "))
    filasMatriz2 = int(input("Ingresa la cantidad de filas de la segunda matriz: "))

    if (columnasMatriz1==columnasMatriz2 and filasMatriz1 == filasMatriz2):
        matriz1 = []
        matriz2 = []

        print("\n")
        print("Matriz 1: ")
        for i in range(filasMatriz1):
            fila = []
            for j in range(columnasMatriz1):
                fila.append(int(input(f"Ingrese el valor [{i}][{j}]: ")))
            matriz1.append(fila)

        print("\nMatriz 2: ")
        for i in range(filasMatriz2):
            fila = []
            for j in range(columnasMatriz2):
                fila.append(int(input(f"Ingrese el valor [{i}][{j}]: ")))
            matriz2.append(fila)

        matrizResultante = []
        for i in range(filasMatriz1):
            fila = []
            for j in range(columnasMatriz1):
                fila.append(matriz1[i][j] + matriz2[i][j])
            matrizResultante.append(fila)

        print("\nMatriz 1: ")
        for fila in matriz1:
            print(fila)
        print("\nMatriz 2: ")
        for fila in matriz2:
            print(fila)
        print("\nMatriz Resulante: ")
        for fila in matrizResultante:
            print(fila)
        print("\n")
    
    else:
        print("\nNo se pueden sumas las matrices porque son de orden diferente.\n")
    
def multiplicarMatriz():
    print("\n")
    columnasMatriz1 = int(input("Ingresa la cantidad de columnas de la primer matriz: "))
    filasMatriz1 = int(input("Ingresa la cantidad de filas de la primer matriz: "))
    columnasMatriz2 = int(input("Ingresa la cantidad de columnas de la segunda matriz: "))
    filasMatriz2 = int(input("Ingresa la cantidad de filas de la segunda matriz: "))

    if(columnasMatriz1==filasMatriz2):
        filasProducto = filasMatriz1
        columnasProducto = columnasMatriz2
        matriz1 = []
        matriz2 = []

        print("\n")
        print("Matriz 1: ")
        for i in range(filasMatriz1):
            fila = []
            for j in range(columnasMatriz1):
                fila.append(int(input(f"Ingrese el valor [{i}][{j}]: ")))
            matriz1.append(fila)

        print("\nMatriz 2: ")
        for i in range(filasMatriz2):
            fila = []
            for j in range(columnasMatriz2):
                fila.append(int(input(f"Ingrese el valor [{i}][{j}]: ")))
            matriz2.append(fila)
        
        matrizResultante = []
        for i in range(filasProducto):
            fila = []
            for j in range(columnasProducto):
                suma = 0
                for k in range (len(matriz2)):
                    suma += matriz1[i][k] * matriz2[k][j]
                fila.append(suma)
            matrizResultante.append(fila)

        print("\nMatriz 1: ")
        for fila in matriz1:
            print(fila)
        print("\nMatriz 2: ")
        for fila in matriz2:
            print(fila)
        print("\nMatriz Resulante: ")
        for fila in matrizResultante:
            print(fila)
        print("\n")


    else:
        print("\nLas matrices no son conformables.\n")  

