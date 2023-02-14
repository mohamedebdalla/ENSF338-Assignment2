import json
import time
import matplotlib.pyplot as plt

# Import the sorting function from the previous question
import sys
sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

# Load the data from the provided URL
import urllib.request
url = "https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment2/ex2.json"
response = urllib.request.urlopen(url)
data = json.loads(response.read().decode())

# Create lists to store the input sizes and corresponding times
input_sizes = []
times = []

# Test the sorting function for each input size and record the time taken
for arr in data:
    arr = list(map(int, arr))
    size = len(arr)
    start_time = time.time()
    func1(arr, 0, size-1)
    end_time = time.time()
    input_sizes.append(size)
    times.append(end_time - start_time)

# Plot the timing results
plt.plot(input_sizes, times)
plt.title("Execution Time of QuickSort Algorithm")
plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.show()
