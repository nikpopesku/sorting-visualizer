from numpy.random import randint, seed


def generate_array(seed_value: int, length: int) -> tuple:
    seed(seed_value)
    values = randint(0, 100, length)
    keys = range(1, length + 1)

    return keys, values
