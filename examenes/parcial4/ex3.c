/*
    Francisco Oro @ FI UNAM
    Estructura de Datos y Algoritmos II
    Examen Parcial 3
    Problema 3
*/
#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int main(int argc, char const *argv[])
{
    int sum[1000], A[1000], B[1000], thread;
    int operations[5] = {0,0,0,0,0};

    for (int i = 0; i < 1000; i++)
    {
        A[i] = i;
        B[i] = 1999 - i;
    }

    omp_set_num_threads(5);
    #pragma omp parallel for reduction(+:operations[omp_get_thread_num()])
    for (int i = 0; i < 1000; i++)
    {
        sum[i] = A[i] + B[i];
        thread = omp_get_thread_num();
        operations[thread]+=1;
        printf("Thread %d: %d\n", thread, operations[thread]);
    }

    for (int i = 0; i < 5; i++)
    {
        printf("Thread %d did %d operations\n", i, operations[i]);
    }
    return 0;
}