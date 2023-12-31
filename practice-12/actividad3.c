#include <stdio.h>
#include <omp.h>

long long num_steps = 100000000;
double step;
double empezar, terminar;

int main(int argc, char const *argv[])
{
    double x, pi, sum = 0.0;
    int i;
    step = 1.0 / (double)num_steps;
    empezar = omp_get_wtime();

    #pragma omp parallel for reduction(+:sum) // Directiva pragma
    for ( i = 0; i < num_steps; i++)
    {
        x = (i + .5)*step;
        sum +=  4.0 / (1. + x*x);
    }

    pi = sum * step; 
    terminar = omp_get_wtime();

    printf("El valor de PI es %15.2f\n", pi);
    printf("El tiempo de cálculo del pi es %lf segundos ", terminar-empezar);
    
    return 0;
}
