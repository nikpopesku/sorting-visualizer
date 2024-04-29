def insertion_sort(array: list) -> list:
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

            return array

        # Place key at after the element just smaller than it.
        array[j + 1] = key

    return array

def insertion_average():
    return 'n2'

def insertion_worst():
    return 'n2'

def insertion_best():
    return 'n'
