/*
    Practica 13 - Ejercicio 3
    Equipo 2
    Estructura de Datos y Algoritmos 2
*/

#include <stdio.h>  

long fibonacci (int n); 

 

int main(int argc, char const *argv[]) 

{ 

    int nthr = 0; 

    int n; 

    long result; 

    printf("\n Numero a calcular? "); 

    scanf("%d", &n); 

    result = fibonacci(n); 

    printf("\n El numero de Fibonacci de %5d es %d", n, result); 

    return 0; 

} 

 

long fibonacci(n) 

{ 

    long fn1, fn2, fn; 

    int id; 

    if (n == 0 || n==1) 

    { 

        return(n); 

    } 

 

    if (n < 30) 

    { 

       fn1 = fibonacci(n-1); 

       fn2 = fibonacci(n-2); 

       fn = fn1 + fn2; 

    } 

    return (fn); 

} 