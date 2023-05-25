def multiply_elements() -> int:
    my_list = [1, 2, 3, 4, 5, 6]
    product = 1
    for element in my_list:
        product = product * element

    return product


def sum_elements() -> int:
    some_list = [1, 2, 3, 4, 5, 6]
    total = 0
    for element in some_list:
        total = total + element

    return total