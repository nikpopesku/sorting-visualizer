from numpy.random import randint


def generate_array(length: int) -> tuple:
    return range(1, length + 1), randint(0, 100, length)
