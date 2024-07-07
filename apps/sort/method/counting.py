def counting_sort(array: list) -> list:
    initial_arr = array[:]
    size = len(array)
    output = [0] * size

    mmax = max(array)
    # Initialize count array
    count = [0] * (mmax + 1)



    # Store the count of each element in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, mmax+1):
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
        temp = array[i]
        array[i] = output[i]

        if initial_arr[i] != array[i]:
            index = initial_arr.index(output[i], i)
            array[index] = temp

            return array

    return array

def counting_average():
    return 'n+k'

def counting_worst():
    return 'n+k'

def counting_best():
    return 'n+k'

def counting_explanation():
    return '<div>max - is the maximum value in the array</div><div>k - is number of different values in the array</div>'

def counting_space_complexity():
    return 'max'
