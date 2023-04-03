lst = [1, 2, "qwerty", "asd", "zxc", 4, 6]

filtered_list = list(filter(lambda x: x == int, lst))
print(list(filtered_list))

