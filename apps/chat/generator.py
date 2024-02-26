from numpy.random import randint, seed


def generate_array(length: int) -> tuple:
    values = randint(0, 100, length)
    keys = range(1, length + 1)

    return keys, values
