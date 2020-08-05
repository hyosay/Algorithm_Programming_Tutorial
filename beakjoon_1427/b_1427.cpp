#define _CRT_SECURE_NO_WARNING
#include <stdio.h>


int data[10] = { 10, 8, 1, 2, 5, 9, 3, 4, 7, 6 };
void Quicksort(int *data,int start,int end) {
	if (start >= end) {
		return;
	}
	int pivot = start;
	int L = start;
	int R = end;
	int temp;

	while (L <= R) {
		while (data[L] < data[pivot])	L++;
		while (data[R] >= data[pivot] && R > start) R--;

	}
	if (L > R) {
		temp = data[R];
		data[R] = data[pivot];
		data[pivot] = temp;
	}
	else {
		temp = data[R];
		data[R] = data[L];
		data[L] = temp;
	}
	Quicksort(data, start, R - 1);
	Quicksort(data, R + 1, end);
}



int main(void) {
	Quicksort(data, 0, 9);
	for (int i = 0; i < 10; i++) {
		printf("%d",data[i]);
	}

}