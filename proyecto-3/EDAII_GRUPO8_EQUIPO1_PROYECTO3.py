#Importamos las funciones de los programas separados
from ACT31 import sumarMatrices,multiplicarMatriz
from ACT32 import ingresar_matriz, calcular_determinante, obtener_submatriz, imprimir_matriz
from ACT33 import main33
from ACT34 import traspuesta
from ACT35 import imprimir_matriz35, calcular_transpuesta35, calcular_adjunta35, calcular_determinante35,calcular_inversa35
from ACT36 import main

validacion = True

while(validacion):
    print("----- MENU -----")
    print("1.- Operaciones con Matrices")
    print("2.- Determinantes y Cofactores")
    print("3.- Sistemas de Ecuaciones con Regla de Cramer")
    print("4.- Traspuesta de una Matriz")
    print("5.- Matriz Inversa")
    print("6.- Sistemas de Ecuaciones con Matriz Inversa")
    print("7.- Salir")

    opcion = int(input("Selecciona una opcion: "))

    #Operaciones con Matrices
    if opcion == 1:
        print("\n1.- Sumar matrices")
        print("2.- Multiplicar matrices")
        opcion = int(input("Selecciona una opcion: "))
        if(opcion == 1):
            sumarMatrices()
        elif(opcion == 2):
            multiplicarMatriz()
        else:
            print("Opcion invalida.")

    #3.2.- Determinantes y Cofactores
    elif opcion == 2:
        print("\n * Cálculo del determinante de una matriz cuadrada * ")
        matriz = ingresar_matriz()
        print("\n-----------------")
        print("     Matriz")
        print("-----------------")
        imprimir_matriz(matriz)


        determinante = calcular_determinante(matriz)
        print("\n---------------------------------------")
        print("El determinante de la matriz es:", determinante)
        print("---------------------------------------")
    
    #3.3.- Regla de Cramer
    elif opcion == 3:
        print("\n * Calculo de sistemas de ecuaciones mediante regla de Cramer * \n")
        main33()

    #3.4.- Traspuesta
    elif opcion == 4:
        traspuesta()

    #3.5.- Matriz Inversa
    elif opcion == 5:
        n = int(input("\nIngrese el grado de la matriz cuadrada (n): "))

        matriz = [[float(input(f"Ingrese el elemento ({i+1}, {j+1}): ")) for j in range(n)] for i in range(n)]

        print("\nMatriz original:")
        imprimir_matriz35(matriz)

        matriz_inversa = calcular_inversa35(matriz,n)

        if matriz_inversa is not None:
            print("\nMatriz inversa:")
            imprimir_matriz35(matriz_inversa)
            print("\n")
        else:
            print("\nLa matriz no tiene inversa.\n")

    elif opcion == 6:
        print("\n * Cálculo de un Sistema de Ecuaciones 3x3 * \n")
        main()

    elif opcion == 7:
        print("\nGracias por utizar el programa.")
        validacion = False
    else:
        print("Opcion no válida")