import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                yield j, j+1
    yield None, None

def visualize_sort(arr):
    generator = bubble_sort(arr)
    for (i, j) in generator:
        if i is None:
            for x in arr:
                print("{}".format(x), end=" ")
            print("")
            return

        for k, x in enumerate(arr):
            if k == i or k == j:
                print("\033[91m{}\033[0m".format(x), end=" ")
            else:
                print("{}".format(x), end=" ")
        print("")
        time.sleep(0.1)

arr = [random.randint(1, 100) for x in range(10)]
print("Original Array: ", arr)
visualize_sort(arr)
