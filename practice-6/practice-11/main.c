#include <omp.h>
#include <stdio.h>

void Suma(int *A, int *B, int *C, int n);
int main(int argc, char const *argv[])
{
    int a[3] = {1,2,3}, b[3] = {4, 5, 6}, c[3] = {7, 8, 9};
    Suma(a, b, c, 3);
    return 0;
}

void Suma(int A[], int B[], int C[], int n)
{   
    int i, tid;

    #pragma omp parallel private(tid)
    {
        tid = omp_get_thread_num();
        #pragma omp for
        for ( i = 0; i < n; i++)
        {
            C[i] = A[i] + B[i]; 
            printf("hilo %d calculo C[%d] = %d\n", tid, i, C[i]);
        }
        
    }

}
