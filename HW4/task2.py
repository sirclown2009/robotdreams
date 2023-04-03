def add_num(*args):
    total = 0
    for i in args:
        total = total + i
    print(total)


add_num(10, 5, 3)
add_num(2, 3)
add_num(9, 13, 2, 8, 10, 11)

