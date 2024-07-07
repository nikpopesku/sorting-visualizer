def partition(arr: list, l: int, h: int) -> int:
    i = l - 1
    x = arr[h]

    for j in range(l, h):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]

    return i + 1


def quicksort_iterative(arr: list) -> list:
    xxx = arr[:]
    l = 0
    h = len(arr) - 1
    # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * size
    # initialize top of stack
    top = -1
    # push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
    # Keep popping from stack while is not empty
    while top >= 0:
        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        # Set pivot element at its correct position in
        # sorted array
        p = partition(arr, l, h)

        if xxx != arr:
            return arr

        # If there are elements on left side of pivot,
        # then push left side to stack
        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        if xxx != arr:
            return arr

        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

        if xxx != arr:
            return arr

    return arr


def quicksort_iterative_average():
    return 'nlog(n)'

def quicksort_iterative_worst():
    return 'n2'

def quicksort_iterative_best():
    return 'nlog(n)'

def quicksort_iterative_explanation():
    return ''

def quicksort_space_complexity():
    return 'nlog(n)'
