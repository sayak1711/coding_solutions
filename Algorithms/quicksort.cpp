//QUICKSORT
#include <iostream>
using namespace std;

void swap(int* a, int* b)
{
	int temp = *a;
	*a = *b;
	*b = temp;
}

int partition(int arr[], int start, int end)
{
	int pivot = arr[end];
	int i = start-1;
	for(int j = start; j < end; j++)
	{
		if(arr[j] <= pivot)
		{
			i++;
			swap(&arr[j], &arr[i]);
		}
	}
	swap(arr[i+1], arr[end]);
	return i+1;
}

void quicksort(int arr[], int start, int end)
{
	if(start < end)
	{
		int splitpoint = partition(arr, start, end);
		quicksort(arr, start, splitpoint-1);
		quicksort(arr, splitpoint+1, end);
	}
}

int main() 
{
	int arr[] = {7, 6, 2, 1, 0, 9, 4, 8};
	quicksort(arr, 0, 7);
	for(int i = 0; i < 8; i++)
	    cout<<arr[i]<<" ";
	return 0;
}