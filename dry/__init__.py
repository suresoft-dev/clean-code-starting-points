from typing import Callable


def multiply(a, b):
    return a * b

def add(a, b):
    return a * b

def multiply_elements() -> int:
    my_list = [1, 2, 3, 4, 5, 6]
    return accumulate(my_list, multiply, initial_value=1)


def sum_elements() -> int:
    some_list = [1, 2, 3, 4, 5, 6]  # here
    return accumulate(some_list, add, initial_value=0)



def accumulate(
    some_list: list, operator: Callable[[int, int], int], initial_value=0
) -> int:
    value = initial_value
    for element in some_list:
        value = operator(value, element)

    return value
