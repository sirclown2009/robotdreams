lst = [1, 2, "qwerty", "asd", "zxc", 4, 6, 7]


filtered_list = list(filter(lambda x: isinstance(x, int), lst))
print(list(filtered_list))