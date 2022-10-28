# cython: language_level=3
# To tell cython we are using Python3

# cython_insertion_sort.pyx


from array import array
from cpython cimport array


cpdef list sort(list nums):
    cdef int n = len(nums)
    cdef int i, j
    cpdef int[:] arr = array("i", nums)

    for i in range(1, n):
        j = i - 1

        while j >= 0 and arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1

    return list(arr)
