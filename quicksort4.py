#!/usr/bin/python

import random
import timeit
import pickle
from random_nums_generation import store_values, get_randoms

def quicksort(arr, start, end, pivot_mode='random'):
	if start < end:
		split = partition(arr, start, end, pivot_mode)
		quicksort(arr, start, split-1, pivot_mode)
		quicksort(arr, split+1, end, pivot_mode)
	return arr

def partition(arr, start, end, pivot_mode):
	if pivot_mode == 'first':
		pivot = arr[start]
	else:
		pivot_index = random.randrange(start,end)
		pivot = arr[pivot_index]
		arr[pivot_index], arr[start] = arr[start], arr[pivot_index] # place the pivot at the beginning
	i = start + 1
	for j in range(start+1,end+1):
		if arr[j] < pivot:
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
	arr[start], arr[i-1] = arr[i-1], arr[start]
	return i-1

def main():
    quicksort_periods = []
    randoms = get_randoms()
    for i in randoms:
        big_arr = randoms[i]
        sort_period = timeit.Timer(lambda: quicksort(big_arr,0, len(big_arr)-1, 'first')).timeit(number=1)
        quicksort_periods.append(sort_period)
    store_values(quicksort_periods,'quick_sort.dat')

if __name__ == '__main__':
    main()