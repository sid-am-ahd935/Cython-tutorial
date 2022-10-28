# python_insertion_sort.py

def sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i - 1

        while j >= 0 and arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1

    return arr
