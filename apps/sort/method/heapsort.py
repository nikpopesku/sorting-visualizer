def heapify(arr, n, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    old_arr = arr[:]
    n = len(arr)

    # Build max heap
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]


        # Heapify root element
        heapify(arr, i, 0)

        if old_arr[i:n] != arr[i:n]:
            return arr

    return arr

def heapsort_iterative_average():
    return 'nlog(n)'

def heapsort_iterative_worst():
    return 'nlog(n)'

def heapsort_iterative_best():
    return 'nlog(n)'

def heapsort_space_complexity():
    return '1'
