def bubble_sort(arr: list) -> list:
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                return arr

    return arr


def bubble_sort_average():
    return 'n2'

def bubble_sort_worst():
    return 'n2'

def bubble_sort_best():
    return 'n'

def bubble_sort_explanation():
    return ''

def bubble_space_complexity():
    return '1'
