from numpy.random import randint


def generate_array(length: int, array_type: str) -> tuple:
    keys = range(1, length + 1)
    print("array_type: ", array_type)

    if array_type == "":
        values = randint(0, 100, length)
    elif array_type == "bubble":
        values = randint(0, 20, length)
    elif array_type == "merge":
        values = randint(0, 200, length)
    else:
        values = randint(0, 100, length)


    return keys, values
