def set_equal_numbers():
    set1 = {1, 2, 3, 4, 5}
    set2 = {1, 3, 6, 7, 4}
    return print(set1.intersection(set2))


def set_unique_numbers():
    set1 = {1, 2, 3, 4, 5, 8}
    set2 = {1, 3, 6, 7, 4, 10}
    return print(set1.difference(set2))


set_equal_numbers()
set_unique_numbers()