# this program generates random numbers and stores them in a file for comparison
import random
import pickle


# Create a list of random numbers
sort_length = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
rand_nums_dictionary = dict.fromkeys(sort_length,0)

for sortnum in sort_length:
    rand_nums_dictionary[sortnum] = [random.random() for _ in range(sortnum)]

# Store the list of random numbers in a file
with open('rand_nums.dat', 'wb') as file:
    pickle.dump(rand_nums_dictionary, file)

# Retrieve the list of random numbers from the file
def get_randoms():
    with open('rand_nums.dat','rb') as file:
        rand_nums = pickle.load(file)
    file.close()
    return rand_nums

# Store values of periods in file
def store_values(data,fname):
    with open(fname,'wb') as file:
        pickle.dump(data,file)