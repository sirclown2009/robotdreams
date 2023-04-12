def recursion(inp):
    print(inp, end=" ")
    if inp == 0:
        return

    recursion(inp - 1)


inp = int(input("Please type in a number: "))
recursion(inp)
