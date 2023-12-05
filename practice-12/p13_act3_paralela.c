/*
    Practica 13 - Ejercicio 3
    Equipo 2
    Estructura de Datos y Algoritmos 2
*/

#include <stdio.h> 

#include <omp.h> 

long fibonacci (int n); 

 

int main(int argc, char const *argv[]) 

{ 

    in nthr = 0; 

    int n; 

    long result; 

    printf("\n Numero a calcular? "); 

    scanf("%d", &n); 

 

    #pragma omp parallel 

    { 

        #pragma omp single 

        { 

            result = fibonacci(n); 

        } 

    } 

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

        #pragma omp task shared(fn1) 

        { 

            fn1 = fibonacci(n-1); 

        } 

        #pragma omp task shared(fn2) 

        { 

            fn2 = fibonacci(n-2); 

        } 

        #pragma omp taskwait 

        { 

            fn = fn1 + fn2; 

        } 

    } 

    return (fn); 

} 