def counting_sort(array: list) -> list:
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * 100

    # Store the count of each element in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]

    return array

def counting_iterative_average():
    return 'nlog(n)'

def counting_iterative_worst():
    return 'n2'

def counting_iterative_best():
    return 'nlog(n)'

def counting_space_complexity():
    return 'nlog(n)'
