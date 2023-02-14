import timeit
import pickle
import matplotlib.pyplot as plt
from random_nums_generation import get_randoms, store_values

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
def main():
    randoms = get_randoms()
    merge_periods = []
    for i in randoms:
        arr = randoms[i]
        sort_period = timeit.Timer(lambda: merge_sort(arr)).timeit(number=1)
        merge_periods.append(sort_period)
    
    sort_length = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
    plt.plot(sort_length,merge_periods)
    plt.xlabel("Number of elements sorted, n")
    plt.ylabel("Time taken to sort n elements, T(n)")
    plt.title('Merge Sort Performance')
    plt.legend()
    plt.show()
    store_values(merge_periods,'merge_sort.dat')

if __name__ == '__main__':
    main()