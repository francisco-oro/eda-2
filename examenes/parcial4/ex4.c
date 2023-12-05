// C program for implementation of Bubble sort 
#include <stdio.h> 
#include <omp.h> // include the OpenMP library

// Swap function 
void swap(int* arr, int i, int j) 
{ 
	int temp = arr[i]; 
	arr[i] = arr[j]; 
	arr[j] = temp; 
} 

// A function to implement bubble sort 
void bubbleSort(int arr[], int n) 
{ 
	int i, j; 
	for (i = 0; i < n - 1; i++) 

		// Last i elements are already 
		// in place 
		for (j = 0; j < n - i - 1; j++) 
			if (arr[j] > arr[j + 1]) 
				swap(arr, j, j + 1); 
} 

void parallelBubbleSort(int arr[], int n, int num_threads) 
{ 
    omp_set_num_threads(num_threads);

    int ops[num_threads];
    for (int i = 0; i < num_threads; i++) {
        ops[i] = 0;
    }

    #pragma omp parallel
    {
        int thread_id = omp_get_thread_num();

        #pragma omp for schedule(dynamic)
        for (int i = 0; i < n - 1; i++) {
            #pragma omp critical
            {
                bubbleSort(arr, n);

                ops[thread_id]++;
            }
        }
    }

    // Print the number of operations by each thread
    for (int i = 0; i < num_threads; i++) {
        printf("Thread %d did %d operations\n", i, ops[i]);
    }
}

// Function to print an array 
void printArray(int arr[], int size) 
{ 
	int i; 
	for (i = 0; i < size; i++) 
		printf("%d ", arr[i]); 
	printf("\n"); 
} 

// Driver code 
int main() 
{ 
	int arr[1000];
    for (int i = 0; i < 1000; i++)
    {
        arr[i] = 1000-i;
    }
    int N = sizeof(arr) / sizeof(arr[0]); 
    printf("Original array: "); 
    printArray(arr, N); 

    int num_threads = 5;

    parallelBubbleSort(arr, N, num_threads);
	return 0; 
}
