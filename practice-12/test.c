#include <omp.h>
#include <stdio.h>

int main(int argc, char const *argv[])
{
    int A[1000], B[1000], C[1000];
    int tid, nth;

    for (int i = 0; i < 1000; i++)
    {
        A[i] = i;
        B[i] = i;
    }
    
    #pragma omp parallel private(tid)
    {
        tid = omp_get_thread_num();
        nth = omp_get_num_threads();

        for (int i = 0; i < 1000; i++)
        {
            C[i] = A[i] + B[i];
            printf("Hilo %d C[%d]=%d\n", tid, i, C[i]);
        }
        
    } // End of parallel region 
    return 0;
}
