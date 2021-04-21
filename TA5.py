import random
import time


def countingSort(arr, exp):
 
    n = len(arr)
 
    output = [0] * (n)
 
    count = [0] * (10)
 
    for i in range(0, n):
        index = (arr[i] / exp)
        count[int(index % 10)] += 1
 
    for i in range(1, 10):
        count[i] += count[i - 1]
 
    i = n - 1
    while i >= 0:
        index = (arr[i] / exp)
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1

    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
 
def radixSort(arr, d):
 
    max1 = max(arr)
 
    exp = 1
    while max1 / exp > 0:
        countingSort(arr, exp)
        exp *= 10
 
 
def main():
    n = [10, 100, 1000, 10000] 
    d = int(input("Number of digits:")) 

    for i in n:
        arr = [random.randint(10**(d-1),10**d-1 ) for x in range(i)]
        start = time.process_time()
        radixSort(arr, d) 
        end = time.process_time()
        time_test = end - start 
        print ("Size: ", i)
        print ("RadixSort time:" , time_test, "\n")

if __name__=="__main__":
    main()
