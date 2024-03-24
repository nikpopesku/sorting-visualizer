def bubble_sort(arr: list) -> list:
    xxx = list(arr)
    for i in range(len(xxx)):
        for j in range(i, len(xxx)):
            if xxx[i] > xxx[j]:
                xxx[i], xxx[j] = xxx[j], xxx[i]
                return xxx

    return xxx
