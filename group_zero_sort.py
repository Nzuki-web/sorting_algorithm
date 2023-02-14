import pickle
import matplotlib.pyplot as plt

def getdata():
    with open('merge_sort.dat','rb') as mf:
        merge_data = pickle.load(mf)
    with open('quick_sort.dat','rb') as qf:
        qsdata = pickle.load(qf)
    periods = {}
    periods['merge_sort'] = merge_data
    periods['quick_sort'] = qsdata
    mf.close()
    qf.close()
    return periods

# Plot graphs
def plot_graphs(periods):
    sort_length = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
    plt.plot(sort_length,periods['merge_sort'], label = "Merge Sort")
    plt.plot(sort_length,periods['quick_sort'], label = 'Quick Sort')

    plt.xlabel('Number of sorted elements (n)')
    plt.ylabel('Time taken to sort elements, T(n) (s)')
    plt.title('Comparison of Sorting Algorithms')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    periods = getdata()
    plot_graphs(periods)